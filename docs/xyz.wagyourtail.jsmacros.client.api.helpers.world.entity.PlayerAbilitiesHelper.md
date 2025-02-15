

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.PlayerAbilitiesHelper
------------------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[PlayerAbilities](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/player/PlayerAbilities)>

1.0.3

### Constructors

#### new PlayerAbilitiesHelper (a)

| Parameter | Type | Description |
|---|---|---|
| a | PlayerAbilities |  |



#### Methods

[getInvulnerable()](#getInvulnerable-)


[getFlying()](#getFlying-)


[getAllowFlying()](#getAllowFlying-)


[getCreativeMode()](#getCreativeMode-)


[canModifyWorld()](#canModifyWorld-)


[setFlying(b)](#setFlying-boolean-)


[setAllowFlying(b)](#setAllowFlying-boolean-)


[getFlySpeed()](#getFlySpeed-)


[setFlySpeed(flySpeed)](#setFlySpeed-double-)


[getWalkSpeed()](#getWalkSpeed-)


[setWalkSpeed(speed)](#setWalkSpeed-double-)


[toString()](#toString-)



### Methods

#### .getInvulnerable()

1.0.3


##### Returns: boolean

whether the player can be damaged.



#### .getFlying()

1.0.3


##### Returns: boolean

if the player is currently flying.



#### .getAllowFlying()

1.0.3


##### Returns: boolean

if the player is allowed to fly.



#### .getCreativeMode()

1.0.3


##### Returns: boolean

if the player is in creative.



#### .canModifyWorld()

1.8.4

Even if this method returns true, the player may not be able to modify the world due to other
restrictions such as plugins and mods. Modifying the world includes, placing, breaking or
interacting with blocks.


##### Returns: boolean

`true` if the player is allowed to modify the world, `false` otherwise.



#### .setFlying(b)

1.0.3

set the player flying state.

| Parameter | Type | Description |
|---|---|---|
| b | boolean |  |

##### Returns: [PlayerAbilitiesHelper](#)



#### .setAllowFlying(b)

1.0.3

set the player allow flying state.

| Parameter | Type | Description |
|---|---|---|
| b | boolean |  |

##### Returns: [PlayerAbilitiesHelper](#)



#### .getFlySpeed()

1.0.3


##### Returns: float

the player fly speed multiplier.



#### .setFlySpeed(flySpeed)

1.0.3

set the player fly speed multiplier.

| Parameter | Type | Description |
|---|---|---|
| flySpeed | double |  |

##### Returns: [PlayerAbilitiesHelper](#)



#### .getWalkSpeed()

1.8.4


##### Returns: float

the player's walk speed.



#### .setWalkSpeed(speed)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| speed | double | the new walk speed |

##### Returns: [PlayerAbilitiesHelper](#)

self for chaining.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




