

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.mob.CreeperEntityHelper
--------------------------------------------------------------------------------------------

#### extends [MobEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/MobEntityHelper.html)<[CreeperEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/mob/CreeperEntity)>

1.8.4

### Constructors

#### new CreeperEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | CreeperEntity |  |



#### Methods

[isCharged()](#isCharged-)


[isIgnited()](#isIgnited-)


[getFuseChange()](#getFuseChange-)


[getFuseTime()](#getFuseTime-)


[getMaxFuseTime()](#getMaxFuseTime-)


[getRemainingFuseTime()](#getRemainingFuseTime-)



### Methods

#### .isCharged()

1.8.4


##### Returns: boolean

`true` if the creeper is charged, `false` otherwise.



#### .isIgnited()

1.8.4


##### Returns: boolean

`true` if the creeper has been ignited, `false` otherwise.



#### .getFuseChange()

1.8.4

A negative value means the creeper is currently defusing, while a positive value means the
creeper is currently charging up.


##### Returns: int

the change in fuse every tick.



#### .getFuseTime()

1.8.4


##### Returns: int

the time the creeper has been charging up.



#### .getMaxFuseTime()

1.8.4


##### Returns: int

the maximum time the creeper can be charged for before exploding.



#### .getRemainingFuseTime()

1.8.4


##### Returns: int

the remaining time until the creeper explodes with the current fuse time, or
`-1` if the creeper is not about to explode.




