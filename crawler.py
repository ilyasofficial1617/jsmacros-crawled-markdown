from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse, urljoin
import time
import markdownify
import os
import hashlib
import logging

class CustomMarkdownConverter(markdownify.MarkdownConverter):
    def convert_table(self, el, text, convert_as_inline):
        # First, let's get all rows
        rows = el.find_all(['tr'])
        if not rows:
            return ''
        
        # Initialize the markdown table
        table_markdown = []
        
        # Process header row
        header = rows[0]
        header_cols = header.find_all(['th', 'td'])
        header_md = '| ' + ' | '.join(col.get_text().strip() for col in header_cols) + ' |'
        table_markdown.append(header_md)
        
        # Add separator row
        separator = '|' + '|'.join(['---' for _ in header_cols]) + '|'
        table_markdown.append(separator)
        
        # Process data rows
        for row in rows[1:]:
            cols = row.find_all(['td'])
            if cols:
                row_md = '| ' + ' | '.join(col.get_text().strip() for col in cols) + ' |'
                table_markdown.append(row_md)
        
        return '\n'.join(table_markdown) + '\n\n'

class Crawler:
    def __init__(self, start_url, excluded_links=None):
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        self.start_url = start_url
        self.domain = urlparse(start_url).netloc
        self.visited_urls = set()
        self.visited_titles = set()
        self.content_hashes = set()
        self.excluded_links = set(excluded_links or [])
        
        # Setup Chrome in fullscreen
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def wait_for_load(self):
        """Wait for page to load"""
        time.sleep(5)  # Changed from 1.5 to 2 seconds
        
    def get_markdown(self):
        """Convert current page content to markdown"""
        main_content = self.wait.until(
            EC.presence_of_element_located((By.ID, "mainContent"))
        )
        html_content = main_content.get_attribute('innerHTML')
        converter = CustomMarkdownConverter()
        return converter.convert(html_content)
    
    def get_page_title(self):
        """Get the page title from h2.classTitle or fallback to first h2"""
        try:
            # First try to find h2.classTitle
            title_element = self.driver.find_element(By.CSS_SELECTOR, "h2.classTitle")
            return title_element.text.strip()
        except:
            try:
                # Fallback to any h2
                title_element = self.driver.find_element(By.TAG_NAME, "h2")
                return title_element.text.strip()
            except:
                return None
    
    def is_page_visited(self, title):
        """Check if page with this title has been visited"""
        if not title:
            return False
        if title in self.visited_titles:
            return True
        self.visited_titles.add(title)
        return False
    
    def is_content_duplicate(self, title):
        """Check if content is duplicate based on title"""
        if not title:
            return False
        content_hash = hashlib.md5(title.encode()).hexdigest()
        if content_hash in self.content_hashes:
            return True
        self.content_hashes.add(content_hash)
        return False
    
    def save_markdown(self, content, title):
        """Save markdown content to file"""
        if not title:
            title = 'unnamed_page'
        
        # Clean filename but preserve dots and $ signs
        # Only remove characters that are actually invalid for filenames
        invalid_chars = '<>:"/\\|?*'
        filename = "".join(c for c in title if c not in invalid_chars)
        filename = f"output/{filename}.md"
        
        self.logger.info(f"Saving to file: {filename}")
        os.makedirs('output', exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def is_same_domain(self, url):
        """Check if URL belongs to same domain"""
        return urlparse(url).netloc == self.domain
    
    def normalize_url(self, url):
        """Remove fragment identifier and normalize URL"""
        parsed = urlparse(url)
        return urljoin(self.start_url, parsed.path)
    
    def explore_page(self, current_url, depth=0):
        """Recursively explore all buttons in mainContent"""
        indent = "  " * depth
        try:
            self.logger.info(f"{indent}Current URL: {current_url}")
            
            # Check if we've seen this page title before
            title = self.get_page_title()
            self.logger.info(f"{indent}Exploring page: {title or 'Untitled'} (Depth: {depth})")
            
            if self.is_page_visited(title):
                self.logger.info(f"{indent}Skipping already visited page: {title}")
                return
            
            # Convert current page to markdown and save if unique content
            if not self.is_content_duplicate(title):
                self.logger.info(f"{indent}Found unique content, saving markdown for: {title}")
                content = self.get_markdown()
                self.save_markdown(content, title)
            else:
                self.logger.info(f"{indent}Duplicate content detected for: {title}")
            
            # Find all clickable elements in mainContent
            try:
                main_content = self.wait.until(
                    EC.presence_of_element_located((By.ID, "mainContent"))
                )
            except TimeoutException:
                self.logger.error(f"{indent}Timeout waiting for mainContent on URL: {current_url}")
                return
            
            # Get all clickable elements
            clickable_elements = main_content.find_elements(By.CSS_SELECTOR, "button, a[href]")
            
            self.logger.info(f"{indent}Found {len(clickable_elements)} clickable elements")
            
            # Store element information for re-finding if needed
            elements_info = []
            for element in clickable_elements:
                try:
                    # Check if element is within subClasses
                    try:
                        parent_subclasses = element.find_element(By.XPATH, "./ancestor::*[@id='subClasses']")
                        if parent_subclasses:
                            self.logger.debug(f"{indent}Skipping element in subClasses")
                            continue
                    except:
                        pass  # Element is not in subClasses, continue processing

                    element_href = element.get_attribute('href') if element.tag_name == 'a' else ''
                    element_text = element.text.strip()
                    
                    self.logger.debug(f"{indent}Checking element: [{element.tag_name}] "
                                    f"text='{element_text}' href='{element_href}'")
                    
                    # Skip if href contains '#' or http(s)://
                    if element_href and ('#' in element_href or 'http://' in element_href or 'https://' in element_href):
                        self.logger.info(f"{indent}Skipping external/fragment link: {element_href}")
                        continue
                        
                    element_info = {
                        'tag_name': element.tag_name,
                        'text': element_text,
                        'href': element_href,
                        'index': len(elements_info)
                    }
                    elements_info.append(element_info)
                    self.logger.debug(f"{indent}Added element to process queue: {element_info}")
                    
                except StaleElementReferenceException as e:
                    self.logger.error(f"{indent}Stale element while gathering info on URL {current_url}: {str(e)}")
                    continue
            
            self.logger.info(f"{indent}Processing {len(elements_info)} elements after filtering")
            
            for i, element_info in enumerate(elements_info, 1):
                try:
                    element_text = element_info['text']
                    element_href = element_info['href']
                    tag_name = element_info['tag_name']
                    
                    self.logger.info(f"{indent}Processing element {i}/{len(elements_info)}: "
                                   f"[{tag_name}] {element_text or element_href}")
                    
                    if (element_text in self.excluded_links or 
                        element_href in self.excluded_links):
                        self.logger.info(f"{indent}Skipping excluded link: {element_text or element_href}")
                        continue
                    
                    # Try to find and click the element
                    try:
                        # Re-find the element
                        main_content = self.wait.until(
                            EC.presence_of_element_located((By.ID, "mainContent"))
                        )
                        clickable_elements = main_content.find_elements(
                            By.CSS_SELECTOR, 
                            "button, a[href]"
                        )
                        element = clickable_elements[element_info['index']]
                        
                        # Double check href before clicking
                        current_href = element.get_attribute('href') if element.tag_name == 'a' else ''
                        if current_href and ('#' in current_href or 'http://' in current_href or 'https://' in current_href):
                            self.logger.info(f"{indent}Skipping external/fragment link (double-check): {current_href}")
                            continue
                        
                        self.logger.info(f"{indent}Clicking element: {element_text or element_href}")
                        element.click()
                        self.wait_for_load()
                        
                        # Recursively explore the new page state
                        self.explore_page(self.driver.current_url, depth + 1)
                        
                        self.logger.info(f"{indent}Navigating back from: {element_text or element_href}")
                        # Go back
                        self.driver.back()
                        self.wait_for_load()
                        
                    except (StaleElementReferenceException, IndexError) as e:
                        self.logger.error(f"{indent}Failed to re-find element on URL {current_url}: {str(e)}")
                        self.logger.error(f"{indent}Element info: {element_info}")
                        continue
                    
                except Exception as e:
                    self.logger.error(f"{indent}Error processing element on URL {current_url}: {str(e)}")
                    self.logger.error(f"{indent}Element info: {element_info}")
                    continue
                    
        except Exception as e:
            self.logger.error(f"{indent}Unexpected error on URL {current_url}: {str(e)}")
    
    def crawl(self):
        """Main crawling method"""
        try:
            # Load initial page
            self.logger.info("Starting crawl at: %s", self.start_url)
            self.driver.get(self.start_url)
            time.sleep(20)  # Wait 20 seconds for initial load
            
            # Get all navigation links from sidebar
            sidebar = self.wait.until(
                EC.presence_of_element_located((By.ID, "mainNav"))
            )
            nav_links = sidebar.find_elements(By.TAG_NAME, "a")
            self.logger.info(f"Found {len(nav_links)} main navigation links")
            
            # Process each main navigation link
            for i, link in enumerate(nav_links, 1):
                try:
                    href = link.get_attribute('href')
                    link_text = link.text.strip()
                    
                    self.logger.info(f"\nProcessing main navigation {i}/{len(nav_links)}: {link_text}")
                    
                    if not href or not self.is_same_domain(href):
                        self.logger.info(f"Skipping external navigation link: {href}")
                        continue
                    
                    # Click the navigation link
                    self.logger.info(f"Clicking main navigation: {link_text}")
                    link.click()
                    self.wait_for_load()
                    
                    # Explore the main page and all its sub-pages
                    self.explore_page(self.driver.current_url)
                    
                except (StaleElementReferenceException, TimeoutException) as e:
                    self.logger.error(f"Error processing navigation link: {str(e)}")
                    continue
                    
        finally:
            self.logger.info("Crawl completed. Closing browser.")
            self.driver.quit()

if __name__ == "__main__":
    START_URL = "https://jsmacros.wagyourtail.xyz/?general.html"
    # Example of excluded links - add any text or URLs you want to skip
    EXCLUDED_LINKS = [
        "Skip this link",
        "https://example.com/skip-this-url",
        "Don't click me",
        "https://jsmacros.wagyourtail.xyz/1.9.2/https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App",
        "https://jsmacros.wagyourtail.xyz/1.9.2/"
    ]
    crawler = Crawler(START_URL, excluded_links=EXCLUDED_LINKS)
    crawler.crawl()
