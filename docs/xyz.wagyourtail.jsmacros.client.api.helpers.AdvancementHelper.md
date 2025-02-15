

xyz.wagyourtail.jsmacros.client.api.helpers.AdvancementHelper
-------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[PlacedAdvancement](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/advancement/PlacedAdvancement)>

1.8.4

### Constructors

#### new AdvancementHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | PlacedAdvancement |  |



#### Methods

[getParent()](#getParent-)


[getChildren()](#getChildren-)


[getRequirements()](#getRequirements-)


[getRequirementCount()](#getRequirementCount-)


[getId()](#getId-)


[getExperience()](#getExperience-)


[getLoot()](#getLoot-)


[getRecipes()](#getRecipes-)


[getProgress()](#getProgress-)


[toJson()](#toJson-)


[toString()](#toString-)



### Methods

#### .getParent()

1.8.4


##### Returns: [AdvancementHelper](#)

the parent advancement or `null` if there is none.



#### .getChildren()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](#)>

a list of all child advancements.



#### .getRequirements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>

the requirements of this advancement.



#### .getRequirementCount()

1.8.4


##### Returns: int

the amount of requirements.



#### .getId()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of this advancement.



#### .getExperience()

1.8.4


##### Returns: int

the experience awarded by this advancement.



#### .getLoot()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

the loot table ids for this advancement's rewards.



#### .getRecipes()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

the recipes unlocked through this advancement.



#### .getProgress()

1.8.4


##### Returns: [AdvancementProgressHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementProgressHelper.html)

the progress.



#### .toJson()

1.9.0


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the json string of this advancement.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




