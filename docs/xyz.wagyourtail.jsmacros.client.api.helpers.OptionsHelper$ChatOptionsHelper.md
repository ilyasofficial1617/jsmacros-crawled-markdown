

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper$ChatOptionsHelper
---------------------------------------------------------------------------

#### 

### Constructors

#### new OptionsHelper$ChatOptionsHelper (OptionsHelper)

| Parameter | Type | Description |
|---|---|---|
| OptionsHelper | OptionsHelper |  |



#### Fields

[parent](#parent)
F



#### Methods

[getParent()](#getParent-)


[getChatVisibility()](#getChatVisibility-)


[setChatVisibility(mode)](#setChatVisibility-String-)


[areColorsShown()](#areColorsShown-)


[setShowColors(val)](#setShowColors-boolean-)


[areWebLinksEnabled()](#areWebLinksEnabled-)


[enableWebLinks(val)](#enableWebLinks-boolean-)


[isWebLinkPromptEnabled()](#isWebLinkPromptEnabled-)


[enableWebLinkPrompt(val)](#enableWebLinkPrompt-boolean-)


[getChatOpacity()](#getChatOpacity-)


[setChatOpacity(val)](#setChatOpacity-double-)


[setTextBackgroundOpacity(val)](#setTextBackgroundOpacity-double-)


[getTextBackgroundOpacity()](#getTextBackgroundOpacity-)


[getTextSize()](#getTextSize-)


[setTextSize(val)](#setTextSize-double-)


[getChatLineSpacing()](#getChatLineSpacing-)


[setChatLineSpacing(val)](#setChatLineSpacing-double-)


[getChatDelay()](#getChatDelay-)


[setChatDelay(val)](#setChatDelay-double-)


[getChatWidth()](#getChatWidth-)


[setChatWidth(val)](#setChatWidth-double-)


[getChatFocusedHeight()](#getChatFocusedHeight-)


[setChatFocusedHeight(val)](#setChatFocusedHeight-double-)


[getChatUnfocusedHeight()](#getChatUnfocusedHeight-)


[setChatUnfocusedHeight(val)](#setChatUnfocusedHeight-double-)


[getNarratorMode()](#getNarratorMode-)


[setNarratorMode(mode)](#setNarratorMode-String-)


[areCommandSuggestionsEnabled()](#areCommandSuggestionsEnabled-)


[enableCommandSuggestions(val)](#enableCommandSuggestions-boolean-)


[areMatchedNamesHidden()](#areMatchedNamesHidden-)


[enableHideMatchedNames(val)](#enableHideMatchedNames-boolean-)


[isDebugInfoReduced()](#isDebugInfoReduced-)


[reduceDebugInfo(val)](#reduceDebugInfo-boolean-)



### Fields

#### .parent

Final

##### Type: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)



### Methods

#### .getParent()

1.8.4


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

the parent options helper.



#### .getChatVisibility()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current chat visibility mode.



#### .setChatVisibility(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the new chat visibility mode. Must be "FULL", "SYSTEM" or "HIDDEN |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .areColorsShown()

1.8.4


##### Returns: boolean

`true` if messages can use color codes, `false` otherwise.



#### .setShowColors(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to allow color codes in messages or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .areWebLinksEnabled()

1.8.4


##### Returns: boolean

`true` if it's allowed to open web links from chat, `false`
otherwise.



#### .enableWebLinks(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to allow opening web links from chat or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .isWebLinkPromptEnabled()

1.8.4


##### Returns: boolean

`true` if a warning prompt before opening links should be shown,
`false` otherwise.



#### .enableWebLinkPrompt(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to show warning prompts before opening links or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatOpacity()

1.8.4


##### Returns: double

the current chat opacity.



#### .setChatOpacity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat opacity |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .setTextBackgroundOpacity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new background opacity for text |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getTextBackgroundOpacity()

1.8.4


##### Returns: double

the current background opacity of text.



#### .getTextSize()

1.8.4


##### Returns: double

the current text size.



#### .setTextSize(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new text size |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatLineSpacing()

1.8.4


##### Returns: double

the current chat line spacing.



#### .setChatLineSpacing(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat line spacing |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatDelay()

1.8.4


##### Returns: double

the current chat delay in seconds.



#### .setChatDelay(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat delay in seconds |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatWidth()

1.8.4


##### Returns: double

the current chat width.



#### .setChatWidth(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat width |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatFocusedHeight()

1.8.4


##### Returns: double

the focused chat height.



#### .setChatFocusedHeight(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new focused chat height |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getChatUnfocusedHeight()

1.8.4


##### Returns: double

the unfocused chat height.



#### .setChatUnfocusedHeight(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new unfocused chat height |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .getNarratorMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current narrator mode.



#### .setNarratorMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the mode to set the narrator to. Must be either "OFF", "ALL", "CHAT", or
                                     "SYSTEM" |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .areCommandSuggestionsEnabled()

1.8.4


##### Returns: boolean

`true` if command suggestions are enabled



#### .enableCommandSuggestions(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable command suggestions or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .areMatchedNamesHidden()

1.8.4


##### Returns: boolean

`true` if messages from blocked users are hidden.



#### .enableHideMatchedNames(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to hide messages of blocked users or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.



#### .isDebugInfoReduced()

1.8.4


##### Returns: boolean

`true` if reduced debug info is enabled, `false` otherwise.



#### .reduceDebugInfo(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable reduced debug info or not |

##### Returns: [OptionsHelper$ChatOptionsHelper](#)

self for chaining.




