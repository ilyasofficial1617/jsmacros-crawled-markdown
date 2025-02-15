

xyz.wagyourtail.jsmacros.client.api.helpers.screen.LockButtonWidgetHelper$LockButtonBuilder
-------------------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[LockButtonWidgetHelper$LockButtonBuilder](#), [LockButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/LockButtonWidget), [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)>

1.8.4

### Constructors

#### new LockButtonWidgetHelper$LockButtonBuilder (screen)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |



#### Methods

[isLocked()](#isLocked-)


[locked(locked)](#locked-boolean-)


[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[createWidget()](#createWidget-)



### Methods

#### .isLocked()

1.8.4


##### Returns: boolean

the initial state of the lock button.



#### .locked(locked)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| locked | boolean | whether to initially lock the button or not |

##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](#)

self for chaining.



#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html), [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the action to run when the button is pressed.



#### .action(action)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<LockButtonWidgetHelper, IScreen, Object, ?> | the action to run when the button is pressed |

##### Returns: [LockButtonWidgetHelper$LockButtonBuilder](#)

self for chaining.



#### .createWidget()


##### Returns: [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html)




