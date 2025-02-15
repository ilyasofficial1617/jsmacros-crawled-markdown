

xyz.wagyourtail.jsmacros.client.api.helpers.screen.TextFieldWidgetHelper
------------------------------------------------------------------------

#### extends [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)<[TextFieldWidgetHelper](#), [TextFieldWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TextFieldWidget)>

1.0.5

### Constructors

#### new TextFieldWidgetHelper (t)

| Parameter | Type | Description |
|---|---|---|
| t | TextFieldWidget |  |


#### new TextFieldWidgetHelper (t, zIndex)

| Parameter | Type | Description |
|---|---|---|
| t | TextFieldWidget |  |
| zIndex | int |  |



#### Methods

[getText()](#getText-)


[setText(text)](#setText-String-)


[setText(text, await)](#setText-String-boolean-)


[setEditableColor(color)](#setEditableColor-int-)


[setEditable(edit)](#setEditable-boolean-)


[isEditable()](#isEditable-)


[setUneditableColor(color)](#setUneditableColor-int-)


[getSelectedText()](#getSelectedText-)


[setSuggestion(suggestion)](#setSuggestion-String-)


[getMaxLength()](#getMaxLength-)


[setMaxLength(length)](#setMaxLength-int-)


[setSelection(start, end)](#setSelection-int-int-)


[setTextPredicate(predicate)](#setTextPredicate-MethodWrapper-)


[resetTextPredicate()](#resetTextPredicate-)


[setCursorPosition(position)](#setCursorPosition-int-)


[setCursorPosition(position, shift)](#setCursorPosition-int-boolean-)


[setCursorToStart()](#setCursorToStart-)


[setCursorToStart(shift)](#setCursorToStart-boolean-)


[setCursorToEnd()](#setCursorToEnd-)


[setCursorToEnd(shift)](#setCursorToEnd-boolean-)


[toString()](#toString-)



### Methods

#### .getText()

1.0.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the currently entered [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html).



#### .setText(text)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| text | String |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setText(text, await)

1.3.1

set the currently entered [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html).

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| await | boolean |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setEditableColor(color)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setEditable(edit)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| edit | boolean |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .isEditable()

1.8.4


##### Returns: boolean

`true` if the text field is editable, `false` otherwise.



#### .setUneditableColor(color)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .getSelectedText()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the selected text.



#### .setSuggestion(suggestion)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestion | String | the suggestion to set |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .getMaxLength()

1.8.4


##### Returns: int

the maximum length of this text field.



#### .setMaxLength(length)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| length | int | the new maximum length |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setSelection(start, end)

| Parameter | Type | Description |
|---|---|---|
| start | int |  |
| end | int |  |

##### Returns: [TextFieldWidgetHelper](#)



#### .setTextPredicate(predicate)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| predicate | MethodWrapper<String, ?, ?, ?> | the text filter |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .resetTextPredicate()

1.8.4


##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setCursorPosition(position)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| position | int | the cursor position |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setCursorPosition(position, shift)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| shift | boolean |  |

##### Returns: [TextFieldWidgetHelper](#)

the cursor position.



#### .setCursorToStart()

1.8.4


##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setCursorToStart(shift)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| shift | boolean |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setCursorToEnd()

1.8.4


##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .setCursorToEnd(shift)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| shift | boolean |  |

##### Returns: [TextFieldWidgetHelper](#)

self for chaining.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




