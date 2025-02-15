

xyz.wagyourtail.jsmacros.client.api.helpers.screen.CyclingButtonWidgetHelper$CyclicButtonBuilder< T >
-----------------------------------------------------------------------------------------------------

Static
#### extends [AbstractWidgetBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/AbstractWidgetBuilder.html)<[CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >, [CyclingButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/CyclingButtonWidget)< T >, [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< T >>

1.8.4

### Constructors

#### new CyclingButtonWidgetHelper$CyclicButtonBuilder (screen, valueToText)

| Parameter | Type | Description |
|---|---|---|
| screen | IScreen |  |
| valueToText | MethodWrapper<T, ?, TextHelper, ?> |  |



#### Methods

[getInitialValue()](#getInitialValue-)


[initially(value)](#initially-T-)


[getOption()](#getOption-)


[option(option)](#option-String-)


[option(option)](#option-TextHelper-)


[getAction()](#getAction-)


[action(action)](#action-MethodWrapper-)


[getValueToText()](#getValueToText-)


[valueToText(valueToText)](#valueToText-MethodWrapper-)


[getDefaultValues()](#getDefaultValues-)


[getAlternateValues()](#getAlternateValues-)


[values(values)](#values-T[]-)
F


[alternatives(values)](#alternatives-T[]-)
F


[values(defaults, alternatives)](#values-T[]-T[]-)


[values(defaults, alternatives)](#values-List-List-)


[getAlternateToggle()](#getAlternateToggle-)


[alternateToggle(alternateToggle)](#alternateToggle-MethodWrapper-)


[isOptionTextOmitted()](#isOptionTextOmitted-)


[omitTextOption(optionTextOmitted)](#omitTextOption-boolean-)


[createWidget()](#createWidget-)



### Methods

#### .getInitialValue()

1.8.4


##### Returns: T

the initial value of the slider.



#### .initially(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | T | the initial value of the slider |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .getOption()

1.8.4

The option text is a prefix of all values, separated by a colon.


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the option text of the button or an empty text if it is omitted.



#### .option(option)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| option | String | the option text of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .option(option)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| option | TextHelper | the option text of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .getAction()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< T >, [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >

the action to run when the button is pressed.



#### .action(action)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<CyclingButtonWidgetHelper<T>, IScreen, Object, ?> | the action to run when the button is pressed |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .getValueToText()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , ? , [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html), ? >

the function to convert a value to a text.



#### .valueToText(valueToText)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| valueToText | MethodWrapper<T, ?, TextHelper, ?> | the function to convert a value to a text |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .getDefaultValues()

1.8.4

The button will normally cycle through the default values, but if the alternate toggle is
true, it will cycle through the alternate values.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< T >

the list of all default values.



#### .getAlternateValues()

1.8.4

The button will normally cycle through the default values, but if the alternate toggle is
true, it will cycle through the alternate values.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< T >

the list of all alternate values.



#### .values(values)

Final

1.8.4

| Parameter | Type | Description |
|---|---|---|
| values | T[] | the default values of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .alternatives(values)

Final

1.8.4

| Parameter | Type | Description |
|---|---|---|
| values | T[] | the alternate values of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .values(defaults, alternatives)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| defaults | T[] | the default values of the button |
| alternatives | T[] | the alternate values of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .values(defaults, alternatives)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| defaults | List<T> | the default values of the button |
| alternatives | List<T> | the alternate values of the button |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .getAlternateToggle()

1.8.4


##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< ? , ? , [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html), ? >

the toggle function to determine if the button should cycle through the default
or the alternate values.



#### .alternateToggle(alternateToggle)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alternateToggle | MethodWrapper<?, ?, Boolean, ?> | the toggle function to determine if the button should cycle
                                                through the default or the alternate values |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .isOptionTextOmitted()

1.8.4


##### Returns: boolean

`true` if the prefix option text should be omitted, `false`
otherwise.



#### .omitTextOption(optionTextOmitted)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| optionTextOmitted | boolean | whether the prefix option text should be omitted or not |

##### Returns: [CyclingButtonWidgetHelper$CyclicButtonBuilder](#)< T >

self for chaining.



#### .createWidget()


##### Returns: [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)< T >




