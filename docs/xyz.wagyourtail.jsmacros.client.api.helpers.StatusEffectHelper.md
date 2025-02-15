

xyz.wagyourtail.jsmacros.client.api.helpers.StatusEffectHelper
--------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[StatusEffectInstance](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/effect/StatusEffectInstance)>

1.2.4

### Constructors

#### new StatusEffectHelper (s)

| Parameter | Type | Description |
|---|---|---|
| s | StatusEffectInstance |  |


#### new StatusEffectHelper (s)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| s | StatusEffect |  |


#### new StatusEffectHelper (s, t)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| s | StatusEffect |  |
| t | int |  |



#### Methods

[getId()](#getId-)


[getStrength()](#getStrength-)


[getCategory()](#getCategory-)


[getTime()](#getTime-)


[isPermanent()](#isPermanent-)


[isAmbient()](#isAmbient-)


[hasIcon()](#hasIcon-)


[isVisible()](#isVisible-)


[isInstant()](#isInstant-)


[isBeneficial()](#isBeneficial-)


[isNeutral()](#isNeutral-)


[isHarmful()](#isHarmful-)


[toString()](#toString-)



### Methods

#### .getId()

1.2.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getStrength()

1.2.4


##### Returns: int



#### .getCategory()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the string name of the category of the status effect, "HARMFUL", "NEUTRAL", or "BENEFICIAL".



#### .getTime()

1.2.4


##### Returns: int



#### .isPermanent()

1.8.4


##### Returns: boolean

`true` if this effect is applied permanently, `false` otherwise.



#### .isAmbient()

1.8.4

Ambient effects are usually applied through beacons and they make the particles more
translucent.


##### Returns: boolean

`true` if this effect is an ambient one, `false` otherwise.



#### .hasIcon()

1.8.4


##### Returns: boolean

`true` if this effect has an icon it should render, `false` otherwise.



#### .isVisible()

1.8.4


##### Returns: boolean

`true` if this effect affects the particle color and gets rendered in game,
`false` otherwise.



#### .isInstant()

1.8.4

An effect which is instant can still have a duration, but only if it's set through a
command.


##### Returns: boolean

`true` if this effect should be applied instantly, `false` otherwise.



#### .isBeneficial()

1.8.4


##### Returns: boolean

`true` if this effect is considered beneficial, `false` otherwise.



#### .isNeutral()

1.8.4


##### Returns: boolean

`true` if this effect is considered neutral, `false` otherwise.



#### .isHarmful()

1.8.4


##### Returns: boolean

`true` if this effect is considered harmful, `false` otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




