

xyz.wagyourtail.jsmacros.client.api.helpers.world.ChunkHelper
-------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Chunk](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/chunk/Chunk)>

1.8.4

### Constructors

#### new ChunkHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | Chunk |  |



#### Methods

[getStartingBlock()](#getStartingBlock-)


[getOffsetBlock(xOffset, y, zOffset)](#getOffsetBlock-int-int-int-)


[getMaxBuildHeight()](#getMaxBuildHeight-)


[getMinBuildHeight()](#getMinBuildHeight-)


[getHeight()](#getHeight-)


[getTopYAt(xOffset, zOffset, heightmap)](#getTopYAt-int-int-Heightmap-)


[getChunkX()](#getChunkX-)


[getChunkZ()](#getChunkZ-)


[getBiome(xOffset, y, zOffset)](#getBiome-int-int-int-)


[getInhabitedTime()](#getInhabitedTime-)


[getEntities()](#getEntities-)


[getTileEntities()](#getTileEntities-)


[forEach(includeAir, callback)](#forEach-boolean-MethodWrapper-)


[containsAny(blocks)](#containsAny-String[]-)


[containsAll(blocks)](#containsAll-String[]-)


[getHeightmaps()](#getHeightmaps-)


[getSurfaceHeightmap()](#getSurfaceHeightmap-)


[getOceanFloorHeightmap()](#getOceanFloorHeightmap-)


[getMotionBlockingHeightmap()](#getMotionBlockingHeightmap-)


[getMotionBlockingNoLeavesHeightmap()](#getMotionBlockingNoLeavesHeightmap-)


[toString()](#toString-)



### Methods

#### .getStartingBlock()

1.8.4


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the first block (0 0 0 coordinate) of this chunk.



#### .getOffsetBlock(xOffset, y, zOffset)

1.8.4

The coordinates are relative to the starting chunk position, see
[ChunkHelper#getStartingBlock()](#getStartingBlock-).

| Parameter | Type | Description |
|---|---|---|
| xOffset | int | the xOffset offset |
| y | int | the actual y coordinate |
| zOffset | int | the zOffset offset |

##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the block offset from the starting block of this chunk by xOffset y zOffset.



#### .getMaxBuildHeight()

1.8.4


##### Returns: int

the maximum height of this chunk.



#### .getMinBuildHeight()

1.8.4


##### Returns: int

the minimum height of this chunk.



#### .getHeight()

1.8.4


##### Returns: int

the height of this chunk.



#### .getTopYAt(xOffset, zOffset, heightmap)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| xOffset | int | the xOffset coordinate |
| zOffset | int | the zOffset coordinate |
| heightmap | Heightmap | the heightmap to use |

##### Returns: int

the maximum `y` position of all blocks inside this chunk.



#### .getChunkX()

1.8.4


##### Returns: int

the `x` coordinate (not the world coordinate) of this chunk.



#### .getChunkZ()

1.8.4


##### Returns: int

the `z` coordinate (not the world coordinate) of this chunk.



#### .getBiome(xOffset, y, zOffset)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| xOffset | int | the x offset |
| y | int | the y coordinate |
| zOffset | int | the z offset |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the biome at the given position.



#### .getInhabitedTime()

1.8.4

With an increasing inhabited time, the local difficulty increases and stronger mobs will
spawn. Because the time is cumulative, the more players are in the chunk, the faster the time
will increase.


##### Returns: long

the cumulative time players have spent inside this chunk.



#### .getEntities()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< ? >

all entities inside this chunk.



#### .getTileEntities()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)>

all tile entity positions inside this chunk.



#### .forEach(includeAir, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| includeAir | boolean | whether to include air blocks or not |
| callback | MethodWrapper<BlockDataHelper, ?, ?, ?> | the callback function |

##### Returns: [ChunkHelper](#)

self for chaining.



#### .containsAny(blocks)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| blocks | String[] | the blocks to search for |

##### Returns: boolean

`true` if this chunk contains at least one of the specified blocks,
`false` otherwise.



#### .containsAll(blocks)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| blocks | String[] | the blocks to search for |

##### Returns: boolean

`true` if the chunk contains all the specified blocks, `false`
otherwise.



#### .getHeightmaps()

1.8.4


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[Map$Entry](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map$Entry.html)<[Heightmap$Type](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap$Type), [Heightmap](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap)>>

a map of the raw heightmap data.



#### .getSurfaceHeightmap()

1.8.4


##### Returns: [Heightmap](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap)

the raw surface heightmap.



#### .getOceanFloorHeightmap()

1.8.4


##### Returns: [Heightmap](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap)

the raw ocean floor heightmap.



#### .getMotionBlockingHeightmap()

1.8.4


##### Returns: [Heightmap](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap)

the raw motion blocking heightmap.



#### .getMotionBlockingNoLeavesHeightmap()

1.8.4


##### Returns: [Heightmap](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/Heightmap)

the raw motion blocking heightmap without leaves.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




