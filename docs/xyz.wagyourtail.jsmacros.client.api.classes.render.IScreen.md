
[MixinScreen](1.9.2/xyz/wagyourtail/jsmacros/client/mixins/access/MixinScreen.html)

xyz.wagyourtail.jsmacros.client.api.classes.render.IScreen
----------------------------------------------------------

Interface
#### implements [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)<[IScreen](#)>

1.2.7

#### Methods

[getScreenClassName()](#getScreenClassName-)


[getTitleText()](#getTitleText-)


[getButtonWidgets()](#getButtonWidgets-)


[getTextFields()](#getTextFields-)


[addButton(x, y, width, height, text, callback)](#addButton-int-int-int-int-String-MethodWrapper-)


[addButton(x, y, width, height, zIndex, text, callback)](#addButton-int-int-int-int-int-String-MethodWrapper-)


[addCheckbox(x, y, width, height, text, checked, showMessage, callback)](#addCheckbox-int-int-int-int-String-boolean-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, text, checked, callback)](#addCheckbox-int-int-int-int-String-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, zIndex, text, checked, callback)](#addCheckbox-int-int-int-int-int-String-boolean-MethodWrapper-)


[addCheckbox(x, y, width, height, zIndex, text, checked, showMessage, callback)](#addCheckbox-int-int-int-int-int-String-boolean-boolean-MethodWrapper-)


[addSlider(x, y, width, height, text, value, steps, callback)](#addSlider-int-int-int-int-String-double-int-MethodWrapper-)


[addSlider(x, y, width, height, zIndex, text, value, steps, callback)](#addSlider-int-int-int-int-int-String-double-int-MethodWrapper-)


[addSlider(x, y, width, height, text, value, callback)](#addSlider-int-int-int-int-String-double-MethodWrapper-)


[addSlider(x, y, width, height, zIndex, text, value, callback)](#addSlider-int-int-int-int-int-String-double-MethodWrapper-)


[addLockButton(x, y, callback)](#addLockButton-int-int-MethodWrapper-)


[addLockButton(x, y, zIndex, callback)](#addLockButton-int-int-int-MethodWrapper-)


[addCyclingButton(x, y, width, height, values, initial, callback)](#addCyclingButton-int-int-int-int-String[]-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, initial, callback)](#addCyclingButton-int-int-int-int-int-String[]-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, callback)](#addCyclingButton-int-int-int-int-int-String[]-String[]-String-String-MethodWrapper-)


[addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, alternateToggle, callback)](#addCyclingButton-int-int-int-int-int-String[]-String[]-String-String-MethodWrapper-MethodWrapper-)


[removeButton(btn)](#removeButton-ClickableWidgetHelper-)
D


[addTextInput(x, y, width, height, message, onChange)](#addTextInput-int-int-int-int-String-MethodWrapper-)


[addTextInput(x, y, width, height, zIndex, message, onChange)](#addTextInput-int-int-int-int-int-String-MethodWrapper-)


[removeTextInput(inp)](#removeTextInput-TextFieldWidgetHelper-)
D


[setOnMouseDown(onMouseDown)](#setOnMouseDown-MethodWrapper-)


[setOnMouseDrag(onMouseDrag)](#setOnMouseDrag-MethodWrapper-)


[setOnMouseUp(onMouseUp)](#setOnMouseUp-MethodWrapper-)


[setOnScroll(onScroll)](#setOnScroll-MethodWrapper-)


[setOnKeyPressed(onKeyPressed)](#setOnKeyPressed-MethodWrapper-)


[setOnCharTyped(onCharTyped)](#setOnCharTyped-MethodWrapper-)


[setOnClose(onClose)](#setOnClose-MethodWrapper-)


[close()](#close-)


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


[isShiftDown()](#isShiftDown-)


[isCtrlDown()](#isCtrlDown-)


[isAltDown()](#isAltDown-)


[getOnClose()](#getOnClose-)



### Methods

#### .getScreenClassName()

1.2.7


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getTitleText()

1.0.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getButtonWidgets()

1.0.5

in `1.3.1` updated to work with all button widgets not just ones added by scripts.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >>



#### .getTextFields()

1.0.5

in `1.3.1` updated to work with all text fields not just ones added by scripts.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)>



#### .addButton(x, y, width, height, text, callback)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| text | String |  |
| callback | MethodWrapper<ClickableWidgetHelper<?, ?>, IScreen, Object, ?> | calls your method as a Consumer<ClickableWidgetHelper> |

##### Returns: [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >



#### .addButton(x, y, width, height, zIndex, text, callback)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| text | String |  |
| callback | MethodWrapper<ClickableWidgetHelper<?, ?>, IScreen, Object, ?> | calls your method as a Consumer<ClickableWidgetHelper> |

##### Returns: [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)< ? , ? >



#### .addCheckbox(x, y, width, height, text, checked, showMessage, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the checkbox |
| y | int | the y position of the checkbox |
| width | int | the width of the checkbox |
| height | int | the height of the checkbox |
| text | String | the text to display next to the checkbox |
| checked | boolean | whether the checkbox is checked or not |
| showMessage | boolean | whether to show the message or not |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> | calls your method as a
                                            Consumer<CheckBoxWidgetHelper> |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)

a [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html) for the given input.



#### .addCheckbox(x, y, width, height, text, checked, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the checkbox |
| y | int | the y position of the checkbox |
| width | int | the width of the checkbox |
| height | int | the height of the checkbox |
| text | String | the text to display next to the checkbox |
| checked | boolean | whether the checkbox is checked or not |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<CheckBoxWidgetHelper> |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)

a [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html) for the given input.



#### .addCheckbox(x, y, width, height, zIndex, text, checked, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the checkbox |
| y | int | the y position of the checkbox |
| width | int | the width of the checkbox |
| height | int | the height of the checkbox |
| zIndex | int | the z-index of the checkbox |
| text | String | the text to display next to the checkbox |
| checked | boolean | whether the checkbox is checked or not |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<CheckBoxWidgetHelper> |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)

a [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html) for the given input.



#### .addCheckbox(x, y, width, height, zIndex, text, checked, showMessage, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the checkbox |
| y | int | the y position of the checkbox |
| width | int | the width of the checkbox |
| height | int | the height of the checkbox |
| zIndex | int | the z-index of the checkbox |
| text | String | the text to display next to the checkbox |
| checked | boolean | whether the checkbox is checked or not |
| showMessage | boolean | whether to show the message or not |
| callback | MethodWrapper<CheckBoxWidgetHelper, IScreen, Object, ?> | calls your method as a
                                            Consumer<CheckBoxWidgetHelper> |

##### Returns: [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html)

a [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html) for the given input.



#### .addSlider(x, y, width, height, text, value, steps, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the slider |
| y | int | the y position of the slider |
| width | int | the width of the slider |
| height | int | the height of the slider |
| text | String | the text to be displayed inside the slider |
| value | double | the initial value of the slider |
| steps | int | the number of steps the slider should have |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<SliderWidgetHelper> |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)

a [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html) for the given input.



#### .addSlider(x, y, width, height, zIndex, text, value, steps, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the slider |
| y | int | the y position of the slider |
| width | int | the width of the slider |
| height | int | the height of the slider |
| zIndex | int | the z-index of the slider |
| text | String | the text to be displayed inside the slider |
| value | double | the initial value of the slider |
| steps | int | the number of steps the slider should have |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<SliderWidgetHelper> |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)

a [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html) for the given input.



#### .addSlider(x, y, width, height, text, value, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the slider |
| y | int | the y position of the slider |
| width | int | the width of the slider |
| height | int | the height of the slider |
| text | String | the text to be displayed inside the slider |
| value | double | the initial value of the slider |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<SliderWidgetHelper> |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)

a [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html) for the given input.



#### .addSlider(x, y, width, height, zIndex, text, value, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the slider |
| y | int | the y position of the slider |
| width | int | the width of the slider |
| height | int | the height of the slider |
| zIndex | int | the z-index of the slider |
| text | String | the text to be displayed inside the slider |
| value | double | the initial value of the slider |
| callback | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> | calls your method as a Consumer<SliderWidgetHelper> |

##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)

a [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html) for the given input.



#### .addLockButton(x, y, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the lock button |
| y | int | the y position of the lock button |
| callback | MethodWrapper<LockButtonWidgetHelper, IScreen, Object, ?> | calls your method as a
                                         Consumer<LockButtonWidgetHelper> |

##### Returns: [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)

[LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html) for the given input.



#### .addLockButton(x, y, zIndex, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the lock button |
| y | int | the y position of the lock button |
| zIndex | int | the z-index of the lock button |
| callback | MethodWrapper<LockButtonWidgetHelper, IScreen, Object, ?> | calls your method as a
                                         Consumer<LockButtonWidgetHelper> |

##### Returns: [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)

[LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html) for the given input.



#### .addCyclingButton(x, y, width, height, values, initial, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the cycling button |
| y | int | the y position of the cycling button |
| width | int | the width of the cycling button |
| height | int | the height of the cycling button |
| values | String[] | the values to cycle through |
| initial | String | the initial value of the cycling button |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> | calls your method as a
                                         Consumer<CyclingButtonWidgetHelper> |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >

[CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html) for the given input.



#### .addCyclingButton(x, y, width, height, zIndex, values, initial, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the cycling button |
| y | int | the y position of the cycling button |
| width | int | the width of the cycling button |
| height | int | the height of the cycling button |
| zIndex | int | the z-index of the cycling button |
| values | String[] | the values to cycle through |
| initial | String | the initial value of the cycling button |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> | calls your method as a
                                         Consumer<CyclingButtonWidgetHelper> |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >

[CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html) for the given input.



#### .addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the cycling button |
| y | int | the y position of the cycling button |
| width | int | the width of the cycling button |
| height | int | the height of the cycling button |
| zIndex | int | the z-index of the cycling button |
| values | String[] | the values to cycle through |
| alternatives | String[] | the alternative values to cycle through |
| initial | String | the initial value of the cycling button |
| prefix | String | the prefix of the values |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> | calls your method as a
                                             Consumer<CyclingButtonWidgetHelper> |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >

[CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html) for the given input.



#### .addCyclingButton(x, y, width, height, zIndex, values, alternatives, initial, prefix, alternateToggle, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the cycling button |
| y | int | the y position of the cycling button |
| width | int | the width of the cycling button |
| height | int | the height of the cycling button |
| zIndex | int | the z-index of the cycling button |
| values | String[] | the values to cycle through |
| alternatives | String[] | the alternative values to cycle through |
| initial | String | the initial value of the cycling button |
| prefix | String | the prefix of the values |
| alternateToggle | MethodWrapper<?, ?, Boolean, ?> | the method to determine if the cycling button should use the
                                                alternative values |
| callback | MethodWrapper<CyclingButtonWidgetHelper<?>, IScreen, Object, ?> | calls your method as a
                                                Consumer<CyclingButtonWidgetHelper> |

##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< ? >

[CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html) for the given input.



#### .removeButton(btn)

Deprecated

1.0.5

| Parameter | Type | Description |
|---|---|---|
| btn | ClickableWidgetHelper<?, ?> |  |

##### Returns: [IScreen](#)



#### .addTextInput(x, y, width, height, message, onChange)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| message | String |  |
| onChange | MethodWrapper<String, IScreen, Object, ?> | calls your method as a Consumer<String> |

##### Returns: [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)



#### .addTextInput(x, y, width, height, zIndex, message, onChange)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| zIndex | int |  |
| message | String |  |
| onChange | MethodWrapper<String, IScreen, Object, ?> | calls your method as a Consumer<String> |

##### Returns: [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)



#### .removeTextInput(inp)

Deprecated

1.0.5

| Parameter | Type | Description |
|---|---|---|
| inp | TextFieldWidgetHelper |  |

##### Returns: [IScreen](#)



#### .setOnMouseDown(onMouseDown)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onMouseDown | MethodWrapper<Pos2D, Integer, Object, ?> | calls your method as a BiConsumer<Pos2D, Integer> |

##### Returns: [IScreen](#)



#### .setOnMouseDrag(onMouseDrag)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onMouseDrag | MethodWrapper<Vec2D, Integer, Object, ?> | calls your method as a BiConsumer<Vec2D, Integer> |

##### Returns: [IScreen](#)



#### .setOnMouseUp(onMouseUp)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onMouseUp | MethodWrapper<Pos2D, Integer, Object, ?> | calls your method as a BiConsumer<Pos2D, Integer> |

##### Returns: [IScreen](#)



#### .setOnScroll(onScroll)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onScroll | MethodWrapper<Pos2D, Pos2D, Object, ?> | calls your method as a BiConsumer<Pos2D, Double> |

##### Returns: [IScreen](#)



#### .setOnKeyPressed(onKeyPressed)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onKeyPressed | MethodWrapper<Integer, Integer, Object, ?> | calls your method as a BiConsumer<Integer, Integer> |

##### Returns: [IScreen](#)



#### .setOnCharTyped(onCharTyped)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| onCharTyped | MethodWrapper<Character, Integer, Object, ?> | calls your method as a BiConsumer<Character, Integer> |

##### Returns: [IScreen](#)



#### .setOnClose(onClose)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| onClose | MethodWrapper<IScreen, Object, Object, ?> | calls your method as a Consumer<IScreen> |

##### Returns: [IScreen](#)



#### .close()

1.1.9


##### Returns: void



#### .reloadScreen()

1.2.7

calls the screen's init function re-loading it.


##### Returns: [IScreen](#)



#### .buttonBuilder()

1.8.4


##### Returns: [ButtonWidgetHelper$ButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.ButtonBuilder.html)

a new builder for buttons.



#### .checkBoxBuilder()

1.8.4


##### Returns: [CheckBoxWidgetHelper$CheckBoxBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.CheckBoxBuilder.html)

a new builder for checkboxes.



#### .checkBoxBuilder(checked)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| checked | boolean | whether the checkbox should be checked by default |

##### Returns: [CheckBoxWidgetHelper$CheckBoxBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.CheckBoxBuilder.html)

a new builder for checkboxes.



#### .cyclicButtonBuilder(valueToText)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| valueToText | MethodWrapper<Object, ?, TextHelper, ?> |  |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.CyclicButtonBuilder.html)< ? >

a new builder for cycling buttons.



#### .lockButtonBuilder()

1.8.4


##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.LockButtonBuilder.html)

a new builder for lock buttons.



#### .lockButtonBuilder(locked)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| locked | boolean | whether the lock button should be locked by default |

##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.LockButtonBuilder.html)

a new builder for lock buttons.



#### .sliderBuilder()

1.8.4


##### Returns: [SliderWidgetHelper$SliderBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.SliderBuilder.html)

a new builder for sliders.



#### .textFieldBuilder()

1.8.4


##### Returns: [TextFieldWidgetHelper$TextFieldBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.TextFieldBuilder.html)

a new builder for text fields.



#### .texturedButtonBuilder()

1.8.4


##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.TexturedButtonBuilder.html)

a new builder for textured buttons.



#### .isShiftDown()

1.8.4


##### Returns: boolean

`true` if the shift key is pressed, `false` otherwise.



#### .isCtrlDown()

1.8.4


##### Returns: boolean

`true` if the ctrl key is pressed, `false` otherwise.



#### .isAltDown()

1.8.4


##### Returns: boolean

`true` if the alt key is pressed, `false` otherwise.



#### .getOnClose()


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[IScreen](#), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >




