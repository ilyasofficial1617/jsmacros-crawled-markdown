

xyz.wagyourtail.jsmacros.client.api.library.impl.FWorld
-------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

Functions for getting and using world data.

An instance of this class is passed to scripts as the `World` variable.

#### Fields

[serverInstantTPS](1.9.2/)
S


[server1MAverageTPS](1.9.2/)
S


[server5MAverageTPS](1.9.2/)
S


[server15MAverageTPS](1.9.2/)
S



#### Methods

[isWorldLoaded()](#isWorldLoaded-)


[getLoadedPlayers()](#getLoadedPlayers-)


[getPlayers()](#getPlayers-)


[getPlayerEntry(name)](#getPlayerEntry-String-)


[getBlock(x, y, z)](#getBlock-int-int-int-)


[getBlock(pos)](#getBlock-Pos3D-)


[getBlock(pos)](#getBlock-BlockPosHelper-)


[getChunk(x, z)](#getChunk-int-int-)


[getWorldScanner()](#getWorldScanner-)


[getWorldScanner(blockFilter, stateFilter)](#getWorldScanner-MethodWrapper-MethodWrapper-)


[findBlocksMatching(centerX, centerZ, id, chunkrange)](#findBlocksMatching-int-int-String-int-)


[findBlocksMatching(id, chunkrange)](#findBlocksMatching-String-int-)


[findBlocksMatching(ids, chunkrange)](#findBlocksMatching-String[]-int-)


[findBlocksMatching(centerX, centerZ, ids, chunkrange)](#findBlocksMatching-int-int-String[]-int-)


[findBlocksMatching(blockFilter, stateFilter, chunkrange)](#findBlocksMatching-MethodWrapper-MethodWrapper-int-)


[findBlocksMatching(chunkX, chunkZ, blockFilter, stateFilter, chunkrange)](#findBlocksMatching-int-int-MethodWrapper-MethodWrapper-int-)


[iterateSphere(pos, radius, callback)](#iterateSphere-BlockPosHelper-int-MethodWrapper-)


[iterateSphere(pos, radius, ignoreAir, callback)](#iterateSphere-BlockPosHelper-int-boolean-MethodWrapper-)


[iterateBox(pos1, pos2, callback)](#iterateBox-BlockPosHelper-BlockPosHelper-MethodWrapper-)


[iterateBox(pos1, pos2, ignoreAir, callback)](#iterateBox-BlockPosHelper-BlockPosHelper-boolean-MethodWrapper-)


[getScoreboards()](#getScoreboards-)


[getEntities()](#getEntities-)


[getEntities(types)](#getEntities-String[]-)


[getEntities(distance)](#getEntities-double-)


[getEntities(distance, types)](#getEntities-double-String[]-)


[getEntities(filter)](#getEntities-MethodWrapper-)


[rayTraceBlock(x1, y1, z1, x2, y2, z2, fluid)](#rayTraceBlock-double-double-double-double-double-double-boolean-)


[rayTraceEntity(x1, y1, z1, x2, y2, z2)](#rayTraceEntity-double-double-double-double-double-double-)


[getDimension()](#getDimension-)


[getBiome()](#getBiome-)


[getTime()](#getTime-)


[getTimeOfDay()](#getTimeOfDay-)


[isDay()](#isDay-)


[isNight()](#isNight-)


[isRaining()](#isRaining-)


[isThundering()](#isThundering-)


[getWorldIdentifier()](#getWorldIdentifier-)


[getRespawnPos()](#getRespawnPos-)


[getDifficulty()](#getDifficulty-)


[getMoonPhase()](#getMoonPhase-)


[getSkyLight(x, y, z)](#getSkyLight-int-int-int-)


[getBlockLight(x, y, z)](#getBlockLight-int-int-int-)


[playSoundFile(file, volume)](#playSoundFile-String-double-)


[playSound(id)](#playSound-String-)


[playSound(id, volume)](#playSound-String-double-)


[playSound(id, volume, pitch)](#playSound-String-double-double-)


[playSound(id, volume, pitch, x, y, z)](#playSound-String-double-double-double-double-double-)


[getBossBars()](#getBossBars-)


[isChunkLoaded(chunkX, chunkZ)](#isChunkLoaded-int-int-)


[getCurrentServerAddress()](#getCurrentServerAddress-)


[getBiomeAt(x, z)](#getBiomeAt-int-int-)


[getBiomeAt(x, y, z)](#getBiomeAt-int-int-int-)


[getServerTPS()](#getServerTPS-)


[getTabListHeader()](#getTabListHeader-)


[getTabListFooter()](#getTabListFooter-)


[spawnParticle(id, x, y, z, count)](#spawnParticle-String-double-double-double-int-)


[spawnParticle(id, x, y, z, deltaX, deltaY, deltaZ, speed, count, force)](#spawnParticle-String-double-double-double-double-double-double-double-int-boolean-)


[getRaw()](#getRaw-)


[getServerInstantTPS()](#getServerInstantTPS-)


[getServer1MAverageTPS()](#getServer1MAverageTPS-)


[getServer5MAverageTPS()](#getServer5MAverageTPS-)


[getServer15MAverageTPS()](#getServer15MAverageTPS-)



### Fields

#### .serverInstantTPS

Static

Don't modify.


##### Type: double



#### .server1MAverageTPS

Static

Don't modify.


##### Type: double



#### .server5MAverageTPS

Static

Don't modify.


##### Type: double



#### .server15MAverageTPS

Static

Don't modify.


##### Type: double



### Methods

#### .isWorldLoaded()

1.3.0

returns whether a world is currently loaded


##### Returns: boolean



#### .getLoadedPlayers()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[PlayerEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/PlayerEntityHelper.html)<[PlayerEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/player/PlayerEntity)>>

players within render distance.



#### .getPlayers()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[PlayerListEntryHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/PlayerListEntryHelper.html)>

players on the tablist.



#### .getPlayerEntry(name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| name | String | the name of the player to get the entry for |

##### Returns: [PlayerListEntryHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/PlayerListEntryHelper.html)

player entry for the given player's name or `null` if not found.



#### .getBlock(x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: [BlockDataHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockDataHelper.html)

The block at that position.



#### .getBlock(pos)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |

##### Returns: [BlockDataHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockDataHelper.html)



#### .getBlock(pos)

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |

##### Returns: [BlockDataHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockDataHelper.html)



#### .getChunk(x, z)

1.8.4

The x and z position of the chunk can be calculated by the following formula: xChunk =
x >> 4; zChunk = z >> 4;

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the chunk, not the absolute position |
| z | int | the z coordinate of the chunk, not the absolute position |

##### Returns: [ChunkHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ChunkHelper.html)

ChunkHelper for the chunk coordinates [ChunkHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ChunkHelper.html).



#### .getWorldScanner()

1.6.5

Usage:   

This will return all blocks that are facing south, don't require a tool to break,
have a hardness of 10 or less and whose name contains either chest or barrel.

```
                 World.getWorldScanner()
                     .withBlockFilter("getHardness").is("<=", 10)
                     .andStringBlockFilter().contains("chest", "barrel")
                     .withStringStateFilter().contains("facing=south")
                     .andStateFilter("isToolRequired").is(false)
                     .build()
                 
```

##### Returns: [WorldScannerBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/worldscanner/WorldScannerBuilder.html)

a builder to create a WorldScanner.



#### .getWorldScanner(blockFilter, stateFilter)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| blockFilter | MethodWrapper<BlockHelper, Object, Boolean, ?> |  |
| stateFilter | MethodWrapper<BlockStateHelper, Object, Boolean, ?> |  |

##### Returns: [WorldScanner](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/worldscanner/WorldScanner.html)

a scanner for the current world.



#### .findBlocksMatching(centerX, centerZ, id, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| centerX | int |  |
| centerZ | int |  |
| id | String |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .findBlocksMatching(id, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .findBlocksMatching(ids, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| ids | String[] |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .findBlocksMatching(centerX, centerZ, ids, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| centerX | int |  |
| centerZ | int |  |
| ids | String[] |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .findBlocksMatching(blockFilter, stateFilter, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| blockFilter | MethodWrapper<BlockHelper, Object, Boolean, ?> |  |
| stateFilter | MethodWrapper<BlockStateHelper, Object, Boolean, ?> |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .findBlocksMatching(chunkX, chunkZ, blockFilter, stateFilter, chunkrange)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| chunkX | int |  |
| chunkZ | int |  |
| blockFilter | MethodWrapper<BlockHelper, Object, Boolean, ?> |  |
| stateFilter | MethodWrapper<BlockStateHelper, Object, Boolean, ?> |  |
| chunkrange | int |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>



#### .iterateSphere(pos, radius, callback)

1.8.4

By default, air blocks are ignored and the callback is only called for real blocks.

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the center position |
| radius | int | the radius to scan |
| callback | MethodWrapper<BlockDataHelper, ?, ?, ?> | the callback to call for each block |

##### Returns: void



#### .iterateSphere(pos, radius, ignoreAir, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the center position |
| radius | int | the radius to scan |
| ignoreAir | boolean | whether to ignore air blocks |
| callback | MethodWrapper<BlockDataHelper, ?, ?, ?> | the callback to call for each block |

##### Returns: void



#### .iterateBox(pos1, pos2, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position |
| pos2 | BlockPosHelper | the second position |
| callback | MethodWrapper<BlockDataHelper, ?, ?, ?> | the callback to call for each block |

##### Returns: void



#### .iterateBox(pos1, pos2, ignoreAir, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position |
| pos2 | BlockPosHelper | the second position |
| ignoreAir | boolean | whether to ignore air blocks |
| callback | MethodWrapper<BlockDataHelper, ?, ?, ?> | the callback to call for each block |

##### Returns: void



#### .getScoreboards()

1.2.9


##### Returns: [ScoreboardsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ScoreboardsHelper.html)

a helper for the scoreboards provided to the client.



#### .getEntities()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >>

all entities in the render distance.



#### .getEntities(types)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| types | String[] | the entity types to consider |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >>

all entities in the render distance, that match the specified entity type.



#### .getEntities(distance)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| distance | double | the maximum distance to search for entities |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >>

a list of entities within the specified distance to the player.



#### .getEntities(distance, types)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| distance | double | the maximum distance to search for entities |
| types | String[] | the entity types to consider |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >>

a list of entities within the specified distance to the player, that match the specified entity type.



#### .getEntities(filter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| filter | MethodWrapper<EntityHelper<?>, ?, ?, ?> | the entity filter |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >>

a list of entities that match the specified filter.



#### .rayTraceBlock(x1, y1, z1, x2, y2, z2, fluid)

1.6.5

raytrace between two points returning the first block hit.

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |
| fluid | boolean |  |

##### Returns: [BlockDataHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockDataHelper.html)



#### .rayTraceEntity(x1, y1, z1, x2, y2, z2)

1.8.3

raytrace between two points returning the first entity hit.

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |

##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >



#### .getDimension()

1.1.2

note that some server might utilize dimension identifiers for mods to distinguish between worlds.


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current dimension.



#### .getBiome()

1.1.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current biome.



#### .getTime()

1.1.5

ticks processed since world was started.


##### Returns: long

the current world time. `-1` if world is not loaded.



#### .getTimeOfDay()

1.1.5

ticks passed since world was started INCLUDING those skipped when nights were cut short with sleeping.


##### Returns: long

the current world time of day. `-1` if world is not loaded.



#### .isDay()

1.8.4


##### Returns: boolean

`true` if it is daytime, `false` otherwise.



#### .isNight()

1.8.4


##### Returns: boolean

`true` if it is nighttime, `false` otherwise.



#### .isRaining()

1.8.4


##### Returns: boolean

`true` if it is raining, `false` otherwise.



#### .isThundering()

1.8.4


##### Returns: boolean

`true` if it is thundering, `false` otherwise.



#### .getWorldIdentifier()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

an identifier for the loaded world that is based on the world's name or server ip and
thus most likely unique enough to identify a specific world, or
`"UNKNOWN_NAME"` if no world was found.



#### .getRespawnPos()

1.2.6


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

respawn position.



#### .getDifficulty()

1.2.6


##### Returns: int

world difficulty as an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html). `-1` if world is not loaded.



#### .getMoonPhase()

1.2.6


##### Returns: int

moon phase as an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html). `-1` if world is not loaded.



#### .getSkyLight(x, y, z)

1.1.2

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: int

sky light as an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html). `-1` if world is not loaded.



#### .getBlockLight(x, y, z)

1.1.2

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: int

block light as an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html). `-1` if world is not loaded.



#### .playSoundFile(file, volume)

1.1.7

plays a sound file using javax's sound stuff.

| Parameter | Type | Description |
|---|---|---|
| file | String |  |
| volume | double |  |

##### Returns: [Clip](https://docs.oracle.com/javase/8/docs/api/index.html?javax/sound/sampled/Clip.html)



#### .playSound(id)

1.1.7

| Parameter | Type | Description |
|---|---|---|
| id | String |  |

##### Returns: void



#### .playSound(id, volume)

1.1.7

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| volume | double |  |

##### Returns: void



#### .playSound(id, volume, pitch)

1.1.7

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| volume | double |  |
| pitch | double |  |

##### Returns: void



#### .playSound(id, volume, pitch, x, y, z)

1.1.7

plays a minecraft sound using the internal system.

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| volume | double |  |
| pitch | double |  |
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: void



#### .getBossBars()

1.2.1


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [BossBarHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/BossBarHelper.html)>

a map of boss bars by the boss bar's UUID.



#### .isChunkLoaded(chunkX, chunkZ)

1.2.2

Check whether a chunk is within the render distance and loaded.

| Parameter | Type | Description |
|---|---|---|
| chunkX | int |  |
| chunkZ | int |  |

##### Returns: boolean



#### .getCurrentServerAddress()

1.2.2


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current server address as a string (`server.address/server.ip:port`).



#### .getBiomeAt(x, z)

1.2.2 [Citation Needed]

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| z | int |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

biome at specified location, only works if the block/chunk is loaded.



#### .getBiomeAt(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

biome at specified location, only works if the block/chunk is loaded.



#### .getServerTPS()

1.2.7


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

best attempt to measure and give the server tps with various timings.



#### .getTabListHeader()

1.3.1


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

text helper for the top part of the tab list (above the players)



#### .getTabListFooter()

1.3.1


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

text helper for the bottom part of the tab list (below the players)



#### .spawnParticle(id, x, y, z, count)

1.8.4

Summons the amount of particles at the desired position.

| Parameter | Type | Description |
|---|---|---|
| id | String | the particle id |
| x | double | the x position to spawn the particle |
| y | double | the y position to spawn the particle |
| z | double | the z position to spawn the particle |
| count | int | the amount of particles to spawn |

##### Returns: void



#### .spawnParticle(id, x, y, z, deltaX, deltaY, deltaZ, speed, count, force)

1.8.4

Summons the amount of particles at the desired position with some variation of delta and the
given speed.

| Parameter | Type | Description |
|---|---|---|
| id | String | the particle id |
| x | double | the x position to spawn the particle |
| y | double | the y position to spawn the particle |
| z | double | the z position to spawn the particle |
| deltaX | double | the x variation of the particle |
| deltaY | double | the y variation of the particle |
| deltaZ | double | the z variation of the particle |
| speed | double | the speed of the particle |
| count | int | the amount of particles to spawn |
| force | boolean | whether to show the particle if it's more than 32 blocks away |

##### Returns: void



#### .getRaw()

1.9.1


##### Returns: [ClientWorld](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/world/ClientWorld)

the raw minecraft world.



#### .getServerInstantTPS()

1.2.7


##### Returns: double

best attempt to measure and give the server tps.



#### .getServer1MAverageTPS()

1.2.7


##### Returns: double

best attempt to measure and give the server tps over the previous 1 minute average.



#### .getServer5MAverageTPS()

1.2.7


##### Returns: double

best attempt to measure and give the server tps over the previous 5 minute average.



#### .getServer15MAverageTPS()

1.2.7


##### Returns: double

best attempt to measure and give the server tps over the previous 15 minute average.




