

xyz.wagyourtail.jsmacros.client.api.helpers.world.PlayerListEntryHelper
-----------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[PlayerListEntry](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/network/PlayerListEntry)>

1.0.2

### Constructors

#### new PlayerListEntryHelper (p)

| Parameter | Type | Description |
|---|---|---|
| p | PlayerListEntry |  |



#### Methods

[getUUID()](#getUUID-)


[getName()](#getName-)


[getPing()](#getPing-)


[getGamemode()](#getGamemode-)


[getDisplayText()](#getDisplayText-)


[getPublicKey()](#getPublicKey-)


[hasCape()](#hasCape-)


[hasSlimModel()](#hasSlimModel-)


[getSkinTexture()](#getSkinTexture-)


[getSkinUrl()](#getSkinUrl-)


[getCapeTexture()](#getCapeTexture-)


[getElytraTexture()](#getElytraTexture-)


[getTeam()](#getTeam-)


[toString()](#toString-)



### Methods

#### .getUUID()

1.1.9


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getName()

1.0.2


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getPing()

1.6.5


##### Returns: int



#### .getGamemode()

1.6.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

null if unknown



#### .getDisplayText()

1.1.9


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)



#### .getPublicKey()

1.8.2


##### Returns: byte []



#### .hasCape()

1.8.4


##### Returns: boolean

`true` if the player has a cape enabled, `false` otherwise.



#### .hasSlimModel()

1.8.4

A slim skin is an Alex skin, while the default one is Steve.


##### Returns: boolean

`true` if the player has a slim skin, `false` otherwise.



#### .getSkinTexture()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of the player's skin texture or `null` if it's unknown.



#### .getSkinUrl()

1.9.0


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getCapeTexture()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of the player's cape texture or `null` if it's unknown.



#### .getElytraTexture()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of the player's elytra texture or `null` if it's unknown.



#### .getTeam()

1.8.4


##### Returns: [TeamHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/TeamHelper.html)

the team of the player or `null` if the player is not in a team.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




