

xyz.wagyourtail.jsmacros.client.mixins.access.MixinScreen
---------------------------------------------------------

Abstract
#### extends [AbstractParentElement](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/AbstractParentElement) implements [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html) [IScreenInternal](1.9.2/xyz/wagyourtail/jsmacros/client/access/IScreenInternal.html)

### Constructors

#### new MixinScreen ()




#### Fields

[width](1.9.2/)


[height](1.9.2/)


[textRenderer](#textRenderer)



#### Methods

[onClose()](#onClose-)
A


[tick()](#tick-)
A


[handleTextClick(style)](#handleTextClick-Style-)
A


[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[getDraw2Ds()](#getDraw2Ds-)


[addDraw2D(draw2D, x, y, width, height)](#addDraw2D-Draw2D-int-int-int-int-)


[addDraw2D(draw2D, x, y, width, height, zIndex)](#addDraw2D-Draw2D-int-int-int-int-int-)


[removeDraw2D(draw2D)](#removeDraw2D-Draw2DElement-)


[getLines()](#getLines-)


[getTexts()](#getTexts-)


[getRects()](#getRects-)


[getItems()](#getItems-)


[getImages()](#getImages-)


[getTextFields()](#getTextFields-)


[getButtonWidgets()](#getButtonWidgets-)


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


[addItem(x, y, item)](#addItem-int-int-ItemStackHelper-)


[addItem(x, y, zIndex, item)](#addItem-int-int-int-ItemStackHelper-)


[addItem(x, y, item, overlay)](#addItem-int-int-ItemStackHelper-boolean-)


[addItem(x, y, zIndex, item, overlay)](#addItem-int-int-int-ItemStackHelper-boolean-)


[addItem(x, y, item, overlay, scale, rotation)](#addItem-int-int-ItemStackHelper-boolean-double-double-)


[addItem(x, y, zIndex, item, overlay, scale, rotation)](#addItem-int-int-int-ItemStackHelper-boolean-double-double-)


[removeItem(i)](#removeItem-Item-)


[getScreenClassName()](#getScreenClassName-)


[getTitleText()](#getTitleText-)


[addButton(x, y, width, height, text, callback)](#addButton-int-int-int-int-String-MethodWrapper-)


[addButton(x, y, width, height, zIndex, text, callback)](#addButton-int-int-int-int-int-String-MethodWrapper-)


[addCheckbox(x, y, width, height, text, checked, showMessage, callback)](#addCheckbox-int-int-int-int-String-boolean-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, text, checked, callback)](#addCheckbox-int-int-int-int-String-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, zIndex, text, checked, callback)](#addCheckbox-int-int-int-int-int-String-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, zIndex, text, checked, showMessage, callback)](#addCheckbox-int-int-int-int-int-String-boolean-boolean-MethodWrapper-)


[addSlider(x, y, width, height, text, value, steps, callback)](#addSlider-int-int-int-int-String-double-int-MethodWrapper-)


[addSlider(x, y, width, height, zIndex, text, value, callback)](#addSlider-int-int-int-int-int-String-double-MethodWrapper-)


[addSlider(x, y, width, height, text, value, callback)](#addSlider-int-int-int-int-String-double-MethodWrapper-)


[addSlider(x, y, width, height, zIndex, text, value, steps, callback)](#addSlider-int-int-int-int-int-String-double-int-MethodWrapper-)


[addLockButton(x, y, callback)](#addLockButton-int-int-MethodWrapper-)


[addLockButton(x, y, zIndex, callback)](#addLockButton-int-int-int-MethodWrapper-)


[addCyclingButton(x, y, width, height, values, initial, callback)](#addCyclingButton-int-int-int-int-String[]-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, initial, callback)](#addCyclingButton-int-int-int-int-int-String[]-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, callback)](#addCyclingButton-int-int-int-int-int-String[]-String[]-String-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, alternateToggle, callback)](#addCyclingButton-int-int-int-int-int-String[]-String[]-String-String-MethodWrapper-MethodWrapper-)


[removeButton(btn)](#removeButton-ClickableWidgetHelper-)


[addTextInput(x, y, width, height, message, onChange)](#addTextInput-int-int-int-int-String-MethodWrapper-)


[addTextInput(x, y, width, height, zIndex, message, onChange)](#addTextInput-int-int-int-int-int-String-MethodWrapper-)


[removeTextInput(inp)](#removeTextInput-TextFieldWidgetHelper-)


[soft$close()](#soft$close-)


[setOnMouseDown(onMouseDown)](#setOnMouseDown-MethodWrapper-)


[setOnMouseDrag(onMouseDrag)](#setOnMouseDrag-MethodWrapper-)


[setOnMouseUp(onMouseUp)](#setOnMouseUp-MethodWrapper-)


[setOnScroll(onScroll)](#setOnScroll-MethodWrapper-)


[setOnKeyPressed(onKeyPressed)](#setOnKeyPressed-MethodWrapper-)


[setOnCharTyped(onCharTyped)](#setOnCharTyped-MethodWrapper-)


[setOnInit(onInit)](#setOnInit-MethodWrapper-)


[setOnFailInit(catchInit)](#setOnFailInit-MethodWrapper-)


[setOnClose(onClose)](#setOnClose-MethodWrapper-)


[reloadScreen()](#reloadScreen-)


[buttonBuilder()](#buttonBuilder-)


[checkBoxBuilder()](#checkBoxBuilder-)


[checkBoxBuilder(checked)](#checkBoxBuilder-boolean-)


[cyclicButtonBuilder(valueToText)](#cyclicButtonBuilder-MethodWrapper-)


[lockButtonBuilder()](#lockButtonBuilder-)


[lockButtonBuilder(locked)](#lockButtonBuilder-boolean-)


[sliderBuilder()](#sliderBuilder-)


[textFieldBuilder()](#textFieldBuilder-)


[texturedButtonBuilder()](#texturedButtonBuilder-)


[jsmacros\_render(drawContext, mouseX, mouseY, delta)](#jsmacros_render-DrawContext-int-int-float-)


[jsmacros\_mouseClicked(mouseX, mouseY, button)](#jsmacros_mouseClicked-double-double-int-)


[jsmacros\_mouseDragged(mouseX, mouseY, button, deltaX, deltaY)](#jsmacros_mouseDragged-double-double-int-double-double-)


[jsmacros\_mouseReleased(mouseX, mouseY, button)](#jsmacros_mouseReleased-double-double-int-)


[jsmacros\_keyPressed(keyCode, scanCode, modifiers)](#jsmacros_keyPressed-int-int-int-)


[jsmacros\_charTyped(chr, modifiers)](#jsmacros_charTyped-char-int-)


[jsmacros\_mouseScrolled(mouseX, mouseY, horiz, vert)](#jsmacros_mouseScrolled-double-double-double-double-)


[handleCustomClickEvent(style, cir)](#handleCustomClickEvent-Style-CallbackInfoReturnable-)


[getOnClose()](#getOnClose-)



### Fields

#### .width


##### Type: int



#### .height


##### Type: int



#### .textRenderer


##### Type: [TextRenderer](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/font/TextRenderer)



### Methods

#### .onClose()

Abstract

##### Returns: void



#### .tick()

Abstract

##### Returns: void



#### .handleTextClick(style)

Abstract
| Parameter | Type | Description |
|---|---|---|
| style | Style |  |

##### Returns: boolean



#### .getWidth()


##### Returns: int



#### .getHeight()


##### Returns: int



#### .getDraw2Ds()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html)>



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

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .getLines()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html)>



#### .getTexts()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html)>



#### .getRects()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)>



#### .getItems()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)>



#### .getImages()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html)>



#### .getTextFields()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)>



#### .getButtonWidgets()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >>



#### .getElements()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)>



#### .removeElement(e)

| Parameter | Type | Description |
|---|---|---|
| e | RenderElement |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .reAddElement< T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) >(e)

| Parameter | Type | Description |
|---|---|---|
| e | T
                             extends RenderElement |  |

##### Returns: T **extends** [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html)



#### .addText(text, x, y, color, shadow)

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

| Parameter | Type | Description |
|---|---|---|
| t | Text |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .addImage(x, y, width, height, id, imageX, imageY, regionWidth, regionHeight, textureWidth, textureHeight)

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

| Parameter | Type | Description |
|---|---|---|
| i | Image |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .addRect(x1, y1, x2, y2, color)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| x2 | int |  |
| y2 | int |  |
| color | int |  |

##### Returns: [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html)



#### .addRect(x1, y1, x2, y2, color, alpha)

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

| Parameter | Type | Description |
|---|---|---|
| r | Rect |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



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

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .addItem(x, y, id)

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



#### .addItem(x, y, item)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| item | ItemStackHelper |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, zIndex, item)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| item | ItemStackHelper |  |

##### Returns: [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)



#### .addItem(x, y, item, overlay)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| item | ItemStackHelper |  |
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

| Parameter | Type | Description |
|---|---|---|
| i | Item |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .getScreenClassName()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getTitleText()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .addButton(x, y, width, height, text, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| callback | MethodWrapper<ClickableWidgetHelper<?, ?>, IScreen, Object, ?> |  |

##### Returns: [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >



#### .addButton(x, y, width, height, zIndex, text, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| callback | MethodWrapper<ClickableWidgetHelper<?, ?>, IScreen, Object, ?> |  |

##### Returns: [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >



#### .addCheckbox(x, y, width, height, text, checked, showMessage, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| checked | boolean |  |
| showMessage | boolean |  |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)



#### .addCheckbox(x, y, width, height, text, checked, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| checked | boolean |  |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)



#### .addCheckbox(x, y, width, height, zIndex, text, checked, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| checked | boolean |  |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)



#### .addCheckbox(x, y, width, height, zIndex, text, checked, showMessage, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| checked | boolean |  |
| showMessage | boolean |  |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)



#### .addSlider(x, y, width, height, text, value, steps, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| value | double |  |
| steps | int |  |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)



#### .addSlider(x, y, width, height, zIndex, text, value, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| value | double |  |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)



#### .addSlider(x, y, width, height, text, value, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| value | double |  |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)



#### .addSlider(x, y, width, height, zIndex, text, value, steps, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| value | double |  |
| steps | int |  |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)



#### .addLockButton(x, y, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| callback | MethodWrapper<LockButtonWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)



#### .addLockButton(x, y, zIndex, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| callback | MethodWrapper<LockButtonWidgetHelper, IScreen, Object, ?> |  |

##### Returns: [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)



#### .addCyclingButton(x, y, width, height, values, initial, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| values | String[] |  |
| initial | String |  |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> |  |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >



#### .addCyclingButton(x, y, width, height, zIndex, values, initial, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| values | String[] |  |
| initial | String |  |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> |  |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >



#### .addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| values | String[] |  |
| alternatives | String[] |  |
| initial | String |  |
| prefix | String |  |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> |  |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >



#### .addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, alternateToggle, callback)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| values | String[] |  |
| alternatives | String[] |  |
| initial | String |  |
| prefix | String |  |
| alternateToggle | MethodWrapper<?, ?, Boolean, ?> |  |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> |  |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >



#### .removeButton(btn)

| Parameter | Type | Description |
|---|---|---|
| btn | ClickableWidgetHelper<?, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .addTextInput(x, y, width, height, message, onChange)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| message | String |  |
| onChange | MethodWrapper<String, IScreen, Object, ?> |  |

##### Returns: [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)



#### .addTextInput(x, y, width, height, zIndex, message, onChange)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| message | String |  |
| onChange | MethodWrapper<String, IScreen, Object, ?> |  |

##### Returns: [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)



#### .removeTextInput(inp)

| Parameter | Type | Description |
|---|---|---|
| inp | TextFieldWidgetHelper |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .soft$close()


##### Returns: void



#### .setOnMouseDown(onMouseDown)

| Parameter | Type | Description |
|---|---|---|
| onMouseDown | MethodWrapper<Pos2D, Integer, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnMouseDrag(onMouseDrag)

| Parameter | Type | Description |
|---|---|---|
| onMouseDrag | MethodWrapper<Vec2D, Integer, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnMouseUp(onMouseUp)

| Parameter | Type | Description |
|---|---|---|
| onMouseUp | MethodWrapper<Pos2D, Integer, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnScroll(onScroll)

| Parameter | Type | Description |
|---|---|---|
| onScroll | MethodWrapper<Pos2D, Pos2D, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnKeyPressed(onKeyPressed)

| Parameter | Type | Description |
|---|---|---|
| onKeyPressed | MethodWrapper<Integer, Integer, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnCharTyped(onCharTyped)

| Parameter | Type | Description |
|---|---|---|
| onCharTyped | MethodWrapper<Character, Integer, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnInit(onInit)

| Parameter | Type | Description |
|---|---|---|
| onInit | MethodWrapper<IScreen, Object, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnFailInit(catchInit)

| Parameter | Type | Description |
|---|---|---|
| catchInit | MethodWrapper<String, Object, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .setOnClose(onClose)

| Parameter | Type | Description |
|---|---|---|
| onClose | MethodWrapper<IScreen, Object, Object, ?> |  |

##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .reloadScreen()


##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .buttonBuilder()


##### Returns: [ButtonWidgetHelper$ButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.ButtonBuilder.html)



#### .checkBoxBuilder()


##### Returns: [CheckBoxWidgetHelper$CheckBoxBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.CheckBoxBuilder.html)



#### .checkBoxBuilder(checked)

| Parameter | Type | Description |
|---|---|---|
| checked | boolean |  |

##### Returns: [CheckBoxWidgetHelper$CheckBoxBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.CheckBoxBuilder.html)



#### .cyclicButtonBuilder(valueToText)

| Parameter | Type | Description |
|---|---|---|
| valueToText | MethodWrapper<Object, ?, TextHelper, ?> |  |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.CyclicButtonBuilder.html)< ? >



#### .lockButtonBuilder()


##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.LockButtonBuilder.html)



#### .lockButtonBuilder(locked)

| Parameter | Type | Description |
|---|---|---|
| locked | boolean |  |

##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.LockButtonBuilder.html)



#### .sliderBuilder()


##### Returns: [SliderWidgetHelper$SliderBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.SliderBuilder.html)



#### .textFieldBuilder()


##### Returns: [TextFieldWidgetHelper$TextFieldBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.TextFieldBuilder.html)



#### .texturedButtonBuilder()


##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.TexturedButtonBuilder.html)



#### .jsmacros\_render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .jsmacros\_mouseClicked(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: void



#### .jsmacros\_mouseDragged(mouseX, mouseY, button, deltaX, deltaY)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |
| deltaX | double |  |
| deltaY | double |  |

##### Returns: void



#### .jsmacros\_mouseReleased(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: void



#### .jsmacros\_keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: void



#### .jsmacros\_charTyped(chr, modifiers)

| Parameter | Type | Description |
|---|---|---|
| chr | char |  |
| modifiers | int |  |

##### Returns: void



#### .jsmacros\_mouseScrolled(mouseX, mouseY, horiz, vert)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| horiz | double |  |
| vert | double |  |

##### Returns: void



#### .handleCustomClickEvent(style, cir)

| Parameter | Type | Description |
|---|---|---|
| style | Style |  |
| cir | CallbackInfoReturnable<Boolean> |  |

##### Returns: void



#### .getOnClose()


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >




