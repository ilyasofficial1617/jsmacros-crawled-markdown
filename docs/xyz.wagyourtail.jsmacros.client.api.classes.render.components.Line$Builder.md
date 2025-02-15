

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Line$Builder
--------------------------------------------------------------------------

Static
#### extends [RenderElementBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElementBuilder.html)<[Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)> implements [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Line$Builder](#)>

1.8.4

### Constructors

#### new Line$Builder (draw2D)

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


[rotation(rotation)](#rotation-double-)


[getRotation()](#getRotation-)


[rotateCenter(rotateCenter)](#rotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[width(width)](#width-double-)


[getWidth()](#getWidth-)


[color(color)](#color-int-)


[color(color, alpha)](#color-int-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[zIndex(zIndex)](#zIndex-int-)


[getZIndex()](#getZIndex-)


[moveTo(x, y)](#moveTo-int-int-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)



### Methods

#### .x1(x1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the first point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getX1()

1.8.4


##### Returns: int

the x position of the first point.



#### .y1(y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y1 | int | the y position of the first point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getY1()

1.8.4


##### Returns: int

the y position of the first point.



#### .pos1(x1, y1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the first point |
| y1 | int | the y position of the first point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .x2(x2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the x position of the second point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getX2()

1.8.4


##### Returns: int

the x position of the second point.



#### .y2(y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y2 | int | the y position of the second point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getY2()

1.8.4


##### Returns: int

the y position of the second point.



#### .pos2(x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the x position of the second point |
| y2 | int | the y position of the second point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .pos(x1, y1, x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the first point |
| y1 | int | the y position of the first point |
| x2 | int | the x position of the second point |
| y2 | int | the y position of the second point |

##### Returns: [Line$Builder](#)

self for chaining.



#### .rotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the line |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the line.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this line should be rotated around its center |

##### Returns: [Line$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this line should be rotated around its center, `false`
otherwise.



#### .width(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | double | the width of the line |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: float

the width of the line.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |

##### Returns: [Line$Builder](#)

self for chaining.



#### .color(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |
| alpha | int | the alpha component of the color |

##### Returns: [Line$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [Line$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha value of the color |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the line.



#### .alpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value of the color |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the color.



#### .zIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the line |

##### Returns: [Line$Builder](#)

self for chaining.



#### .getZIndex()

1.8.4


##### Returns: int

the z-index of the line.



#### .moveTo(x, y)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Line$Builder](#)



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




