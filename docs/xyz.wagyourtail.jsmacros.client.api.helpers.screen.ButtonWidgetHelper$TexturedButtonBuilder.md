

xyz.wagyourtail.jsmacros.client.api.helpers.screen.ButtonWidgetHelper$TexturedButtonBuilder
-------------------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[ButtonWidgetHelper$TexturedButtonBuilder](#), [TexturedButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TexturedButtonWidget), [ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[TexturedButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TexturedButtonWidget)>>

1.8.4

### Constructors

#### new ButtonWidgetHelper$TexturedButtonBuilder (screen)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |



#### Methods

[height(height)](#height-int-)


[size(width, height)](#size-int-int-)


[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[enabledTexture(enabled)](#enabledTexture-Identifier-)


[disabledTexture(disabled)](#disabledTexture-Identifier-)


[enabledFocusedTexture(enabledFocused)](#enabledFocusedTexture-Identifier-)


[disabledFocusedTexture(disabledFocused)](#disabledFocusedTexture-Identifier-)


[createWidget()](#createWidget-)



### Methods

#### .height(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | int | this argument is ignored and will always be set to 20 |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .size(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the button |
| height | int | this argument is ignored and will always be set to 20 |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[TexturedButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TexturedButtonWidget)>, [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the action to run when the button is pressed.



#### .action(action)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<ButtonWidgetHelper<TexturedButtonWidget>, IScreen, Object, ?> | the action to run when the button is pressed |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .enabledTexture(enabled)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| enabled | Identifier |  |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .disabledTexture(disabled)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| disabled | Identifier |  |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .enabledFocusedTexture(enabledFocused)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| enabledFocused | Identifier |  |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .disabledFocusedTexture(disabledFocused)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| disabledFocused | Identifier |  |

##### Returns: [ButtonWidgetHelper$TexturedButtonBuilder](#)

self for chaining.



#### .createWidget()


##### Returns: [ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<[TexturedButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TexturedButtonWidget)>




