

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.boss.EnderDragonEntityHelper
-------------------------------------------------------------------------------------------------

#### extends [MobEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/MobEntityHelper.html)<[EnderDragonEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/boss/dragon/EnderDragonEntity)>

1.8.4

### Constructors

#### new EnderDragonEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | EnderDragonEntity |  |



#### Methods

[getPhase()](#getPhase-)


[getBodyPart(index)](#getBodyPart-int-)


[getBodyParts()](#getBodyParts-)


[getBodyParts(name)](#getBodyParts-String-)



### Methods

#### .getPhase()

1.8.4

The phases are as follows:

`HoldingPattern`, `StrafePlayer`, `LandingApproach`, `Landing`,
`Takeoff`, `SittingFlaming`, `SittingScanning`, `SittingAttacking`,
`ChargingPlayer`, `Dying`, `Hover`


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current phase of the dragon.



#### .getBodyPart(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index of the dragon's body part to get |

##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

the specified body part of the dragon.



#### .getBodyParts()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< ? >

a list of all body parts of the dragon.



#### .getBodyParts(name)

1.8.4

The name can be either `head`, `neck`, `body`, `tail` or
`wing`.

| Parameter | Type | Description |
|---|---|---|
| name | String | the name of the body part to get |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< ? >

a list of all body parts of the dragon with the specified name.




