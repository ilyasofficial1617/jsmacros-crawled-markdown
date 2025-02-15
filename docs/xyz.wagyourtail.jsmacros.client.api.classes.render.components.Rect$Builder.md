

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Rect$Builder
--------------------------------------------------------------------------

Static
Final
#### extends [RenderElementBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElementBuilder.html)<[Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)> implements [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Rect$Builder](#)>

1.8.4

### Constructors

#### new Rect$Builder (draw2D)

| Parameter | Type | Description |
|---|---|---|
| draw2D | IDraw2D<?> |  |



#### Methods

[x1(x1)](#x1-int-)


[getX1()](#getX1-)


[y1(y1)](#y1-int-)


[getY1()](#getY1-)


[pos1(x1, y1)](#pos1-int-int-)


[x2(x2)](#x2-int-)


[getX2()](#getX2-)


[y2(y2)](#y2-int-)


[getY2()](#getY2-)


[pos2(x2, y2)](#pos2-int-int-)


[pos(x1, y1, x2, y2)](#pos-int-int-int-int-)


[width(width)](#width-int-)


[getWidth()](#getWidth-)


[height(height)](#height-int-)


[getHeight()](#getHeight-)


[size(width, height)](#size-int-int-)


[color(color)](#color-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[color(color, alpha)](#color-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[rotation(rotation)](#rotation-double-)


[getRotation()](#getRotation-)


[rotateCenter(rotateCenter)](#rotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[zIndex(zIndex)](#zIndex-int-)


[getZIndex()](#getZIndex-)


[createElement()](#createElement-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)


[moveTo(x, y)](#moveTo-int-int-)



### Methods

#### .x1(x1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getX1()

1.8.4


##### Returns: int

the first x position of the rectangle.



#### .y1(y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y1 | int | the first y position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getY1()

1.8.4


##### Returns: int

the first y position of the rectangle.



#### .pos1(x1, y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of the rectangle |
| y1 | int | the first y position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .x2(x2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the second x position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getX2()

1.8.4


##### Returns: int

the second x position of the rectangle.



#### .y2(y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y2 | int | the second y position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getY2()

1.8.4


##### Returns: int

the second y position of the rectangle.



#### .pos2(x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the second x position of the rectangle |
| y2 | int | the second y position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .pos(x1, y1, x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of the rectangle |
| y1 | int | the first y position of the rectangle |
| x2 | int | the second x position of the rectangle |
| y2 | int | the second y position of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .width(width)

1.8.4

The width will just set the x2 position to `x1 + width`.

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of the rectangle.



#### .height(height)

1.8.4

The width will just set the y2 position to `y1 + height`.

| Parameter | Type | Description |
|---|---|---|
| height | int | the height of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: int

the height of the rectangle.



#### .size(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha value of the color |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .color(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the rectangle |
| alpha | int | the alpha value of the color |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the rectangle.



#### .alpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value of the color |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the color.



#### .rotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the rectangle in degrees |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the rectangle in degrees.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this rectangle should be rotated around its center |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this rectangle should be rotated around its center,
`false` otherwise.



#### .zIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the rectangle |

##### Returns: [Rect$Builder](#)

self for chaining.



#### .getZIndex()

1.8.4


##### Returns: int

the z-index of the rectangle.



#### .createElement()


##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



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

##### Returns: [Rect$Builder](#)




