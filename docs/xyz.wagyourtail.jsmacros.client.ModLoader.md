

xyz.wagyourtail.jsmacros.client.ModLoader
-----------------------------------------

Interface
#### 

1.8.4

#### Methods

[isDevEnv()](#isDevEnv-)


[getName()](#getName-)


[getLoadedMods()](#getLoadedMods-)


[isModLoaded(modId)](#isModLoaded-String-)


[getMod(modId)](#getMod-String-)



### Methods

#### .isDevEnv()

1.8.4


##### Returns: boolean

`true` if the game is running in a development environment, `false`
otherwise.



#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the current mod loader.



#### .getLoadedMods()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< ? >

a list of all loaded mods.



#### .isModLoaded(modId)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| modId | String | the mod id to check |

##### Returns: boolean

`true` if the mod with the given id is loaded, `false` otherwise.



#### .getMod(modId)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| modId | String | the mod id |

##### Returns: [ModContainerHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/ModContainerHelper.html)< ? >

the mod container for the given id or `null` if the mod is not loaded.




