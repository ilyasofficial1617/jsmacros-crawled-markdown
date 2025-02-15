

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Rect
------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Rect](#)>

1.0.5

### Constructors

#### new Rect (x1, y1, x2, y2, color, rotation, zIndex)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| rotation | float |  |
| zIndex | int |  |


#### new Rect (x1, y1, x2, y2, color, alpha, rotation, zIndex)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| alpha | int |  |
| rotation | float |  |
| zIndex | int |  |



#### Fields

[parent](#parent)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[x1](1.9.2/)


[y1](1.9.2/)


[x2](1.9.2/)


[y2](1.9.2/)


[color](1.9.2/)


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


[setWidth(width)](#setWidth-int-)


[getWidth()](#getWidth-)


[setHeight(height)](#setHeight-int-)


[getHeight()](#getHeight-)


[setSize(width, height)](#setSize-int-int-)


[setColor(color)](#setColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


[setAlpha(alpha)](#setAlpha-int-)


[getColor()](#getColor-)


[getAlpha()](#getAlpha-)


[setRotation(rotation)](#setRotation-double-)


[getRotation()](#getRotation-)


[setRotateCenter(rotateCenter)](#setRotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[setParent(parent)](#setParent-IDraw2D-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)


[moveTo(x, y)](#moveTo-int-int-)



### Fields

#### .parent


##### Type: [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)< ? >



#### .rotation


##### Type: float



#### .rotateCenter


##### Type: boolean



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



#### .zIndex


##### Type: int



### Methods

#### .setX1(x1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getX1()

1.8.4


##### Returns: int

the first x position of this rectangle.



#### .setY1(y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y1 | int | the first y position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getY1()

1.8.4


##### Returns: int

the first y position of this rectangle.



#### .setPos1(x1, y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of this rectangle |
| y1 | int | the first y position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .setX2(x2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the second x position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getX2()

1.8.4


##### Returns: int

the second x position of this rectangle.



#### .setY2(y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y2 | int | the second y position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getY2()

1.8.4


##### Returns: int

the second y position of the rectangle.



#### .setPos2(x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the second x position of this rectangle |
| y2 | int | the second y position of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .setPos(x1, y1, x2, y2)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |

##### Returns: [Rect](#)



#### .setWidth(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the new width of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of this rectangle.



#### .setHeight(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | the new height of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: int

the height of this rectangle.



#### .setSize(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the new width of this rectangle |
| height | int | the new height of this rectangle |

##### Returns: [Rect](#)

self for chaining.



#### .setColor(color)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [Rect](#)



#### .setColor(color, alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| color | int |  |
| alpha | int |  |

##### Returns: [Rect](#)



#### .setAlpha(alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| alpha | int |  |

##### Returns: [Rect](#)



#### .getColor()

1.8.4


##### Returns: int

the color value of this rectangle.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of this rectangle.



#### .setRotation(rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| rotation | double |  |

##### Returns: [Rect](#)



#### .getRotation()

1.8.4


##### Returns: float

the rotation of this rectangle.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this rectangle should be rotated around its center |

##### Returns: [Rect](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this rectangle should be rotated around its center, `false`
otherwise.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the new z-index for this rectangle |

##### Returns: [Rect](#)

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

##### Returns: [Rect](#)



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



#### .moveTo(x, y)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Rect](#)




