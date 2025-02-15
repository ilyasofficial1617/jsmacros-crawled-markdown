

xyz.wagyourtail.jsmacros.client.api.helpers.world.BlockDataHelper
-----------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[BlockState](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/block/BlockState)>

### Constructors

#### new BlockDataHelper (b, e, bp)

| Parameter | Type | Description |
|---|---|---|
| b | BlockState |  |
| e | BlockEntity |  |
| bp | BlockPos |  |



#### Methods

[getX()](#getX-)


[getY()](#getY-)


[getZ()](#getZ-)


[getId()](#getId-)


[getName()](#getName-)


[getNBT()](#getNBT-)


[getBlockStateHelper()](#getBlockStateHelper-)


[getBlockHelper()](#getBlockHelper-)
D


[getBlock()](#getBlock-)


[getBlockState()](#getBlockState-)


[getBlockPos()](#getBlockPos-)


[getRawBlock()](#getRawBlock-)


[getRawBlockState()](#getRawBlockState-)


[getRawBlockEntity()](#getRawBlockEntity-)


[toString()](#toString-)



### Methods

#### .getX()

1.1.7


##### Returns: int

the `x` value of the block.



#### .getY()

1.1.7


##### Returns: int

the `y` value of the block.



#### .getZ()

1.1.7


##### Returns: int

the `z` value of the block.



#### .getId()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the item ID of the block.



#### .getName()


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the translated name of the block. (was string before 1.6.5)



#### .getNBT()

1.5.1, used to be a [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>


##### Returns: [NBTElementHelper$NBTCompoundHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/NBTElementHelper.NBTCompoundHelper.html)



#### .getBlockStateHelper()

1.6.5


##### Returns: [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html)



#### .getBlockHelper()

Deprecated

1.6.5


##### Returns: [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)



#### .getBlock()

1.6.5


##### Returns: [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)

the block



#### .getBlockState()

1.1.7


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

block state data as a [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html).



#### .getBlockPos()

1.2.7


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the block pos.



#### .getRawBlock()


##### Returns: [Block](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/block/Block)



#### .getRawBlockState()


##### Returns: [BlockState](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/block/BlockState)



#### .getRawBlockEntity()


##### Returns: [BlockEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/block/entity/BlockEntity)



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




