
[UniversalBlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/UniversalBlockStateHelper.html)

xyz.wagyourtail.jsmacros.client.api.helpers.world.BlockStateHelper
------------------------------------------------------------------

#### extends [StateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/StateHelper.html)<[BlockState](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/block/BlockState)>

1.6.5

### Constructors

#### new BlockStateHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | BlockState |  |



#### Methods

[getBlock()](#getBlock-)


[getId()](#getId-)


[getFluidState()](#getFluidState-)


[getHardness()](#getHardness-)


[getLuminance()](#getLuminance-)


[emitsRedstonePower()](#emitsRedstonePower-)


[exceedsCube()](#exceedsCube-)


[isAir()](#isAir-)


[isOpaque()](#isOpaque-)


[isToolRequired()](#isToolRequired-)


[hasBlockEntity()](#hasBlockEntity-)


[hasRandomTicks()](#hasRandomTicks-)


[hasComparatorOutput()](#hasComparatorOutput-)


[getPistonBehaviour()](#getPistonBehaviour-)


[blocksMovement()](#blocksMovement-)


[isBurnable()](#isBurnable-)


[isLiquid()](#isLiquid-)


[isSolid()](#isSolid-)


[isReplaceable()](#isReplaceable-)


[allowsSpawning(pos, entity)](#allowsSpawning-BlockPosHelper-String-)


[shouldSuffocate(pos)](#shouldSuffocate-BlockPosHelper-)


[getUniversal()](#getUniversal-)


[toString()](#toString-)



### Methods

#### .getBlock()

1.6.5


##### Returns: [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)

the block the state belongs to.



#### .getId()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the block's id.



#### .getFluidState()

1.8.4


##### Returns: [FluidStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/FluidStateHelper.html)

the fluid state of this block state.



#### .getHardness()

1.6.5


##### Returns: float

the hardness.



#### .getLuminance()

1.6.5


##### Returns: int

the luminance.



#### .emitsRedstonePower()

1.6.5


##### Returns: boolean

`true` if the state emits redstone power.



#### .exceedsCube()

1.6.5


##### Returns: boolean

`true` if the shape of the state is a cube.



#### .isAir()

1.6.5


##### Returns: boolean

`true` if the state is air.



#### .isOpaque()

1.6.5


##### Returns: boolean

`true` if the state is opaque.



#### .isToolRequired()

1.6.5


##### Returns: boolean

`true` if a tool is required to mine the block.



#### .hasBlockEntity()

1.6.5


##### Returns: boolean

`true` if the state has a block entity.



#### .hasRandomTicks()

1.6.5


##### Returns: boolean

`true` if the state can be random ticked.



#### .hasComparatorOutput()

1.6.5


##### Returns: boolean

`true` if the state has a comparator output.



#### .getPistonBehaviour()

1.6.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the piston behaviour of the state.



#### .blocksMovement()

1.6.5


##### Returns: boolean

`true` if the state blocks the movement of entities.



#### .isBurnable()

1.6.5


##### Returns: boolean

`true` if the state is burnable.



#### .isLiquid()

1.6.5


##### Returns: boolean

`true` if the state is a liquid.



#### .isSolid()

1.6.5


##### Returns: boolean

`true` if the state is solid.



#### .isReplaceable()

1.6.5

This will return true for blocks like air and grass, that can be replaced without breaking
them first.


##### Returns: boolean

`true` if the state can be replaced.



#### .allowsSpawning(pos, entity)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position of the block to check |
| entity | String | the entity type to check |

##### Returns: boolean

`true` if the entity can spawn on this block state at the given position in the
current world.



#### .shouldSuffocate(pos)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position of the block to check |

##### Returns: boolean

`true` if an entity can suffocate in this block state at the given position in
the current world.



#### .getUniversal()

1.8.4


##### Returns: [UniversalBlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/UniversalBlockStateHelper.html)

an [UniversalBlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/UniversalBlockStateHelper.html) to access all properties of this block state.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




