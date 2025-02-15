
[TextInput](1.9.2/xyz/wagyourtail/wagyourgui/elements/TextInput.html) [AnnotatedCheckBox](1.9.2/xyz/wagyourtail/wagyourgui/elements/AnnotatedCheckBox.html)

xyz.wagyourtail.wagyourgui.elements.Button
------------------------------------------

#### extends [PressableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/PressableWidget)

### Constructors

#### new Button (x, y, width, height, textRenderer, color, borderColor, highlightColor, textColor, message, onPress)

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
| message | Text |  |
| onPress | Consumer<Button> |  |



#### Fields

[horizCenter](1.9.2/)


[onPress](#onPress)


[hovering](1.9.2/)


[forceHover](1.9.2/)



#### Methods

[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[cantRenderAllText()](#cantRenderAllText-)


[setMessage(message)](#setMessage-Text-)


[setColor(color)](#setColor-int-)


[setHighlightColor(color)](#setHighlightColor-int-)


[renderWidget(drawContext, mouseX, mouseY, delta)](#renderWidget-DrawContext-int-int-float-)


[onClick(mouseX, mouseY)](#onClick-double-double-)


[onRelease(mouseX, mouseY)](#onRelease-double-double-)


[onPress()](#onPress-)



### Fields

#### .horizCenter


##### Type: boolean



#### .onPress


##### Type: [Consumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Consumer.html)<[Button](#)>



#### .hovering


##### Type: boolean



#### .forceHover


##### Type: boolean



### Methods

#### .setPos(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: [Button](#)



#### .cantRenderAllText()


##### Returns: boolean



#### .setMessage(message)

| Parameter | Type | Description |
|---|---|---|
| message | Text |  |

##### Returns: void



#### .setColor(color)

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: void



#### .setHighlightColor(color)

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: void



#### .renderWidget(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .onClick(mouseX, mouseY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |

##### Returns: void



#### .onRelease(mouseX, mouseY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |

##### Returns: void



#### .onPress()


##### Returns: void




