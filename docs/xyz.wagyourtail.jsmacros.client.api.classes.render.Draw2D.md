
[Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)

xyz.wagyourtail.jsmacros.client.api.classes.render.Draw2D
---------------------------------------------------------

#### implements [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)<[Draw2D](#)> [Registrable](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Registrable.html)<[Draw2D](#)>

1.0.5

### Constructors

#### new Draw2D ()




#### Fields

[widthSupplier](#widthSupplier)


[heightSupplier](#heightSupplier)


[zIndex](1.9.2/)


[visible](1.9.2/)


[onInit](#onInit)
D


[catchInit](#catchInit)
D



#### Methods

[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[getTexts()](#getTexts-)


[getRects()](#getRects-)


[getLines()](#getLines-)


[getItems()](#getItems-)


[getImages()](#getImages-)


[getDraw2Ds()](#getDraw2Ds-)


[getElements()](#getElements-)


[removeElement(e)](#removeElement-RenderElement-)


[reAddElement(e)](#reAddElement-T-)


[setVisible(visible)](#setVisible-boolean-)


[isVisible()](#isVisible-)


[addDraw2D(draw2D, x, y, width, height)](#addDraw2D-Draw2D-int-int-int-int-)


[addDraw2D(draw2D, x, y, width, height, zIndex)](#addDraw2D-Draw2D-int-int-int-int-int-)


[removeDraw2D(draw2D)](#removeDraw2D-Draw2DElement-)


[addText(text, x, y, color, shadow)](#addText-String-int-int-int-boolean-)


[addText(text, x, y, color, zIndex, shadow)](#addText-String-int-int-int-int-boolean-)


[addText(text, x, y, color, shadow, scale, rotation)](#addText-String-int-int-int-boolean-double-double-)


[addText(text, x, y, color, zIndex, shadow, scale, rotation)](#addText-String-int-int-int-int-boolean-double-double-)


[addText(text, x, y, color, shadow)](#addText-TextHelper-int-int-int-boolean-)


[addText(text, x, y, color, zIndex, shadow)](#addText-TextHelper-int-int-int-int-boolean-)


[addText(text, x, y, color, shadow, scale, rotation)](#addText-TextHelper-int-int-int-boolean-double-double-)


[addText(text, x, y, color, zIndex, shadow, scale, rotation)](#addText-TextHelper-int-int-int-int-boolean-double-double-)


[removeText(t)](#removeText-Text-)


[addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)](#addImage-int-int-int-int-String-int-int-int-int-int-int-)


[addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)](#addImage-int-int-int-int-int-String-int-int-int-int-int-int-)


[addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[addImage(x, y, width, height, zIndex, alpha, color, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)](#addImage-int-int-int-int-int-int-int-String-int-int-int-int-int-int-double-)


[removeImage(i)](#removeImage-Image-)


[addRect(x1, y1, x2, y2, color)](#addRect-int-int-int-int-int-)


[addRect(x1, y1, x2, y2, color, alpha)](#addRect-int-int-int-int-int-int-)


[addRect(x1, y1, x2, y2, color, alpha, rotation)](#addRect-int-int-int-int-int-int-double-)


[addRect(x1, y1, x2, y2, color, alpha, rotation, zIndex)](#addRect-int-int-int-int-int-int-double-int-)


[removeRect(r)](#removeRect-Rect-)


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


[addItem(x, y, Item)](#addItem-int-int-ItemStackHelper-)


[addItem(x, y, zIndex, item)](#addItem-int-int-int-ItemStackHelper-)


[addItem(x, y, Item, overlay)](#addItem-int-int-ItemStackHelper-boolean-)


[addItem(x, y, zIndex, item, overlay)](#addItem-int-int-int-ItemStackHelper-boolean-)


[addItem(x, y, item, overlay, scale, rotation)](#addItem-int-int-ItemStackHelper-boolean-double-double-)


[addItem(x, y, zIndex, item, overlay, scale, rotation)](#addItem-int-int-int-ItemStackHelper-boolean-double-double-)


[removeItem(i)](#removeItem-Item-)


[init()](#init-)


[render(drawContext)](#render-DrawContext-)


[getElementsByZIndex()](#getElementsByZIndex-)


[setOnInit(onInit)](#setOnInit-MethodWrapper-)


[setOnFailInit(catchInit)](#setOnFailInit-MethodWrapper-)


[register()](#register-)


[unregister()](#unregister-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)



### Fields

#### .widthSupplier


##### Type: [IntSupplier](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/IntSupplier.html)



#### .heightSupplier


##### Type: [IntSupplier](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/IntSupplier.html)



#### .zIndex


##### Type: int



#### .visible


##### Type: boolean



#### .onInit

Deprecated

1.0.5


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Draw2D](#), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .catchInit

Deprecated

1.1.9 [citation needed]


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



### Methods

#### .getWidth()

1.0.5


##### Returns: int



#### .getHeight()

1.0.5


##### Returns: int



#### .getTexts()

1.0.5


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)>



#### .getRects()

1.0.5


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)>



#### .getLines()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)>



#### .getItems()

1.0.5


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)>



#### .getImages()

1.2.3


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)>



#### .getDraw2Ds()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)>



#### .getElements()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)>



#### .removeElement(e)

| Parameter | Type | Description |
|---|---|---|
| e | RenderElement |  |

##### Returns: [Draw2D](#)



#### .reAddElement< T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) >(e)

| Parameter | Type | Description |
|---|---|---|
| e | T
                             extends RenderElement |  |

##### Returns: T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)



#### .setVisible(visible)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| visible | boolean | whether to render this element. |

##### Returns: [Draw2D](#)

self for chaining.



#### .isVisible()

1.8.4


##### Returns: boolean

`true` if this draw2d is visible, `false` otherwise.



#### .addDraw2D(draw2D, x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D |  |
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: [Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)



#### .addDraw2D(draw2D, x, y, width, height, zIndex)

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2D |  |
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |

##### Returns: [Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)



#### .removeDraw2D(draw2D)

| Parameter | Type | Description |
|---|---|---|
| draw2D | Draw2DElement |  |

##### Returns: [Draw2D](#)



#### .addText(text, x, y, color, shadow)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int |  |
| y | int |  |
| color | int |  |
| shadow | boolean |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, zIndex, shadow)

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, shadow, scale, rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int |  |
| y | int |  |
| color | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, zIndex, shadow, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| text | String |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, shadow)

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int |  |
| y | int |  |
| color | int |  |
| shadow | boolean |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, zIndex, shadow)

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, shadow, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int |  |
| y | int |  |
| color | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .addText(text, x, y, color, zIndex, shadow, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| x | int |  |
| y | int |  |
| color | int |  |
| zIndex | int |  |
| shadow | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)



#### .removeText(t)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| t | Text |  |

##### Returns: [Draw2D](#)



#### .addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



#### .addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



#### .addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |
| rotation | double |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



#### .addImage(x, y, width, height, zIndex, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight, rotation)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| id | String |  |
| imageX | int |  |
| imageY | int |  |
| regionWidth | int |  |
| regionHeight | int |  |
| textureWidth | int |  |
| textureHeight | int |  |
| rotation | double |  |

##### Returns: [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)



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

1.2.3

| Parameter | Type | Description |
|---|---|---|
| i | Image |  |

##### Returns: [Draw2D](#)



#### .addRect(x1, y1, x2, y2, color)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



#### .addRect(x1, y1, x2, y2, color, alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| alpha | int |  |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



#### .addRect(x1, y1, x2, y2, color, alpha, rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| alpha | int |  |
| rotation | double |  |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



#### .addRect(x1, y1, x2, y2, color, alpha, rotation, zIndex)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| alpha | int |  |
| rotation | double |  |
| zIndex | int |  |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



#### .removeRect(r)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| r | Rect |  |

##### Returns: [Draw2D](#)



#### .addLine(x1, y1, x2, y2, color)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .addLine(x1, y1, x2, y2, color, zIndex)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| zIndex | int |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .addLine(x1, y1, x2, y2, color, width)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| width | double |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .addLine(x1, y1, x2, y2, color, zIndex, width)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| zIndex | int |  |
| width | double |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .addLine(x1, y1, x2, y2, color, width, rotation)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| width | double |  |
| rotation | double |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .addLine(x1, y1, x2, y2, color, zIndex, width, rotation)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |
| zIndex | int |  |
| width | double |  |
| rotation | double |  |

##### Returns: [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)



#### .removeLine(l)

| Parameter | Type | Description |
|---|---|---|
| l | Line |  |

##### Returns: [Draw2D](#)



#### .addItem(x, y, id)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| id | String |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, id)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| id | String |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, id, overlay)

1.2.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| id | String |  |
| overlay | boolean |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, id, overlay)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| id | String |  |
| overlay | boolean |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, id, overlay, scale, rotation)

1.2.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| id | String |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, id, overlay, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| id | String |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, Item)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| Item | ItemStackHelper |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, item)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| item | ItemStackHelper |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, Item, overlay)

1.2.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| Item | ItemStackHelper |  |
| overlay | boolean |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, item, overlay)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| item | ItemStackHelper |  |
| overlay | boolean |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, item, overlay, scale, rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| item | ItemStackHelper |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, item, overlay, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| item | ItemStackHelper |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | double |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .removeItem(i)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| i | Item |  |

##### Returns: [Draw2D](#)



#### .init()


##### Returns: void



#### .render(drawContext)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |

##### Returns: void



#### .getElementsByZIndex()


##### Returns: [Iterator](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Iterator.html)<[RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)>



#### .setOnInit(onInit)

1.2.7

init function, called when window is resized or screen/draw2d is registered.
clears all previous elements when called.

| Parameter | Type | Description |
|---|---|---|
| onInit | MethodWrapper<Draw2D, Object, Object, ?> | calls your method as a Consumer<Draw2D> |

##### Returns: [Draw2D](#)



#### .setOnFailInit(catchInit)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| catchInit | MethodWrapper<String, Object, Object, ?> | calls your method as a Consumer<String> |

##### Returns: [Draw2D](#)



#### .register()

1.6.5

register so the overlay actually renders


##### Returns: [Draw2D](#)

self for chaining



#### .unregister()

1.6.5

unregister so the overlay stops rendering


##### Returns: [Draw2D](#)

self for chaining



#### .setZIndex(zIndex)

| Parameter | Type | Description |
|---|---|---|
| zIndex | int |  |

##### Returns: void



#### .getZIndex()


##### Returns: int




