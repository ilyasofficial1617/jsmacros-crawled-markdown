

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Text
------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Text](#)>

1.0.5

### Constructors

#### new Text (text, x, y, color, zIndex, shadow, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | float |  |


#### new Text (text, x, y, color, zIndex, shadow, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | float |  |



#### Fields

[parent](#parent)


[text](#text)


[scale](1.9.2/)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[x](1.9.2/)


[y](1.9.2/)


[color](1.9.2/)


[width](1.9.2/)


[shadow](1.9.2/)


[zIndex](1.9.2/)



#### Methods

[setX(x)](#setX-int-)


[getX()](#getX-)


[setY(y)](#setY-int-)


[getY()](#getY-)


[setPos(x, y)](#setPos-int-int-)


[setText(text)](#setText-String-)


[setText(text)](#setText-TextHelper-)


[getText()](#getText-)


[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[setShadow(shadow)](#setShadow-boolean-)


[hasShadow()](#hasShadow-)


[setScale(scale)](#setScale-double-)


[getScale()](#getScale-)


[setRotation(rotation)](#setRotation-double-)


[getRotation()](#getRotation-)


[setRotateCenter(rotateCenter)](#setRotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[setColor(color)](#setColor-int-)


[getColor()](#getColor-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[render3D(drawContext, mouseX, mouseY, delta)](#render3D-DrawContext-int-int-float-)


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



#### .text


##### Type: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .scale


##### Type: double



#### .rotation


##### Type: float



#### .rotateCenter


##### Type: boolean



#### .x


##### Type: int



#### .y


##### Type: int



#### .color


##### Type: int



#### .width


##### Type: int



#### .shadow


##### Type: boolean



#### .zIndex


##### Type: int



### Methods

#### .setX(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the new x position for this text element |

##### Returns: [Text](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of this element.



#### .setY(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the new y position for this text element |

##### Returns: [Text](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of this element.



#### .setPos(x, y)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Text](#)



#### .setText(text)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| text | String |  |

##### Returns: [Text](#)



#### .setText(text)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |

##### Returns: [Text](#)



#### .getText()

1.2.7


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)



#### .getWidth()

1.0.5


##### Returns: int



#### .getHeight()

1.8.4


##### Returns: int

the height of this text.



#### .setShadow(shadow)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| shadow | boolean | whether the text should be rendered with a shadow |

##### Returns: [Text](#)

self for chaining.



#### .hasShadow()

1.8.4


##### Returns: boolean

`true` if this text element is rendered with a shadow, `false`
otherwise.



#### .setScale(scale)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| scale | double |  |

##### Returns: [Text](#)



#### .getScale()

1.8.4


##### Returns: double

the scale of this text.



#### .setRotation(rotation)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| rotation | double |  |

##### Returns: [Text](#)



#### .getRotation()

1.8.4


##### Returns: float

the rotation of this text.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this text should be rotated around its center |

##### Returns: [Text](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this text should be rotated around its center, `false`
otherwise.



#### .setColor(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the new color for this text element |

##### Returns: [Text](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of this text.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the new z-index for this text element |

##### Returns: [Text](#)

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



#### .render3D(drawContext, mouseX, mouseY, delta)

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

##### Returns: [Text](#)



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

##### Returns: [Text](#)




