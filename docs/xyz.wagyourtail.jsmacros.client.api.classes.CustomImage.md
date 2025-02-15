

xyz.wagyourtail.jsmacros.client.api.classes.CustomImage
-------------------------------------------------------

#### 

1.8.4

### Constructors

#### new CustomImage (image)

| Parameter | Type | Description |
|---|---|---|
| image | BufferedImage |  |


#### new CustomImage (image, name)

| Parameter | Type | Description |
|---|---|---|
| image | BufferedImage |  |
| name | String |  |



#### Fields

[IMAGES](#IMAGES)
S
F



#### Methods

[getName()](#getName-)


[loadImage(path)](#loadImage-String-)


[loadImage(path, x, y, width, height)](#loadImage-String-int-int-int-int-)


[update()](#update-)


[saveImage(path, fileName)](#saveImage-String-String-)


[getIdentifier()](#getIdentifier-)


[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[getImage()](#getImage-)


[getPixel(x, y)](#getPixel-int-int-)


[setPixel(x, y, argb)](#setPixel-int-int-int-)


[drawImage(img, x, y, width, height)](#drawImage-Image-int-int-int-int-)


[drawImage(img, x, y, width, height, sourceX, sourceY, sourceWidth, sourceHeight)](#drawImage-Image-int-int-int-int-int-int-int-int-)


[getGraphicsColor()](#getGraphicsColor-)


[setGraphicsColor(color)](#setGraphicsColor-int-)


[translate(x, y)](#translate-int-int-)


[clipRect(x, y, width, height)](#clipRect-int-int-int-int-)


[setClip(x, y, width, height)](#setClip-int-int-int-int-)


[setPaintMode()](#setPaintMode-)


[setXorMode(color)](#setXorMode-int-)


[getClipBounds()](#getClipBounds-)


[copyArea(x, y, width, height, dx, dy)](#copyArea-int-int-int-int-int-int-)


[drawLine(x1, y1, x2, y2)](#drawLine-int-int-int-int-)


[drawRect(x, y, width, height)](#drawRect-int-int-int-int-)


[fillRect(x, y, width, height)](#fillRect-int-int-int-int-)


[clearRect(x, y, width, height)](#clearRect-int-int-int-int-)


[clearRect(x, y, width, height, color)](#clearRect-int-int-int-int-int-)


[drawRoundRect(x, y, width, height, arcWidth, arcHeight)](#drawRoundRect-int-int-int-int-int-int-)


[fillRoundRect(x, y, width, height, arcWidth, arcHeight)](#fillRoundRect-int-int-int-int-int-int-)


[draw3DRect(x, y, width, height, raised)](#draw3DRect-int-int-int-int-boolean-)


[fill3DRect(x, y, width, height, raised)](#fill3DRect-int-int-int-int-boolean-)


[drawOval(x, y, width, height)](#drawOval-int-int-int-int-)


[fillOval(x, y, width, height)](#fillOval-int-int-int-int-)


[drawArc(x, y, width, height, startAngle, arcAngle)](#drawArc-int-int-int-int-int-int-)


[fillArc(x, y, width, height, startAngle, arcAngle)](#fillArc-int-int-int-int-int-int-)


[drawPolygonLine(pointsX, pointsY)](#drawPolygonLine-int[]-int[]-)


[drawPolygon(pointsX, pointsY)](#drawPolygon-int[]-int[]-)


[fillPolygon(pointsX, pointsY)](#fillPolygon-int[]-int[]-)


[drawString(x, y, text)](#drawString-int-int-String-)


[getStringWidth(toAnalyze)](#getStringWidth-String-)


[createWidget(width, height, name)](#createWidget-int-int-String-)
S


[createWidget(path, name)](#createWidget-String-String-)
S


[nativeARGBFlip(argb)](#nativeARGBFlip-int-)
S



### Fields

#### .IMAGES

Static
Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [CustomImage](#)>



### Methods

#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of this image.



#### .loadImage(path)

1.8.4

The image can be used with the drawImage methods to draw it onto this image.

| Parameter | Type | Description |
|---|---|---|
| path | String | the path to the image, relative to the jsMacros config folder |

##### Returns: [BufferedImage](https://docs.oracle.com/javase/8/docs/api/index.html?java/awt/image/BufferedImage.html)

an image from the given path.



#### .loadImage(path, x, y, width, height)

1.8.4

Loads the image from the given path and returns a subimage of it from the given positions.
The image can be used with the drawImage methods to draw it onto this image.

| Parameter | Type | Description |
|---|---|---|
| path | String | the path to the image, relative to the jsMacros config folder |
| x | int | the x position to get the subimage from |
| y | int | the y position to get the subimage from |
| width | int | the width of the subimage |
| height | int | the height of the subimage |

##### Returns: [BufferedImage](https://docs.oracle.com/javase/8/docs/api/index.html?java/awt/image/BufferedImage.html)

the cropped image from the given path.



#### .update()

1.8.4

Updates the texture to be drawn with the contents of this image. Any changes made to this
image will only be displayed after calling this method. The method must not be called after
each change, but rather when the image is finished being changed.


##### Returns: [CustomImage](#)

self for chaining.



#### .saveImage(path, fileName)

1.8.4

Saves this image to the given path. The file will be saved as a png.

| Parameter | Type | Description |
|---|---|---|
| path | String | the path to the image, relative to the jsMacros config folder |
| fileName | String | the file name of the image, without the extension |

##### Returns: [CustomImage](#)

self for chaining.



#### .getIdentifier()

1.8.4

The identifier should be used with any buttons and textures in the draw2D and other classes,
which require an identifier.


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of this image.



#### .getWidth()

1.8.4

The width is a constant and will not change.


##### Returns: int

the width of this image.



#### .getHeight()

1.8.4

The height is a constant and will not change.


##### Returns: int

the height of this image.



#### .getImage()

1.8.4


##### Returns: [BufferedImage](https://docs.oracle.com/javase/8/docs/api/index.html?java/awt/image/BufferedImage.html)

the internal BufferedImage of this image, which all updates are made to.



#### .getPixel(x, y)

1.8.4

The color is in the ARGB format.

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to get the color from |
| y | int | the y position to get the color from |

##### Returns: int

the color at the given position.



#### .setPixel(x, y, argb)

1.8.4

The color is in the ARGB format.

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to set the color at |
| y | int | the y position to set the color at |
| argb | int | the ARGB value to set the pixel to |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawImage(img, x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| img | Image | the image to draw onto this image |
| x | int | the x position to draw the image at |
| y | int | the y position to draw the image at |
| width | int | the width of the image to draw |
| height | int | the height of the image to draw |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawImage(img, x, y, width, height, sourceX, sourceY, sourceWidth, sourceHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| img | Image | the image to draw onto this image |
| x | int | the x position to draw the image at |
| y | int | the y position to draw the image at |
| width | int | the width of the image to draw |
| height | int | the height of the image to draw |
| sourceX | int | the x position of the subimage to draw |
| sourceY | int | the y position of the subimage to draw |
| sourceWidth | int | the width of the subimage to draw |
| sourceHeight | int | the height of the subimage to draw |

##### Returns: [CustomImage](#)

self for chaining.



#### .getGraphicsColor()

1.8.4

The color is a rgb value which is used for draw and fill operations.


##### Returns: int

the graphics current rgb color.



#### .setGraphicsColor(color)

1.8.4

The color is a rgb value which is used for draw and fill operations.

| Parameter | Type | Description |
|---|---|---|
| color | int | the rgb color to use for graphics operations |

##### Returns: [CustomImage](#)

self for chaining.



#### .translate(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the origin point |
| y | int | the y position of the origin point |

##### Returns: [CustomImage](#)

self for chaining.



#### .clipRect(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the rectangle to intersect the clip with |
| y | int | the y coordinate of the rectangle to intersect the clip with |
| width | int | the width of the rectangle to intersect the clip with |
| height | int | the height of the rectangle to intersect the clip with |

##### Returns: [CustomImage](#)

self for chaining.



#### .setClip(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the new clip rectangle |
| y | int | the y coordinate of the new clip rectangle |
| width | int | the width of the new clip rectangle |
| height | int | the height of the new clip rectangle |

##### Returns: [CustomImage](#)

self for chaining.



#### .setPaintMode()

1.8.4


##### Returns: [CustomImage](#)

self for chaining.



#### .setXorMode(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color to use for the xor operation |

##### Returns: [CustomImage](#)

self for chaining.



#### .getClipBounds()

1.8.4


##### Returns: [Rectangle](https://docs.oracle.com/javase/8/docs/api/index.html?java/awt/Rectangle.html)

an array with the bounds of the current clip.



#### .copyArea(x, y, width, height, dx, dy)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to copy from |
| y | int | the y position to copy from |
| width | int | the width of the area to copy |
| height | int | the height of the area to copy |
| dx | int | the offset to the x position to copy to |
| dy | int | the offset to the y position to copy to |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawLine(x1, y1, x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the first x position of the line |
| y1 | int | the first y position of the line |
| x2 | int | the second x position of the line |
| y2 | int | the second y position of the line |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawRect(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the rectangle |
| y | int | the y position of the rectangle |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |

##### Returns: [CustomImage](#)

self for chaining.



#### .fillRect(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the rectangle |
| y | int | the y position of the rectangle |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |

##### Returns: [CustomImage](#)

self for chaining.



#### .clearRect(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the rectangle |
| y | int | the y position of the rectangle |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |

##### Returns: [CustomImage](#)

self for chaining.



#### .clearRect(x, y, width, height, color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the rectangle |
| y | int | the y position of the rectangle |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |
| color | int | the rgb color to fill the rectangle with |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawRoundRect(x, y, width, height, arcWidth, arcHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the rectangle at |
| y | int | the y position to draw the rectangle at |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |
| arcWidth | int | the horizontal diameter of the arc at the four corners |
| arcHeight | int | the vertical diameter of the arc at the four corners |

##### Returns: [CustomImage](#)

self for chaining.



#### .fillRoundRect(x, y, width, height, arcWidth, arcHeight)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the rectangle at |
| y | int | the y position to draw the rectangle at |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |
| arcWidth | int | the horizontal diameter of the arc at the four corners |
| arcHeight | int | the vertical diameter of the arc at the four corners |

##### Returns: [CustomImage](#)

self for chaining.



#### .draw3DRect(x, y, width, height, raised)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the 3D rectangle at |
| y | int | the y position to draw the 3D rectangle at |
| width | int | the width of the 3D rectangle |
| height | int | the height of the 3D rectangle |
| raised | boolean | whether the rectangle should be raised above the surface or etched into the
                                       surface |

##### Returns: [CustomImage](#)

self for chaining.



#### .fill3DRect(x, y, width, height, raised)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the 3D rectangle at |
| y | int | the y position to draw the 3D rectangle at |
| width | int | the width of the 3D rectangle |
| height | int | the height of the 3D rectangle |
| raised | boolean | whether the rectangle should be raised above the surface or etched into the
                                       surface |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawOval(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the oval at |
| y | int | the y position to draw the oval at |
| width | int | the width of the oval |
| height | int | the height of the oval |

##### Returns: [CustomImage](#)

self for chaining.



#### .fillOval(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the oval at |
| y | int | the y position to draw the oval at |
| width | int | the width of the oval |
| height | int | the height of the oval |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawArc(x, y, width, height, startAngle, arcAngle)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the arc at |
| y | int | the y position to draw the arc at |
| width | int | the width of the arc |
| height | int | the height of the arc |
| startAngle | int | the beginning angle |
| arcAngle | int | the angular extent of the arc, relative to the start angle |

##### Returns: [CustomImage](#)

self for chaining.



#### .fillArc(x, y, width, height, startAngle, arcAngle)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the arc at |
| y | int | the y position to draw the arc at |
| width | int | the width of the arc |
| height | int | the height of the arc |
| startAngle | int | the beginning angle |
| arcAngle | int | the angular extent of the arc, relative to the start angle |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawPolygonLine(pointsX, pointsY)

1.8.4

The x and y array must have the same length and order for the points.

| Parameter | Type | Description |
|---|---|---|
| pointsX | int[] | an array of all x positions of the points in the polygon |
| pointsY | int[] | an array of all y positions of the points in the polygon |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawPolygon(pointsX, pointsY)

1.8.4

The x and y array must have the same length and order for the points.

| Parameter | Type | Description |
|---|---|---|
| pointsX | int[] | an array of all x positions of the points in the polygon |
| pointsY | int[] | an array of all y positions of the points in the polygon |

##### Returns: [CustomImage](#)

self for chaining.



#### .fillPolygon(pointsX, pointsY)

1.8.4

The x and y array must have the same length and order for the points.

| Parameter | Type | Description |
|---|---|---|
| pointsX | int[] | an array of all x positions of the points in the polygon |
| pointsY | int[] | an array of all y positions of the points in the polygon |

##### Returns: [CustomImage](#)

self for chaining.



#### .drawString(x, y, text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position to draw the string at |
| y | int | the y position to draw the string at |
| text | String | the text to draw |

##### Returns: [CustomImage](#)

self for chaining.



#### .getStringWidth(toAnalyze)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| toAnalyze | String | the string to analyze |

##### Returns: int

the width of the string for the current font in pixels



#### .createWidget(width, height, name)

Static
| Parameter | Type | Description |
|---|---|---|
| width | int |  |
| height | int |  |
| name | String |  |

##### Returns: [CustomImage](#)



#### .createWidget(path, name)

Static
| Parameter | Type | Description |
|---|---|---|
| path | String |  |
| name | String |  |

##### Returns: [CustomImage](#)



#### .nativeARGBFlip(argb)

Static

1.8.4

Minecraft textures use an ABGR format for some reason.

| Parameter | Type | Description |
|---|---|---|
| argb | int | the argb color to transform |

##### Returns: int

the abgr argb for the given argb color.




