

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.FoodComponentHelper
-------------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[FoodComponent](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/component/type/FoodComponent)>

1.8.4

### Constructors

#### new FoodComponentHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | FoodComponent |  |



#### Methods

[getHunger()](#getHunger-)


[getSaturation()](#getSaturation-)


[isAlwaysEdible()](#isAlwaysEdible-)


[isFastFood()](#isFastFood-)


[getStatusEffects()](#getStatusEffects-)


[toString()](#toString-)



### Methods

#### .getHunger()

1.8.4


##### Returns: int

the amount of hunger this food restores.



#### .getSaturation()

1.8.4


##### Returns: float

the amount of saturation this food restores.



#### .isAlwaysEdible()

1.8.4


##### Returns: boolean

`true` if this food can be eaten even when the player is not hungry,
`false` otherwise.



#### .isFastFood()

1.8.4


##### Returns: boolean

`true` if the food can be eaten faster than usual, `false` otherwise.



#### .getStatusEffects()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[StatusEffectHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatusEffectHelper.html), [Float](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Float.html)>

a map of status effects and their respective probabilities.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




