

xyz.wagyourtail.jsmacros.client.gui.screens.EditorScreen
--------------------------------------------------------

#### extends [BaseScreen](1.9.2/xyz/wagyourtail/wagyourgui/BaseScreen.html)

### Constructors

#### new EditorScreen (parent, file)

| Parameter | Type | Description |
|---|---|---|
| parent | Screen |  |
| file | File |  |



#### Fields

[langs](#langs)
S
F


[defaultStyle](#defaultStyle)
S


[history](#history)
F


[cursor](#cursor)
F


[blockFirst](1.9.2/)


[textRenderTime](1.9.2/)


[prevChar](1.9.2/)


[language](#language)


[codeCompiler](#codeCompiler)



#### Methods

[getDefaultLanguage()](#getDefaultLanguage-)


[openAndScrollToIndex(file, startIndex, endIndex)](#openAndScrollToIndex-File-int-int-)
S


[openAndScrollToLine(file, line, col, endCol)](#openAndScrollToLine-File-int-int-int-)
S


[setScroll(pages)](#setScroll-double-)


[setLanguage(language)](#setLanguage-String-)


[init()](#init-)


[copyToClipboard()](#copyToClipboard-)


[pasteFromClipboard()](#pasteFromClipboard-)


[cutToClipboard()](#cutToClipboard-)


[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[scrollToCursor()](#scrollToCursor-)


[save()](#save-)


[needSave()](#needSave-)


[mouseScrolled(mouseX, mouseY, horiz, vert)](#mouseScrolled-double-double-double-double-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[openParent()](#openParent-)


[mouseClicked(mouseX, mouseY, btn)](#mouseClicked-double-double-int-)


[selectWordAtCursor()](#selectWordAtCursor-)


[mouseDragged(mouseX, mouseY, button, deltaX, deltaY)](#mouseDragged-double-double-int-double-double-)


[updateSettings()](#updateSettings-)


[charTyped(chr, keyCode)](#charTyped-char-int-)



### Fields

#### .langs

Static
Final

##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .defaultStyle

Static

##### Type: [Style](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Style)



#### .history

Final

##### Type: [History](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/History.html)



#### .cursor

Final

##### Type: [SelectCursor](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/SelectCursor.html)



#### .blockFirst


##### Type: boolean



#### .textRenderTime


##### Type: long



#### .prevChar


##### Type: char



#### .language


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .codeCompiler


##### Type: [AbstractRenderCodeCompiler](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/AbstractRenderCodeCompiler.html)



### Methods

#### .getDefaultLanguage()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .openAndScrollToIndex(file, startIndex, endIndex)

Static
| Parameter | Type | Description |
|---|---|---|
| file | File |  |
| startIndex | int |  |
| endIndex | int |  |

##### Returns: void



#### .openAndScrollToLine(file, line, col, endCol)

Static
| Parameter | Type | Description |
|---|---|---|
| file | File |  |
| line | int |  |
| col | int |  |
| endCol | int |  |

##### Returns: void



#### .setScroll(pages)

| Parameter | Type | Description |
|---|---|---|
| pages | double |  |

##### Returns: void



#### .setLanguage(language)

| Parameter | Type | Description |
|---|---|---|
| language | String |  |

##### Returns: void



#### .init()


##### Returns: void



#### .copyToClipboard()


##### Returns: void



#### .pasteFromClipboard()


##### Returns: void



#### .cutToClipboard()


##### Returns: void



#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean



#### .scrollToCursor()


##### Returns: void



#### .save()


##### Returns: void



#### .needSave()


##### Returns: boolean



#### .mouseScrolled(mouseX, mouseY, horiz, vert)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| horiz | double |  |
| vert | double |  |

##### Returns: boolean



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .openParent()


##### Returns: void



#### .mouseClicked(mouseX, mouseY, btn)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| btn | int |  |

##### Returns: boolean



#### .selectWordAtCursor()


##### Returns: void



#### .mouseDragged(mouseX, mouseY, button, deltaX, deltaY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |
| deltaX | double |  |
| deltaY | double |  |

##### Returns: boolean



#### .updateSettings()


##### Returns: void



#### .charTyped(chr, keyCode)

| Parameter | Type | Description |
|---|---|---|
| chr | char |  |
| keyCode | int |  |

##### Returns: boolean




