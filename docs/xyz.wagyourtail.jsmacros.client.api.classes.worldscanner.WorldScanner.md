

xyz.wagyourtail.jsmacros.client.api.classes.worldscanner.WorldScanner
---------------------------------------------------------------------

#### 

1.6.5

A class to scan the world for certain blocks. The results of the filters are cached,
so it's a good idea to reuse an instance of this if possible.
The scanner can either return a list of all block positions or
a list of blocks and their respective count for every block / state matching the filters criteria.

### Constructors

#### new WorldScanner (world, blockFilter, stateFilter)

Creates a new World scanner with for the given world. It accepts two boolean functions,
one for [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html) and the other for [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html).

| Parameter | Type | Description |
|---|---|---|
| world | World | the world to scan |
| blockFilter | Function<BlockHelper, Boolean> | a filter method for the blocks |
| stateFilter | Function<BlockStateHelper, Boolean> | a filter method for the block states |



#### Methods

[getChunkRange(centerX, centerZ, chunkrange)](#getChunkRange-int-int-int-)


[scanAroundPlayer(chunkRange)](#scanAroundPlayer-int-)


[scanChunkRange(centerX, centerZ, chunkrange)](#scanChunkRange-int-int-int-)


[scanCubeArea(pos, range)](#scanCubeArea-BlockPosHelper-int-)


[scanCubeArea(x, y, z, range)](#scanCubeArea-int-int-int-int-)


[scanCubeArea(pos1, pos2)](#scanCubeArea-BlockPosHelper-BlockPosHelper-)


[scanCubeArea(x1, y1, z1, x2, y2, z2)](#scanCubeArea-int-int-int-int-int-int-)


[scanCubeAreaInclusive(pos1, pos2)](#scanCubeAreaInclusive-BlockPosHelper-BlockPosHelper-)


[scanCubeAreaInclusive(x1, y1, z1, x2, y2, z2)](#scanCubeAreaInclusive-int-int-int-int-int-int-)


[scanSphereArea(pos, radius)](#scanSphereArea-Pos3D-double-)


[scanSphereArea(x, y, z, radius)](#scanSphereArea-double-double-double-double-)


[scanReachable()](#scanReachable-)


[scanReachable(strict)](#scanReachable-boolean-)


[scanReachable(pos)](#scanReachable-Pos3D-)


[scanReachable(pos, reach)](#scanReachable-Pos3D-double-)


[scanReachable(pos, reach, strict)](#scanReachable-Pos3D-double-boolean-)


[scanClosestReachable()](#scanClosestReachable-)


[scanClosestReachable(strict)](#scanClosestReachable-boolean-)


[scanClosestReachable(pos, reach, strict)](#scanClosestReachable-Pos3D-double-boolean-)


[getBlocksInChunk(chunkX, chunkZ, ignoreState)](#getBlocksInChunk-int-int-boolean-)


[getBlocksInChunks(centerX, centerZ, chunkRange, ignoreState)](#getBlocksInChunks-int-int-int-boolean-)


[getCachedAmount()](#getCachedAmount-)



### Methods

#### .getChunkRange(centerX, centerZ, chunkrange)

Gets a list of all chunks in the given range around the center chunk.

| Parameter | Type | Description |
|---|---|---|
| centerX | int | the x coordinate of the center chunk to scan around |
| centerZ | int | the z coordinate of the center chunk to scan around |
| chunkrange | int | the range to scan around the center chunk |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ChunkPos](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/ChunkPos)>

a list of all matching block positions.



#### .scanAroundPlayer(chunkRange)

Scans all chunks in the given range around the player and returns a list of all block positions, for blocks matching the filter.
This will scan in a square with length 2\*range + 1. So range = 0 for example will only scan the chunk the player
is standing in, while range = 1 will scan in a 3x3 area.

| Parameter | Type | Description |
|---|---|---|
| chunkRange | int | the range to scan around the center chunk |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>

a list of all matching block positions.



#### .scanChunkRange(centerX, centerZ, chunkrange)

Scans all chunks in the given range around the center chunk and returns a list of all block positions, for blocks matching the filter.
This will scan in a square with length 2\*range + 1. So range = 0 for example will only scan the specified chunk,
while range = 1 will scan in a 3x3 area.

| Parameter | Type | Description |
|---|---|---|
| centerX | int | the x coordinate of the center chunk to scan around |
| centerZ | int | the z coordinate of the center chunk to scan around |
| chunkrange | int | the range to scan around the center chunk |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>

a list of all matching block positions.



#### .scanCubeArea(pos, range)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |
| range | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanCubeArea(x, y, z, range)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| range | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanCubeArea(pos1, pos2)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | first pos, inclusive |
| pos2 | BlockPosHelper | second pos, exclusive |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanCubeArea(x1, y1, z1, x2, y2, z2)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| x1 | int | first x coordinate, inclusive |
| y1 | int | first y coordinate, inclusive |
| z1 | int | first z coordinate, inclusive |
| x2 | int | second x coordinate, exclusive |
| y2 | int | second y coordinate, exclusive |
| z2 | int | second z coordinate, exclusive |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanCubeAreaInclusive(pos1, pos2)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | first pos, inclusive |
| pos2 | BlockPosHelper | second pos, inclusive |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanCubeAreaInclusive(x1, y1, z1, x2, y2, z2)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| x1 | int | first x coordinate, inclusive |
| y1 | int | first y coordinate, inclusive |
| z1 | int | first z coordinate, inclusive |
| x2 | int | second x coordinate, inclusive |
| y2 | int | second y coordinate, inclusive |
| z2 | int | second z coordinate, inclusive |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanSphereArea(pos, radius)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| radius | double |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanSphereArea(x, y, z, radius)

1.9.1

scan area in blocks

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| radius | double |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanReachable()

1.9.1

scan around with player pos and player reach.  

this doesn't filter out positions that has obstacle.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanReachable(strict)

1.9.1

scan around with player pos and player reach.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| strict | boolean | if it should check for block outline instead of full cube, default is true |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanReachable(pos)

1.9.1

scan around with the given pos and player reach.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanReachable(pos, reach)

1.9.1

scan around with the given pos and the given reach.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| reach | double |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanReachable(pos, reach, strict)

1.9.1

scan around with the given pos and the given reach.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | Player.getPlayer().getEyePos() |
| reach | double | Player.getInteractionManager().getReach() |
| strict | boolean | if it should check for block outline instead of full cube, default is true |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .scanClosestReachable()

1.9.1

scan around with player pos and player reach, and return the closest one.  

this doesn't filter out positions that has obstacle.


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .scanClosestReachable(strict)

1.9.1

scan around with player pos and player reach, and return the closest one.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| strict | boolean |  |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .scanClosestReachable(pos, reach, strict)

1.9.1

scan around with player pos and player reach, and return the closest one.  

this doesn't filter out positions that has obstacle.

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| reach | double |  |
| strict | boolean |  |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .getBlocksInChunk(chunkX, chunkZ, ignoreState)

Gets the amount of all blocks matching the criteria inside the chunk.

| Parameter | Type | Description |
|---|---|---|
| chunkX | int | the x coordinate of the chunk to scan |
| chunkZ | int | the z coordinate of the chunk to scan |
| ignoreState | boolean | whether multiple states should be combined to a single block |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)>

a map of all blocks inside the specified chunk and their respective count.



#### .getBlocksInChunks(centerX, centerZ, chunkRange, ignoreState)

Gets the amount of all blocks matching the criteria inside a square around the player.

| Parameter | Type | Description |
|---|---|---|
| centerX | int | the x coordinate of the center chunk to scan around |
| centerZ | int | the z coordinate of the center chunk to scan around |
| chunkRange | int | the range to scan around the center chunk |
| ignoreState | boolean | whether multiple states should be combined to a single block |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)>

a map of all blocks inside the specified chunks and their respective count.



#### .getCachedAmount()

Get the amount of cached block states. This will normally be around 200 - 400.


##### Returns: int

the amount of cached block states.




