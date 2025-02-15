

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper$ControlOptionsHelper
------------------------------------------------------------------------------

#### 

### Constructors

#### new OptionsHelper$ControlOptionsHelper (OptionsHelper)

| Parameter | Type | Description |
|---|---|---|
| OptionsHelper | OptionsHelper |  |



#### Fields

[parent](#parent)
F



#### Methods

[getParent()](#getParent-)


[getMouseSensitivity()](#getMouseSensitivity-)


[setMouseSensitivity(val)](#setMouseSensitivity-double-)


[isMouseInverted()](#isMouseInverted-)


[invertMouse(val)](#invertMouse-boolean-)


[getMouseWheelSensitivity()](#getMouseWheelSensitivity-)


[setMouseWheelSensitivity(val)](#setMouseWheelSensitivity-double-)


[isDiscreteScrollingEnabled()](#isDiscreteScrollingEnabled-)


[enableDiscreteScrolling(val)](#enableDiscreteScrolling-boolean-)


[isTouchscreenEnabled()](#isTouchscreenEnabled-)


[enableTouchscreen(val)](#enableTouchscreen-boolean-)


[isRawMouseInputEnabled()](#isRawMouseInputEnabled-)


[enableRawMouseInput(val)](#enableRawMouseInput-boolean-)


[isAutoJumpEnabled()](#isAutoJumpEnabled-)


[enableAutoJump(val)](#enableAutoJump-boolean-)


[isSneakTogglingEnabled()](#isSneakTogglingEnabled-)


[toggleSneak(val)](#toggleSneak-boolean-)


[isSprintTogglingEnabled()](#isSprintTogglingEnabled-)


[toggleSprint(val)](#toggleSprint-boolean-)


[getRawKeys()](#getRawKeys-)


[getCategories()](#getCategories-)


[getKeys()](#getKeys-)


[getKeyBinds()](#getKeyBinds-)


[getKeyBindsByCategory(category)](#getKeyBindsByCategory-String-)


[getKeyBindsByCategory()](#getKeyBindsByCategory-)



### Fields

#### .parent

Final

##### Type: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)



### Methods

#### .getParent()

1.8.4


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

the parent options helper.



#### .getMouseSensitivity()

1.8.4


##### Returns: double

the current mouse sensitivity.



#### .setMouseSensitivity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new mouse sensitivity |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isMouseInverted()

1.8.4


##### Returns: boolean

`true` if the mouse direction should be inverted.



#### .invertMouse(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to invert the mouse direction or not |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .getMouseWheelSensitivity()

1.8.4


##### Returns: double

the current mouse wheel sensitivity.



#### .setMouseWheelSensitivity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new mouse wheel sensitivity |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isDiscreteScrollingEnabled()

1.8.4

This option was introduced due to a bug on some systems where the mouse wheel would
scroll too fast.


##### Returns: boolean

`true` if discrete scrolling is enabled, `false` otherwise.



#### .enableDiscreteScrolling(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable discrete scrolling or not |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isTouchscreenEnabled()

1.8.4


##### Returns: boolean

`true` if touchscreen mode is enabled, `false` otherwise.



#### .enableTouchscreen(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable touchscreen mode or not |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isRawMouseInputEnabled()

1.8.4

Raw input is directly reading the mouse data, without any adjustments due to other
programs or the operating system.


##### Returns: boolean

`true` if raw mouse input is enabled, `false` otherwise.



#### .enableRawMouseInput(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable raw mouse input or not |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isAutoJumpEnabled()

1.8.4


##### Returns: boolean

`true` if auto jump is enabled, `false` otherwise.



#### .enableAutoJump(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable auto jump or not or not |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isSneakTogglingEnabled()

1.8.4


##### Returns: boolean

`true` if the toggle functionality for sneaking is enabled, `false`
otherwise.



#### .toggleSneak(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable or disable the toggle functionality for sneaking |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .isSprintTogglingEnabled()

1.8.4


##### Returns: boolean

`true` if the toggle functionality for sprinting is enabled, `false`
otherwise.



#### .toggleSprint(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable or disable the toggle functionality for sprinting |

##### Returns: [OptionsHelper$ControlOptionsHelper](#)

self for chaining.



#### .getRawKeys()

1.8.4


##### Returns: [KeyBinding](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/option/KeyBinding)[]

an array of all raw minecraft keybindings.



#### .getCategories()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all keybinding categories.



#### .getKeys()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all key names.



#### .getKeyBinds()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a map of all keybindings and their bound key.



#### .getKeyBindsByCategory(category)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| category | String | the category to get keybindings from |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a map of all keybindings and their bound key in the specified category.



#### .getKeyBindsByCategory()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>

a map of all keybinding categories, containing a map of all keybindings in that
category and their bound key.




