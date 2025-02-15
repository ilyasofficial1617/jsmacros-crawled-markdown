

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Text$Builder
--------------------------------------------------------------------------

Static
#### extends [RenderElementBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElementBuilder.html)<[Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)> implements [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Text$Builder](#)>

1.8.4

### Constructors

#### new Text$Builder (draw2D)

| Parameter | Type | Description |
|---|---|---|
| draw2D | IDraw2D<?> |  |



#### Methods

[text(text)](#text-TextHelper-)


[text(text)](#text-TextBuilder-)


[text(text)](#text-String-)


[getText()](#getText-)


[x(x)](#x-int-)


[getX()](#getX-)


[y(y)](#y-int-)


[getY()](#getY-)


[pos(x, y)](#pos-int-int-)


[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[color(color)](#color-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[scale(scale)](#scale-double-)


[getScale()](#getScale-)


[rotation(rotation)](#rotation-double-)


[getRotation()](#getRotation-)


[rotateCenter(rotateCenter)](#rotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[shadow(shadow)](#shadow-boolean-)


[hasShadow()](#hasShadow-)


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

#### .text(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper | the content of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .text(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | TextBuilder | the content of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .text(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | String | the content of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getText()

1.8.4


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the content of the text element.



#### .x(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of the text element.



#### .y(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the y position of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of the text element.



#### .pos(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the text element |
| y | int | the y position of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of the string.



#### .getHeight()

1.8.4


##### Returns: int

the height of the string.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [Text$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha component of the color |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the text element.



#### .scale(scale)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| scale | double | the scale of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getScale()

1.8.4


##### Returns: double

the scale of the text element.



#### .rotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the text element in degrees |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the text element in degrees.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this text should be rotated around its center |

##### Returns: [Text$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this text should be rotated around its center, `false`
otherwise.



#### .shadow(shadow)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| shadow | boolean | whether the text should have a shadow or not |

##### Returns: [Text$Builder](#)

self for chaining.



#### .hasShadow()

1.8.4


##### Returns: boolean

`true` if the text element has a shadow, `false` otherwise.



#### .zIndex(zIndex)

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the text element |

##### Returns: [Text$Builder](#)

self for chaining.



#### .getZIndex()

1.8.4


##### Returns: int

the z-index of the text element.



#### .createElement()


##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



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

##### Returns: [Text$Builder](#)




