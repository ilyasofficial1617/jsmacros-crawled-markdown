

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.projectile.ArrowEntityHelper
-------------------------------------------------------------------------------------------------

#### extends [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)<[PersistentProjectileEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/projectile/PersistentProjectileEntity)>

1.8.4

### Constructors

#### new ArrowEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | PersistentProjectileEntity |  |



#### Methods

[getColor()](#getColor-)


[isCritical()](#isCritical-)


[getPiercingLevel()](#getPiercingLevel-)


[isShotFromCrossbow()](#isShotFromCrossbow-)



### Methods

#### .getColor()

1.8.4


##### Returns: int

the particle's color of the arrow, or `-1` if the arrow has no particles.



#### .isCritical()

1.8.4


##### Returns: boolean

`true` if the arrow will deal critical damage, `false` otherwise.



#### .getPiercingLevel()

1.8.4

The piercing level will only be set if the arrow was fired from a crossbow with the piercing
enchantment.


##### Returns: int

the piercing level of the arrow.



#### .isShotFromCrossbow()

1.8.4


##### Returns: boolean

`true` if the arrow is shot from a crossbow, `false` otherwise.




