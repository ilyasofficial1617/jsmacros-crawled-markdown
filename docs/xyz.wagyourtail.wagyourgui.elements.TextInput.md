

xyz.wagyourtail.wagyourgui.elements.TextInput
---------------------------------------------

#### extends [Button](1.9.2/xyz/wagyourtail/wagyourgui/elements/Button.html)

### Constructors

#### new TextInput (x, y, width, height, textRenderer, color, borderColor, highlightColor, textColor, message, onClick, onChange)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| color | int |  |
| borderColor | int |  |
| highlightColor | int |  |
| textColor | int |  |
| message | String |  |
| onClick | Consumer<Button> |  |
| onChange | Consumer<String> |  |



#### Fields

[onChange](#onChange)


[mask](#mask)


[content](#content)


[selStartIndex](1.9.2/)


[selEndIndex](1.9.2/)



#### Methods

[setMessage(message)](#setMessage-String-)


[updateSelStart(startIndex)](#updateSelStart-int-)


[updateSelEnd(endIndex)](#updateSelEnd-int-)


[mouseClicked(mouseX, mouseY, button)](#mouseClicked-double-double-int-)


[mouseDragged(mouseX, mouseY, button, deltaX, deltaY)](#mouseDragged-double-double-int-double-double-)


[swapStartEnd()](#swapStartEnd-)


[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[charTyped(chr, keyCode)](#charTyped-char-int-)


[clicked(mouseX, mouseY)](#clicked-double-double-)


[setSelected(sel)](#setSelected-boolean-)



### Fields

#### .onChange


##### Type: [Consumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Consumer.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .mask


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .content


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .selStartIndex


##### Type: int



#### .selEndIndex


##### Type: int



### Methods

#### .setMessage(message)

| Parameter | Type | Description |
|---|---|---|
| message | String |  |

##### Returns: void



#### .updateSelStart(startIndex)

| Parameter | Type | Description |
|---|---|---|
| startIndex | int |  |

##### Returns: void



#### .updateSelEnd(endIndex)

| Parameter | Type | Description |
|---|---|---|
| endIndex | int |  |

##### Returns: void



#### .mouseClicked(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: boolean



#### .mouseDragged(mouseX, mouseY, button, deltaX, deltaY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |
| deltaX | double |  |
| deltaY | double |  |

##### Returns: boolean



#### .swapStartEnd()


##### Returns: void



#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean



#### .charTyped(chr, keyCode)

| Parameter | Type | Description |
|---|---|---|
| chr | char |  |
| keyCode | int |  |

##### Returns: boolean



#### .clicked(mouseX, mouseY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |

##### Returns: boolean



#### .setSelected(sel)

| Parameter | Type | Description |
|---|---|---|
| sel | boolean |  |

##### Returns: void




