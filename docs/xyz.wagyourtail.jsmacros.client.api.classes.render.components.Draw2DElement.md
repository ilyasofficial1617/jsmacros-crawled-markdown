

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Draw2DElement
---------------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Draw2DElement](#)>

1.8.4

### Constructors

#### new Draw2DElement (draw2D, x, y, width, height, zIndex, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D |  |
| x | int |  |
| y | int |  |
| width | IntSupplier |  |
| height | IntSupplier |  |
| zIndex | int |  |
| scale | float |  |
| rotation | float |  |



#### Fields

[draw2D](#draw2D)
F


[parent](#parent)


[x](1.9.2/)


[y](1.9.2/)


[width](#width)


[height](#height)


[scale](1.9.2/)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[zIndex](1.9.2/)



#### Methods

[getDraw2D()](#getDraw2D-)


[setX(x)](#setX-int-)


[getX()](#getX-)


[setY(y)](#setY-int-)


[getY()](#getY-)


[setPos(x, y)](#setPos-int-int-)


[setWidth(width)](#setWidth-int-)


[getWidth()](#getWidth-)


[setHeight(height)](#setHeight-int-)


[getHeight()](#getHeight-)


[setSize(width, height)](#setSize-int-int-)


[setScale(scale)](#setScale-double-)


[getScale()](#getScale-)


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

#### .draw2D

Final

##### Type: [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html)



#### .parent


##### Type: [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)< ? >



#### .x


##### Type: int



#### .y


##### Type: int



#### .width


##### Type: [IntSupplier](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/IntSupplier.html)



#### .height


##### Type: [IntSupplier](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/IntSupplier.html)



#### .scale


##### Type: float



#### .rotation


##### Type: float



#### .rotateCenter


##### Type: boolean



#### .zIndex


##### Type: int



### Methods

#### .getDraw2D()

1.8.4


##### Returns: [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html)

the internal draw2D this draw2D element is wrapping.



#### .setX(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of this draw2D.



#### .setY(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the y position |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of this draw2D.



#### .setPos(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position |
| y | int | the y position |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .setWidth(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of this draw2D.



#### .setHeight(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | the height |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: int

the height of this draw2D.



#### .setSize(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width |
| height | int | the height |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .setScale(scale)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| scale | double | the scale |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getScale()

1.8.4


##### Returns: float

the scale of this draw2D.



#### .setRotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation of this draw2D.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether this draw2D should be rotated around its center |

##### Returns: [Draw2DElement](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this draw2D should be rotated around its center, `false`
otherwise.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of this draw2D |

##### Returns: [Draw2DElement](#)

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

##### Returns: [Draw2DElement](#)



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

##### Returns: [Draw2DElement](#)




