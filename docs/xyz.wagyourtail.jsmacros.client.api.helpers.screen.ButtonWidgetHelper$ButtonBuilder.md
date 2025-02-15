

xyz.wagyourtail.jsmacros.client.api.helpers.screen.ButtonWidgetHelper$ButtonBuilder
-----------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[ButtonWidgetHelper$ButtonBuilder](#), [ButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ButtonWidget), [ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[ButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ButtonWidget)>>

1.8.4

### Constructors

#### new ButtonWidgetHelper$ButtonBuilder (screen)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |



#### Methods

[height(height)](#height-int-)


[size(width, height)](#size-int-int-)


[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[createWidget()](#createWidget-)



### Methods

#### .height(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | this argument is ignored and will always be set to 20 |

##### Returns: [ButtonWidgetHelper$ButtonBuilder](#)

self for chaining.



#### .size(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the button |
| height | int | this argument is ignored and will always be set to 20 |

##### Returns: [ButtonWidgetHelper$ButtonBuilder](#)

self for chaining.



#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[ButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ButtonWidget)>, [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the action to run when the button is pressed.



#### .action(action)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<ButtonWidgetHelper<ButtonWidget>, IScreen, Object, ?> | the action to run when the button is pressed |

##### Returns: [ButtonWidgetHelper$ButtonBuilder](#)

self for chaining.



#### .createWidget()


##### Returns: [ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[ButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ButtonWidget)>




