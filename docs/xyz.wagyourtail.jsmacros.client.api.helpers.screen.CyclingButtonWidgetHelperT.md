

xyz.wagyourtail.jsmacros.client.api.helpers.screen.CyclingButtonWidgetHelper< T >
---------------------------------------------------------------------------------

#### extends [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)<[CyclingButtonWidgetHelper](#)< T >, [CyclingButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/CyclingButtonWidget)< T >>

1.8.4

### Constructors

#### new CyclingButtonWidgetHelper (btn)

| Parameter | Type | Description |
|---|---|---|
| btn | CyclingButtonWidget<T> |  |


#### new CyclingButtonWidgetHelper (btn, zIndex)

| Parameter | Type | Description |
|---|---|---|
| btn | CyclingButtonWidget<T> |  |
| zIndex | int |  |



#### Methods

[getValue()](#getValue-)


[getStringValue()](#getStringValue-)


[setValue(val)](#setValue-T-)


[cycle(amount)](#cycle-int-)


[forward()](#forward-)


[backward()](#backward-)


[toString()](#toString-)



### Methods

#### .getValue()

1.8.4


##### Returns: T

the current value.



#### .getStringValue()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current value in their string representation.



#### .setValue(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | T | the new value |

##### Returns: boolean

`true` if the value has changed, `false` otherwise.



#### .cycle(amount)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| amount | int | the amount to cycle by |

##### Returns: [CyclingButtonWidgetHelper](#)< T >

self for chaining.



#### .forward()

1.8.4


##### Returns: [CyclingButtonWidgetHelper](#)< T >

self for chaining.



#### .backward()

1.8.4


##### Returns: [CyclingButtonWidgetHelper](#)< T >

self for chaining.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




