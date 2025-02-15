

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.boss.WitherEntityHelper
--------------------------------------------------------------------------------------------

#### extends [MobEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/MobEntityHelper.html)<[WitherEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/boss/WitherEntity)>

1.8.4

### Constructors

#### new WitherEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | WitherEntity |  |



#### Methods

[getRemainingInvulnerableTime()](#getRemainingInvulnerableTime-)


[isInvulnerable()](#isInvulnerable-)


[isFirstPhase()](#isFirstPhase-)


[isSecondPhase()](#isSecondPhase-)



### Methods

#### .getRemainingInvulnerableTime()

1.8.4


##### Returns: int

the time in ticks the wither will be invulnerable for.



#### .isInvulnerable()

1.8.4

The wither will only be invulnerable, by default for 220 ticks, when summoned.


##### Returns: boolean

`true` if the wither is invulnerable, `false` otherwise.



#### .isFirstPhase()

1.8.4


##### Returns: boolean

`true` if the wither is in its first phase, `false` otherwise.



#### .isSecondPhase()

1.8.4

In the second phase the wither will be invulnerable to projectiles and starts going down
towards the player.


##### Returns: boolean

`true` if the wither is in its second phase, `false` otherwise.




