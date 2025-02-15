

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Image$Builder
---------------------------------------------------------------------------

Static
Final
#### extends [RenderElementBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElementBuilder.html)<[Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)> implements [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Image$Builder](#)>

1.8.4

### Constructors

#### new Image$Builder (draw2D)

| Parameter | Type | Description |
|---|---|---|
| draw2D | IDraw2D<?> |  |



#### Methods

[fromCustomImage(customImage)](#fromCustomImage-CustomImage-)


[identifier(identifier)](#identifier-String-)


[getIdentifier()](#getIdentifier-)


[x(x)](#x-int-)


[getX()](#getX-)


[y(y)](#y-int-)


[getY()](#getY-)


[pos(x, y)](#pos-int-int-)


[width(width)](#width-int-)


[getWidth()](#getWidth-)


[height(height)](#height-int-)


[getHeight()](#getHeight-)


[size(width, height)](#size-int-int-)


[imageX(imageX)](#imageX-int-)


[getImageX()](#getImageX-)


[imageY(imageY)](#imageY-int-)


[getImageY()](#getImageY-)


[imagePos(imageX, imageY)](#imagePos-int-int-)


[regionWidth(regionWidth)](#regionWidth-int-)


[getRegionWidth()](#getRegionWidth-)


[regionHeight(regionHeight)](#regionHeight-int-)


[getRegionHeight()](#getRegionHeight-)


[regionSize(regionWidth, regionHeight)](#regionSize-int-int-)


[regions(x, y, width, height)](#regions-int-int-int-int-)


[regions(x, y, width, height, textureWidth, textureHeight)](#regions-int-int-int-int-int-int-)


[textureWidth(textureWidth)](#textureWidth-int-)


[getTextureWidth()](#getTextureWidth-)


[textureHeight(textureHeight)](#textureHeight-int-)


[getTextureHeight()](#getTextureHeight-)


[textureSize(textureWidth, textureHeight)](#textureSize-int-int-)


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

#### .fromCustomImage(customImage)

1.8.4

Will automatically set all attributes to the default values of the custom image.
Values set before the call of this method will be overwritten.

| Parameter | Type | Description |
|---|---|---|
| customImage | CustomImage | the custom image to use |

##### Returns: [Image$Builder](#)

self for chaining.



#### .identifier(identifier)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifier | String | the identifier of the image to use |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getIdentifier()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of the used image or `null` if no image is used.



#### .x(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of the image.



#### .y(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the y position of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of the image.



#### .pos(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the image |
| y | int | the y position of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .width(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: int

the width of the image.



#### .height(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | the height of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: int

the height of the image.



#### .size(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the image |
| height | int | the height of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .imageX(imageX)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| imageX | int | the x position in the image texture to start drawing from |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getImageX()

1.8.4


##### Returns: int

the x position in the image texture to start drawing from.



#### .imageY(imageY)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| imageY | int | the y position in the image texture to start drawing from |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getImageY()

1.8.4


##### Returns: int

the y position in the image texture to start drawing from.



#### .imagePos(imageX, imageY)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| imageX | int | the x position in the image texture to start drawing from |
| imageY | int | the y position in the image texture to start drawing from |

##### Returns: [Image$Builder](#)

self for chaining.



#### .regionWidth(regionWidth)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| regionWidth | int | the width of the region to draw |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getRegionWidth()

1.8.4


##### Returns: int

the width of the region to draw.



#### .regionHeight(regionHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| regionHeight | int | the height of the region to draw |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getRegionHeight()

1.8.4


##### Returns: int

the height of the region to draw.



#### .regionSize(regionWidth, regionHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| regionWidth | int | the width of the region to draw |
| regionHeight | int | the height of the region to draw |

##### Returns: [Image$Builder](#)

self for chaining.



#### .regions(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position in the image texture to start drawing from |
| y | int | the y position in the image texture to start drawing from |
| width | int | the width of the region to draw |
| height | int | the height of the region to draw |

##### Returns: [Image$Builder](#)



#### .regions(x, y, width, height, textureWidth, textureHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position in the image texture to start drawing from |
| y | int | the y position in the image texture to start drawing from |
| width | int | the width of the region to draw |
| height | int | the height of the region to draw |
| textureWidth | int | the width of the used texture |
| textureHeight | int | the height of the used texture |

##### Returns: [Image$Builder](#)



#### .textureWidth(textureWidth)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| textureWidth | int | the width of the used texture |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getTextureWidth()

1.8.4


##### Returns: int

the width of the used texture.



#### .textureHeight(textureHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| textureHeight | int | the height of the used texture |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getTextureHeight()

1.8.4


##### Returns: int

the height of the used texture.



#### .textureSize(textureWidth, textureHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| textureWidth | int | the width of the used texture |
| textureHeight | int | the height of the used texture |

##### Returns: [Image$Builder](#)

self for chaining.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [Image$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha component of the color |

##### Returns: [Image$Builder](#)

self for chaining.



#### .color(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the image |
| alpha | int | the alpha value of the color |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the image.



#### .alpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value of the color |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the color.



#### .rotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the image in degrees |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the image in degrees.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether the image should be rotated around its center |

##### Returns: [Image$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this image should be rotated around its center, `false`
otherwise.



#### .zIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the image |

##### Returns: [Image$Builder](#)

self for chaining.



#### .getZIndex()

1.8.4


##### Returns: int

the z-index of the image.



#### .createElement()


##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



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

##### Returns: [Image$Builder](#)




