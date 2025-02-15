
[Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html) [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html) [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html) [MixinScreen](1.9.2/xyz/wagyourtail/jsmacros/client/mixins/access/MixinScreen.html)

xyz.wagyourtail.jsmacros.client.api.classes.render.IDraw2D< T >
---------------------------------------------------------------

Interface
#### 

1.2.7

#### Methods

[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[getTexts()](#getTexts-)
D


[getRects()](#getRects-)
D


[getLines()](#getLines-)


[getItems()](#getItems-)
D


[getImages()](#getImages-)
D


[getDraw2Ds()](#getDraw2Ds-)


[getElements()](#getElements-)


[removeElement(e)](#removeElement-RenderElement-)


[reAddElement(e)](#reAddElement-T-)


[addText(text, x, y, color, shadow)](#addText-String-int-int-int-boolean-)


[addText(text, x, y, color, zIndex, shadow)](#addText-String-int-int-int-int-boolean-)


[addText(text, x, y, color, shadow, scale, rotation)](#addText-String-int-int-int-boolean-double-double-)


[addText(text, x, y, color, zIndex, shadow, scale, rotation)](#addText-String-int-int-int-int-boolean-double-double-)


[addText(text, x, y, color, shadow)](#addText-TextHelper-int-int-int-boolean-)


[addText(text, x, y, color, zIndex, shadow)](#addText-TextHelper-int-int-int-int-boolean-)


[addText(text, x, y, color, shadow, scale, rotation)](#addText-TextHelper-int-int-int-boolean-double-double-)


[addText(text, x, y, color, zIndex, shadow, scale, rotation)](#addText-TextHelper-int-int-int-int-boolean-double-double-)


[removeText(t)](#removeText-Text-)
D


[addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)](#addImage-int-int-int-int-String-int-int-int-int-int-int-)


[addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)](#addImage-int-int-int-int-int-String-int-int-int-int-int-int-)


[addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, alpha, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[removeImage(i)](#removeImage-Image-)
D


[addRect(x1, y1, x2, y2, color)](#addRect-int-int-int-int-int-)


[addRect(x1, y1, x2, y2, color, alpha)](#addRect-int-int-int-int-int-int-)


[addRect(x1, y1, x2, y2, color, alpha, rotation)](#addRect-int-int-int-int-int-int-double-)


[addRect(x1, y1, x2, y2, color, alpha, rotation, zIndex)](#addRect-int-int-int-int-int-int-double-int-)


[removeRect(r)](#removeRect-Rect-)
D


[addLine(x1, y1, x2, y2, color)](#addLine-int-int-int-int-int-)


[addLine(x1, y1, x2, y2, color, zIndex)](#addLine-int-int-int-int-int-int-)


[addLine(x1, y1, x2, y2, color, width)](#addLine-int-int-int-int-int-double-)


[addLine(x1, y1, x2, y2, color, zIndex, width)](#addLine-int-int-int-int-int-int-double-)


[addLine(x1, y1, x2, y2, color, width, rotation)](#addLine-int-int-int-int-int-double-double-)


[addLine(x1, y1, x2, y2, color, zIndex, width, rotation)](#addLine-int-int-int-int-int-int-double-double-)


[removeLine(l)](#removeLine-Line-)


[addItem(x, y, id)](#addItem-int-int-String-)


[addItem(x, y, zIndex, id)](#addItem-int-int-int-String-)


[addItem(x, y, id, overlay)](#addItem-int-int-String-boolean-)


[addItem(x, y, zIndex, id, overlay)](#addItem-int-int-int-String-boolean-)


[addItem(x, y, id, overlay, scale, rotation)](#addItem-int-int-String-boolean-double-double-)


[addItem(x, y, zIndex, id, overlay, scale, rotation)](#addItem-int-int-int-String-boolean-double-double-)


[addItem(x, y, item)](#addItem-int-int-ItemStackHelper-)


[addItem(x, y, zIndex, item)](#addItem-int-int-int-ItemStackHelper-)


[addItem(x, y, item, overlay)](#addItem-int-int-ItemStackHelper-boolean-)


[addItem(x, y, zIndex, item, overlay)](#addItem-int-int-int-ItemStackHelper-boolean-)


[addItem(x, y, item, overlay, scale, rotation)](#addItem-int-int-ItemStackHelper-boolean-double-double-)


[addItem(x, y, zIndex, item, overlay, scale, rotation)](#addItem-int-int-int-ItemStackHelper-boolean-double-double-)


[removeItem(i)](#removeItem-Item-)
D


[addDraw2D(draw2D, x, y, width, height)](#addDraw2D-Draw2D-int-int-int-int-)


[addDraw2D(draw2D, x, y, width, height, zIndex)](#addDraw2D-Draw2D-int-int-int-int-int-)


[removeDraw2D(draw2D)](#removeDraw2D-Draw2DElement-)


[itemBuilder()](#itemBuilder-)


[itemBuilder(item)](#itemBuilder-ItemStackHelper-)


[imageBuilder()](#imageBuilder-)


[imageBuilder(id)](#imageBuilder-String-)


[rectBuilder()](#rectBuilder-)


[rectBuilder(x, y, width, height)](#rectBuilder-int-int-int-int-)


[lineBuilder()](#lineBuilder-)


[lineBuilder(x1, y1, x2, y2)](#lineBuilder-int-int-int-int-)


[textBuilder()](#textBuilder-)


[textBuilder(text)](#textBuilder-String-)


[textBuilder(text)](#textBuilder-TextHelper-)


[draw2DBuilder(draw2D)](#draw2DBuilder-Draw2D-)


[setOnInit(onInit)](#setOnInit-MethodWrapper-)


[setOnFailInit(catchInit)](#setOnFailInit-MethodWrapper-)


[render(drawContext)](#render-DrawContext-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)



### Methods

#### .getWidth()

1.2.7


##### Returns: int

screen width



#### .getHeight()

1.2.7


##### Returns: int

screen height



#### .getTexts()

Deprecated

1.2.7


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)>

text elements



#### .getRects()

Deprecated

1.2.7


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)>

rect elements



#### .getLines()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)>

all registered line elements.



#### .getItems()

Deprecated

1.2.7


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)>

item elements



#### .getImages()

Deprecated

1.2.7


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)>

image elements



#### .getDraw2Ds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)>

all registered draw2d elements.



#### .getElements()

1.2.9


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)>

a read only copy of the list of all elements added by scripts.



#### .removeElement(e)

1.2.9

removes any element regardless of type.

| Parameter | Type | Description |
|---|---|---|
| e | RenderElement |  |

##### Returns: T

self for chaining



#### .reAddElement< T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) >(e)

1.2.9

re-add an element you removed with [IDraw2D#removeElement(xyz.wagyourtail.jsmacros.client.api.classes.render.components.RenderElement)](#removeElement-RenderElement-)

| Parameter | Type | Description |
|---|---|---|
| e | T
                             extends RenderElement |  |

##### Returns: T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)

self for chaining



#### .addText(text, x, y, color, shadow)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| shadow | boolean | include shadow layer |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, zIndex, shadow)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| zIndex | int | z-index |
| shadow | boolean | include shadow layer |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, shadow, scale, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| shadow | boolean | include shadow layer |
| scale | double | text scale (as double) |
| rotation | double | text rotation (as degrees) |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, zIndex, shadow, scale, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| zIndex | int | z-index |
| shadow | boolean | include shadow layer |
| scale | double | text scale (as double) |
| rotation | double | text rotation (as degrees) |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, shadow)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| shadow | boolean | include shadow layer |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, zIndex, shadow)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| zIndex | int | z-index |
| shadow | boolean | include shadow layer |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, shadow, scale, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| shadow | boolean | include shadow layer |
| scale | double | text scale (as double) |
| rotation | double | text rotation (as degrees) |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .addText(text, x, y, color, zIndex, shadow, scale, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int | screen x |
| y | int | screen y |
| color | int | text color |
| zIndex | int | z-index |
| shadow | boolean | include shadow layer |
| scale | double | text scale (as double) |
| rotation | double | text rotation (as degrees) |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)

added text



#### .removeText(t)

Deprecated

1.2.7

| Parameter | Type | Description |
|---|---|---|
| t | Text |  |

##### Returns: T

self for chaining



#### .addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | screen x, top left corner |
| y | int | screen y, top left corner |
| width | int | width on screen |
| height | int | height on screen |
| id | String | image id, in the form minecraft:textures path'd as found in texture packs, ie assets/minecraft/textures/gui/recipe_book.png becomes minecraft:textures/gui/recipe_book.png |
| imageX | int | the left-most coordinate of the texture region |
| imageY | int | the top-most coordinate of the texture region |
| regionWidth | int | the width the texture region |
| regionHeight | int | the height the texture region |
| textureWidth | int | the width of the entire texture |
| textureHeight | int | the height of the entire texture |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)

added image



#### .addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | screen x, top left corner |
| y | int | screen y, top left corner |
| width | int | width on screen |
| height | int | height on screen |
| zIndex | int | z-index |
| id | String | image id, in the form minecraft:textures path'd as found in texture packs, ie assets/minecraft/textures/gui/recipe_book.png becomes minecraft:textures/gui/recipe_book.png |
| imageX | int | the left-most coordinate of the texture region |
| imageY | int | the top-most coordinate of the texture region |
| regionWidth | int | the width the texture region |
| regionHeight | int | the height the texture region |
| textureWidth | int | the width of the entire texture |
| textureHeight | int | the height of the entire texture |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)

added image



#### .addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | screen x, top left corner |
| y | int | screen y, top left corner |
| width | int | width on screen |
| height | int | height on screen |
| id | String | image id, in the form minecraft:textures path'd as found in texture packs, ie assets/minecraft/textures/gui/recipe_book.png becomes minecraft:textures/gui/recipe_book.png |
| imageX | int | the left-most coordinate of the texture region |
| imageY | int | the top-most coordinate of the texture region |
| regionWidth | int | the width the texture region |
| regionHeight | int | the height the texture region |
| textureWidth | int | the width of the entire texture |
| textureHeight | int | the height of the entire texture |
| rotation | double | the rotation (clockwise) of the texture (as degrees) |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)

added image



#### .addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | screen x, top left corner |
| y | int | screen y, top left corner |
| width | int | width on screen |
| height | int | height on screen |
| zIndex | int | z-index |
| id | String | image id, in the form minecraft:textures path'd as found in texture packs, ie assets/minecraft/textures/gui/recipe_book.png becomes minecraft:textures/gui/recipe_book.png |
| imageX | int | the left-most coordinate of the texture region |
| imageY | int | the top-most coordinate of the texture region |
| regionWidth | int | the width the texture region |
| regionHeight | int | the height the texture region |
| textureWidth | int | the width of the entire texture |
| textureHeight | int | the height of the entire texture |
| rotation | double | the rotation (clockwise) of the texture (as degrees) |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)

added image



#### .addImage(x, y, width, height, zIndex, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.6.5

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
| rotation | double |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



#### .addImage(x, y, width, height, zIndex, alpha, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.6.5

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
| rotation | double |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



#### .removeImage(i)

Deprecated

1.2.7

| Parameter | Type | Description |
|---|---|---|
| i | Image |  |

##### Returns: T

self for chaining



#### .addRect(x1, y1, x2, y2, color)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int | as hex, with alpha channel |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)

added rect



#### .addRect(x1, y1, x2, y2, color, alpha)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int | as hex |
| alpha | int | alpha channel 0-255 |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)

added rect



#### .addRect(x1, y1, x2, y2, color, alpha, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int | as hex |
| alpha | int | alpha channel 0-255 |
| rotation | double | as degrees |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)

added rect



#### .addRect(x1, y1, x2, y2, color, alpha, rotation, zIndex)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int | as hex |
| alpha | int | alpha channel 0-255 |
| rotation | double | as degrees |
| zIndex | int | z-index |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)

added rect



#### .removeRect(r)

Deprecated

1.2.7

| Parameter | Type | Description |
|---|---|---|
| r | Rect |  |

##### Returns: T

self for chaining



#### .addLine(x1, y1, x2, y2, color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .addLine(x1, y1, x2, y2, color, zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |
| zIndex | int | the z-index of the line |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .addLine(x1, y1, x2, y2, color, width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |
| width | double | the width of the line |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .addLine(x1, y1, x2, y2, color, zIndex, width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |
| zIndex | int | the z-index of the line |
| width | double | the width of the line |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .addLine(x1, y1, x2, y2, color, width, rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |
| width | double | the width of the line |
| rotation | double | the rotation (clockwise) of the line (as degrees) |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .addLine(x1, y1, x2, y2, color, zIndex, width, rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the start |
| y1 | int | the y position of the start |
| x2 | int | the x position of the end |
| y2 | int | the y position of the end |
| color | int | the color of the line, can include alpha value |
| zIndex | int | the z-index of the line |
| width | double | the width of the line |
| rotation | double | the rotation (clockwise) of the line (as degrees) |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)

the added line.



#### .removeLine(l)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| l | Line | the line to remove |

##### Returns: T

self chaining.



#### .addItem(x, y, id)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| id | String | item id |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, id)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| id | String | item id |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, id, overlay)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| id | String | item id |
| overlay | boolean | should include overlay health and count |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, id, overlay)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| id | String | item id |
| overlay | boolean | should include overlay health and count |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, id, overlay, scale, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| id | String | item id |
| overlay | boolean | should include overlay health and count |
| scale | double | scale of item |
| rotation | double | rotation of item |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, id, overlay, scale, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| id | String | item id |
| overlay | boolean | should include overlay health and count |
| scale | double | scale of item |
| rotation | double | rotation of item |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, item)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| item | ItemStackHelper | from inventory as helper |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, item)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| item | ItemStackHelper | from inventory as helper |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, item, overlay)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| item | ItemStackHelper | from inventory as helper |
| overlay | boolean | should include overlay health and count |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, item, overlay)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| item | ItemStackHelper | from inventory as helper |
| overlay | boolean | should include overlay health and count |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, item, overlay, scale, rotation)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| item | ItemStackHelper | from inventory as helper |
| overlay | boolean | should include overlay health and count |
| scale | double | scale of item |
| rotation | double | rotation of item |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .addItem(x, y, zIndex, item, overlay, scale, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int | left most corner |
| y | int | top most corner |
| zIndex | int | z-index |
| item | ItemStackHelper | from inventory as helper |
| overlay | boolean | should include overlay health and count |
| scale | double | scale of item |
| rotation | double | rotation of item |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)

added item



#### .removeItem(i)

Deprecated

1.2.7

| Parameter | Type | Description |
|---|---|---|
| i | Item |  |

##### Returns: T

self for chaining



#### .addDraw2D(draw2D, x, y, width, height)

1.8.4

Tries to add the given draw2d as a child. Fails if cyclic dependencies are detected.

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D | the draw2d to add |
| x | int | the x position on this draw2d |
| y | int | the y position on this draw2d |
| width | int | the width of the given draw2d |
| height | int | the height of the given draw2d |

##### Returns: [Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)

a wrapper for the draw2d.



#### .addDraw2D(draw2D, x, y, width, height, zIndex)

1.8.4

Tries to add the given draw2d as a child. Fails if cyclic dependencies are detected.

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D | the draw2d to add |
| x | int | the x position on this draw2d |
| y | int | the y position on this draw2d |
| width | int | the width of the given draw2d |
| height | int | the height of the given draw2d |
| zIndex | int | the z-index for the draw2d |

##### Returns: [Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)

a wrapper for the draw2d.



#### .removeDraw2D(draw2D)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2DElement | the draw2d to remove |

##### Returns: T

self chaining.



#### .itemBuilder()

1.8.4


##### Returns: [Item$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.Builder.html)

a builder for an [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html).



#### .itemBuilder(item)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| item | ItemStackHelper | the item to use |

##### Returns: [Item$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.Builder.html)

a builder for an [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html).



#### .imageBuilder()

1.8.4


##### Returns: [Image$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.Builder.html)

a builder for an [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html).



#### .imageBuilder(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the image |

##### Returns: [Image$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.Builder.html)

a builder for an [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html).



#### .rectBuilder()

1.8.4


##### Returns: [Rect$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.Builder.html)

a builder for a [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html).



#### .rectBuilder(x, y, width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the rectangle |
| y | int | the y position of the rectangle |
| width | int | the width of the rectangle |
| height | int | the height of the rectangle |

##### Returns: [Rect$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.Builder.html)

a builder for a [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html).



#### .lineBuilder()

1.8.4


##### Returns: [Line$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.Builder.html)

a builder for a [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html).



#### .lineBuilder(x1, y1, x2, y2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x position of the first point |
| y1 | int | the y position of the first point |
| x2 | int | the x position of the second point |
| y2 | int | the y position of the second point |

##### Returns: [Line$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.Builder.html)

a builder for a [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html).



#### .textBuilder()

1.8.4


##### Returns: [Text$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.Builder.html)

a builder for a [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html).



#### .textBuilder(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | String | the text to display |

##### Returns: [Text$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.Builder.html)

a builder for a [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html).



#### .textBuilder(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper | the text to display |

##### Returns: [Text$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.Builder.html)

a builder for a [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html).



#### .draw2DBuilder(draw2D)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D | the draw2d to add |

##### Returns: [Draw2DElement$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.Builder.html)

a builder for a [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html).



#### .setOnInit(onInit)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onInit | MethodWrapper<T, Object, Object, ?> | calls your method as a Consumer<IDraw2D#T> |

##### Returns: T

self for chaining



#### .setOnFailInit(catchInit)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| catchInit | MethodWrapper<String, Object, Object, ?> | calls your method as a Consumer<String> |

##### Returns: T

self for chaining



#### .render(drawContext)

internal

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |

##### Returns: void



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int |  |

##### Returns: void



#### .getZIndex()

1.8.4


##### Returns: int




