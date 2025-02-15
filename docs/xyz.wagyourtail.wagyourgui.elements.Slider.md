

xyz.wagyourtail.wagyourgui.elements.Slider
------------------------------------------

#### extends [ClickableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ClickableWidget)

1.8.4

### Constructors

#### new Slider (x, y, width, height, text, value, action, steps)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | Text |  |
| value | double |  |
| action | Consumer<Slider> |  |
| steps | int |  |


#### new Slider (x, y, width, height, text, value, action)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | Text |  |
| value | double |  |
| action | Consumer<Slider> |  |



#### Methods

[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[roundValue(value)](#roundValue-double-)


[getValue()](#getValue-)


[setValue(mouseX)](#setValue-double-)


[getSteps()](#getSteps-)


[setSteps(steps)](#setSteps-int-)


[onClick(mouseX, mouseY)](#onClick-double-double-)


[onRelease(mouseX, mouseY)](#onRelease-double-double-)


[setMessage(message)](#setMessage-String-)


[setMessage(message)](#setMessage-Text-)



### Methods

#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean



#### .roundValue(value)

| Parameter | Type | Description |
|---|---|---|
| value | double |  |

##### Returns: double



#### .getValue()


##### Returns: double



#### .setValue(mouseX)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |

##### Returns: void



#### .getSteps()


##### Returns: int



#### .setSteps(steps)

| Parameter | Type | Description |
|---|---|---|
| steps | int |  |

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



#### .setMessage(message)

| Parameter | Type | Description |
|---|---|---|
| message | String |  |

##### Returns: void



#### .setMessage(message)

| Parameter | Type | Description |
|---|---|---|
| message | Text |  |

##### Returns: void




