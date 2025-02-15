

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.decoration.EndCrystalEntityHelper
------------------------------------------------------------------------------------------------------

#### extends [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)<[EndCrystalEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/decoration/EndCrystalEntity)>

1.8.4

### Constructors

#### new EndCrystalEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | EndCrystalEntity |  |



#### Methods

[isNatural()](#isNatural-)


[getBeamTarget()](#getBeamTarget-)



### Methods

#### .isNatural()

1.8.4

Naturally generated end crystals will have a bedrock base, while player placed ones will
not.


##### Returns: boolean

`true` if the end crystal was not placed by a player, `false` otherwise.



#### .getBeamTarget()

1.8.4


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the target of the crystal's beam, or `null` if there is none.




