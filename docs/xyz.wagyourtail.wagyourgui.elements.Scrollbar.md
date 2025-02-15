

xyz.wagyourtail.wagyourgui.elements.Scrollbar
---------------------------------------------

#### extends [ClickableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ClickableWidget)

### Constructors

#### new Scrollbar (x, y, width, height, color, borderColor, highlightColor, scrollPages, onChange)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| color | int |  |
| borderColor | int |  |
| highlightColor | int |  |
| scrollPages | double |  |
| onChange | Consumer<Double> |  |



#### Methods

[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[setScrollPages(scrollPages)](#setScrollPages-double-)


[scrollToPercent(percent)](#scrollToPercent-double-)


[onClick(mouseX, mouseY)](#onClick-double-double-)


[onChange()](#onChange-)


[mouseDragged(mouseX, mouseY, button, deltaX, deltaY)](#mouseDragged-double-double-int-double-double-)


[renderWidget(drawContext, mouseX, mouseY, delta)](#renderWidget-DrawContext-int-int-float-)



### Methods

#### .setPos(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: [Scrollbar](#)



#### .setScrollPages(scrollPages)

| Parameter | Type | Description |
|---|---|---|
| scrollPages | double |  |

##### Returns: void



#### .scrollToPercent(percent)

| Parameter | Type | Description |
|---|---|---|
| percent | double |  |

##### Returns: void



#### .onClick(mouseX, mouseY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |

##### Returns: void



#### .onChange()


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



#### .renderWidget(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




