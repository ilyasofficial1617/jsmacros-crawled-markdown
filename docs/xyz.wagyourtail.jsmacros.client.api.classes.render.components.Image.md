

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Image
-------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Image](#)>

1.2.3

### Constructors

#### new Image (x, y, width, height, zIndex, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| color | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |
| rotation | float |  |


#### new Image (x, y, width, height, zIndex, alpha, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| alpha | int |  |
| color | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |
| rotation | float |  |



#### Fields

[parent](#parent)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[x](1.9.2/)


[y](1.9.2/)


[width](1.9.2/)


[height](1.9.2/)


[imageX](1.9.2/)


[imageY](1.9.2/)


[regionWidth](1.9.2/)


[regionHeight](1.9.2/)


[textureWidth](1.9.2/)


[textureHeight](1.9.2/)


[color](1.9.2/)


[zIndex](1.9.2/)



#### Methods

[setImage(id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)](#setImage-String-int-int-int-int-int-int-)


[getImage()](#getImage-)


[setX(x)](#setX-int-)


[getX()](#getX-)


[setY(y)](#setY-int-)


[getY()](#getY-)


[setPos(x, y)](#setPos-int-int-)


[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[setWidth(width)](#setWidth-int-)


[getWidth()](#getWidth-)


[setHeight(height)](#setHeight-int-)


[getHeight()](#getHeight-)


[setSize(width, height)](#setSize-int-int-)


[setColor(color)](#setColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


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



#### .x


##### Type: int



#### .y


##### Type: int



#### .width


##### Type: int



#### .height


##### Type: int



#### .imageX


##### Type: int



#### .imageY


##### Type: int



#### .regionWidth


##### Type: int



#### .regionHeight


##### Type: int



#### .textureWidth


##### Type: int



#### .textureHeight


##### Type: int



#### .color


##### Type: int



#### .zIndex


##### Type: int



### Methods

#### .setImage(id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |

##### Returns: [Image](#)

self for chaining.



#### .getImage()

1.2.3


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .setX(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the new x position of this image |

##### Returns: [Image](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of this image.



#### .setY(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the new y position of this image |

##### Returns: [Image](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of this image.



#### .setPos(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the new x position of this image |
| y | int | the new y position of this image |

##### Returns: [Image](#)

self for chaining.



#### .setPos(x, y, width, height)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: [Image](#)



#### .setWidth(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the new width of this image |

##### Returns: [Image](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of this image.



#### .setHeight(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | the new height of this image |

##### Returns: [Image](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: int

the height of this image.



#### .setSize(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the new width of this image |
| height | int | the new height of this image |

##### Returns: [Image](#)

self for chaining.



#### .setColor(color)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [Image](#)



#### .setColor(color, alpha)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| color | int |  |
| alpha | int |  |

##### Returns: [Image](#)



#### .getColor()

1.8.4


##### Returns: int

the color of this image.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of this image.



#### .setRotation(rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| rotation | double |  |

##### Returns: [Image](#)



#### .getRotation()

1.8.4


##### Returns: float

the rotation of this image.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether the image should be rotated around its center |

##### Returns: [Image](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this image should be rotated around its center, `false`
otherwise.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the new z-index of this image |

##### Returns: [Image](#)

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

##### Returns: [Image](#)



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

##### Returns: [Image](#)




