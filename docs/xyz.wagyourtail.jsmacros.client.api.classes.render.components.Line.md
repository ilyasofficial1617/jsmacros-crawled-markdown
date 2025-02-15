

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Line
------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Line](#)>

1.8.4

### Constructors

#### new Line (x1, y1, x2, y2, color, rotation, width, zIndex)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| rotation | float |  |
| width | float |  |
| zIndex | int |  |



#### Fields

[parent](#parent)


[x1](1.9.2/)


[y1](1.9.2/)


[x2](1.9.2/)


[y2](1.9.2/)


[color](1.9.2/)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[width](1.9.2/)


[zIndex](1.9.2/)



#### Methods

[setX1(x1)](#setX1-int-)


[getX1()](#getX1-)


[setY1(y1)](#setY1-int-)


[getY1()](#getY1-)


[setPos1(x1, y1)](#setPos1-int-int-)


[setX2(x2)](#setX2-int-)


[getX2()](#getX2-)


[setY2(y2)](#setY2-int-)


[getY2()](#getY2-)


[setPos2(x2, y2)](#setPos2-int-int-)


[setPos(x1, y1, x2, y2)](#setPos-int-int-int-int-)


[setColor(color)](#setColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


[getColor()](#getColor-)


[setAlpha(alpha)](#setAlpha-int-)


[getAlpha()](#getAlpha-)


[setRotation(rotation)](#setRotation-double-)


[getRotation()](#getRotation-)


[setRotateCenter(rotateCenter)](#setRotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[setWidth(width)](#setWidth-double-)


[getWidth()](#getWidth-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[setParent(parent)](#setParent-IDraw2D-)


[moveTo(x, y)](#moveTo-int-int-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)



### Fields

#### .parent


##### Type: [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)< ? >



#### .x1


##### Type: int



#### .y1


##### Type: int



#### .x2


##### Type: int



#### .y2


##### Type: int



#### .color


##### Type: int



#### .rotation


##### Type: float



#### .rotateCenter


##### Type: boolean



#### .width


##### Type: float



#### .zIndex


##### Type: int



### Methods

#### .setX1(x1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start of the line |

##### Returns: [Line](#)

self for chaining.



#### .getX1()

1.8.4


##### Returns: int

the x position of the start of the line.



#### .setY1(y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y1 | int | the y position of the start of the line |

##### Returns: [Line](#)

self for chaining.



#### .getY1()

1.8.4


##### Returns: int

the y position of the start of the line.



#### .setPos1(x1, y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start of the line |
| y1 | int | the y position of the start of the line |

##### Returns: [Line](#)

self for chaining.



#### .setX2(x2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the x position of the end of the line |

##### Returns: [Line](#)

self for chaining.



#### .getX2()

1.8.4


##### Returns: int

the x position of the end of the line.



#### .setY2(y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y2 | int | the y position of the end of the line |

##### Returns: [Line](#)

self for chaining.



#### .getY2()

1.8.4


##### Returns: int

the y position of the end of the line.



#### .setPos2(x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the x position of the end of the line |
| y2 | int | the y position of the end of the line |

##### Returns: [Line](#)

self for chaining.



#### .setPos(x1, y1, x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start of the line |
| y1 | int | the y position of the start of the line |
| x2 | int | the x position of the end of the line |
| y2 | int | the y position of the end of the line |

##### Returns: [Line](#)

self for chaining.



#### .setColor(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |

##### Returns: [Line](#)

self for chaining.



#### .setColor(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |
| alpha | int | the alpha of the line |

##### Returns: [Line](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the line.



#### .setAlpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value of the line's color |

##### Returns: [Line](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the line's color.



#### .setRotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the line |

##### Returns: [Line](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the line.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this line should be rotated around its center |

##### Returns: [Line](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this line should be rotated around its center, `false`
otherwise.



#### .setWidth(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | double | the width of the line |

##### Returns: [Line](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: float

the width of the line.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the line |

##### Returns: [Line](#)

self for chaining.



#### .getZIndex()


##### Returns: int



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .setParent(parent)

| Parameter | Type | Description |
|---|---|---|
| parent | IDraw2D<?> |  |

##### Returns: [Line](#)



#### .moveTo(x, y)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Line](#)



#### .getScaledWidth()


##### Returns: int



#### .getParentWidth()


##### Returns: int



#### .getScaledHeight()


##### Returns: int



#### .getParentHeight()


##### Returns: int



#### .getScaledLeft()


##### Returns: int



#### .getScaledTop()


##### Returns: int




