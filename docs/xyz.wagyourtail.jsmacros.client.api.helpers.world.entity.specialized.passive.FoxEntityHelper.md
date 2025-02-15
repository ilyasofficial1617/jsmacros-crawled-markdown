

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.passive.FoxEntityHelper
--------------------------------------------------------------------------------------------

#### extends [AnimalEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/specialized/passive/AnimalEntityHelper.html)<[FoxEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/passive/FoxEntity)>

1.8.4

### Constructors

#### new FoxEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | FoxEntity |  |



#### Methods

[getItemInMouth()](#getItemInMouth-)


[isSnowFox()](#isSnowFox-)


[isRedFox()](#isRedFox-)


[getOwner()](#getOwner-)


[getSecondOwner()](#getSecondOwner-)


[canTrust(entity)](#canTrust-EntityHelper-)


[hasFoundTarget()](#hasFoundTarget-)


[isSitting()](#isSitting-)


[isWandering()](#isWandering-)


[isSleeping()](#isSleeping-)


[isDefending()](#isDefending-)


[isPouncing()](#isPouncing-)


[isJumping()](#isJumping-)


[isSneaking()](#isSneaking-)



### Methods

#### .getItemInMouth()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the item in this fox's mouth.



#### .isSnowFox()

1.8.4


##### Returns: boolean

`true` if this fox is a snow fox, `false` otherwise.



#### .isRedFox()

1.8.4


##### Returns: boolean

`true` if this fox is a red fox, `false` otherwise.



#### .getOwner()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the owner's UUID, or `null` if this fox has no owner.



#### .getSecondOwner()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the second owner's name, or `null` if this fox has no owner.



#### .canTrust(entity)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> | the entity to check |

##### Returns: boolean

`true` if this fox trusts the given entity, `false` otherwise.



#### .hasFoundTarget()

1.8.4


##### Returns: boolean

`true` if this fox is preparing its jump, `false` otherwise.



#### .isSitting()

1.8.4


##### Returns: boolean

`true` if this fox is sitting, `false` otherwise.



#### .isWandering()

1.8.4


##### Returns: boolean

`true` if this fox is wandering around, `false` otherwise.



#### .isSleeping()

1.8.4


##### Returns: boolean

`true` if this fox is sleeping, `false` otherwise.



#### .isDefending()

1.8.4


##### Returns: boolean

`true` if this fox is defending another fox, `false` otherwise.



#### .isPouncing()

1.8.4


##### Returns: boolean

`true` if this fox is just before its leap, `false` otherwise.



#### .isJumping()

1.8.4


##### Returns: boolean

`true` if this fox is jumping, `false` otherwise.



#### .isSneaking()

1.8.4


##### Returns: boolean

`true` if this fox is sneaking in preparation of an attack, `false`
otherwise.




