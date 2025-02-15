

xyz.wagyourtail.jsmacros.client.api.helpers.screen.SliderWidgetHelper$SliderBuilder
-----------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[SliderWidgetHelper$SliderBuilder](#), [Slider](1.9.2/xyz/wagyourtail/wagyourgui/elements/Slider.html), [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)>

1.8.4

### Constructors

#### new SliderWidgetHelper$SliderBuilder (screen)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |



#### Methods

[getSteps()](#getSteps-)


[steps(steps)](#steps-int-)


[getValue()](#getValue-)


[initially(value)](#initially-int-)


[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[createWidget()](#createWidget-)



### Methods

#### .getSteps()

1.8.4


##### Returns: int

the amount of steps of this slider.



#### .steps(steps)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| steps | int | the amount of steps for the slider. Must be greater or equal to 2 |

##### Returns: [SliderWidgetHelper$SliderBuilder](#)

self for chaining.



#### .getValue()

1.8.4


##### Returns: int

the initial value of the slider.



#### .initially(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the initial value of the slider. Must be between 0 and steps - 1 |

##### Returns: [SliderWidgetHelper$SliderBuilder](#)

self for chaining.



#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html), [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the change listener of the slider.



#### .action(action)

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<SliderWidgetHelper, IScreen, Object, ?> | the change listener for the slider |

##### Returns: [SliderWidgetHelper$SliderBuilder](#)

self for chaining.



#### .createWidget()


##### Returns: [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html)




