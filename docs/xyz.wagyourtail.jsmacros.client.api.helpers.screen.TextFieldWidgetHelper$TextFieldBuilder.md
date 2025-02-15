

xyz.wagyourtail.jsmacros.client.api.helpers.screen.TextFieldWidgetHelper$TextFieldBuilder
-----------------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[TextFieldWidgetHelper$TextFieldBuilder](#), [TextFieldWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/TextFieldWidget), [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)>

1.8.4

### Constructors

#### new TextFieldWidgetHelper$TextFieldBuilder (screen, textRenderer)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |
| textRenderer | TextRenderer |  |



#### Methods

[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[getSuggestion()](#getSuggestion-)


[suggestion(suggestion)](#suggestion-String-)


[createWidget()](#createWidget-)



### Methods

#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the callback for when the text is changed.



#### .action(action)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<String, IScreen, Object, ?> | the callback for when the text is changed |

##### Returns: [TextFieldWidgetHelper$TextFieldBuilder](#)

self for chaining.



#### .getSuggestion()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current suggestion.



#### .suggestion(suggestion)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestion | String | the suggestion to use |

##### Returns: [TextFieldWidgetHelper$TextFieldBuilder](#)

self for chaining.



#### .createWidget()


##### Returns: [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html)




