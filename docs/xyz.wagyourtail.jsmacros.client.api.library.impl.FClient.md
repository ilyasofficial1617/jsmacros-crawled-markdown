

xyz.wagyourtail.jsmacros.client.api.library.impl.FClient
--------------------------------------------------------

#### extends [PerExecLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLibrary.html)

1.2.9

Functions that interact with minecraft that don't fit into their own module.

An instance of this class is passed to scripts as the `Client` variable.

#### Fields

[tickSynchronizer](#tickSynchronizer)
S



#### Methods

[getMinecraft()](#getMinecraft-)


[getRegistryManager()](#getRegistryManager-)


[createPacketByteBuffer()](#createPacketByteBuffer-)


[runOnMainThread(runnable)](#runOnMainThread-MethodWrapper-)


[runOnMainThread(runnable, watchdogMaxTime)](#runOnMainThread-MethodWrapper-long-)


[runOnMainThread(runnable, await, watchdogMaxTime)](#runOnMainThread-MethodWrapper-boolean-long-)


[getGameOptions()](#getGameOptions-)


[mcVersion()](#mcVersion-)


[getFPS()](#getFPS-)


[loadWorld(folderName)](#loadWorld-String-)


[connect(ip)](#connect-String-)


[connect(ip, port)](#connect-String-int-)


[disconnect()](#disconnect-)


[disconnect(callback)](#disconnect-MethodWrapper-)


[shutdown()](#shutdown-)


[waitTick()](#waitTick-)


[waitTick(i)](#waitTick-int-)


[ping(ip)](#ping-String-)


[pingAsync(ip, callback)](#pingAsync-String-MethodWrapper-)


[cancelAllPings()](#cancelAllPings-)


[getLoadedMods()](#getLoadedMods-)


[isModLoaded(modId)](#isModLoaded-String-)


[getMod(modId)](#getMod-String-)


[grabMouse()](#grabMouse-)


[isDevEnv()](#isDevEnv-)


[getModLoader()](#getModLoader-)


[getRegisteredBlocks()](#getRegisteredBlocks-)


[getRegisteredItems()](#getRegisteredItems-)


[exitGamePeacefully()](#exitGamePeacefully-)


[exitGameForcefully()](#exitGameForcefully-)


[sendPacket(packet)](#sendPacket-Packet-)


[receivePacket(packet)](#receivePacket-Packet-)



### Fields

#### .tickSynchronizer

Static

Don't touch this plz xd.


##### Type: [TickSync](1.9.2/xyz/wagyourtail/jsmacros/client/tick/TickSync.html)



### Methods

#### .getMinecraft()

1.0.0 (was in the `jsmacros` library until 1.2.9)


##### Returns: [MinecraftClient](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/MinecraftClient)

the raw minecraft client class, it may be useful to use [Minecraft Mappings Viewer](https://wagyourtail.xyz/Projects/Minecraft%20Mappings%20Viewer/App) for this.



#### .getRegistryManager()

1.8.4


##### Returns: [RegistryHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/RegistryHelper.html)

a helper for interacting with minecraft's registry.



#### .createPacketByteBuffer()

1.8.4


##### Returns: [PacketByteBufferHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/PacketByteBufferHelper.html)

a helper to modify and send minecraft packets.



#### .runOnMainThread(runnable)

1.4.0

Run your task on the main minecraft thread

| Parameter | Type | Description |
|---|---|---|
| runnable | MethodWrapper<Object, Object, Object, ?> | task to run |

##### Returns: void



#### .runOnMainThread(runnable, watchdogMaxTime)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| runnable | MethodWrapper<Object, Object, Object, ?> |  |
| watchdogMaxTime | long |  |

##### Returns: void



#### .runOnMainThread(runnable, await, watchdogMaxTime)

1.9.1

| Parameter | Type | Description |
|---|---|---|
| runnable | MethodWrapper<Object, Object, Object, ?> |  |
| await | boolean |  |
| watchdogMaxTime | long | max time for the watchdog to wait before killing the script |

##### Returns: void



#### .getGameOptions()

1.1.7 (was in the `jsmacros` library until 1.2.9)


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

a helper which gives access to all game options and some other useful features.



#### .mcVersion()

1.1.2 (was in the `jsmacros` library until 1.2.9)


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current minecraft version as a [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html).



#### .getFPS()

1.2.0 (was in the `jsmacros` library until 1.2.9)


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the fps debug string from minecraft.



#### .loadWorld(folderName)

1.6.6

Join singleplayer world

| Parameter | Type | Description |
|---|---|---|
| folderName | String |  |

##### Returns: void



#### .connect(ip)

1.2.3 (was in the `jsmacros` library until 1.2.9)

| Parameter | Type | Description |
|---|---|---|
| ip | String |  |

##### Returns: void



#### .connect(ip, port)

1.2.3 (was in the `jsmacros` library until 1.2.9)

Connect to a server

| Parameter | Type | Description |
|---|---|---|
| ip | String |  |
| port | int |  |

##### Returns: void



#### .disconnect()

1.2.3 (was in the `jsmacros` library until 1.2.9)


##### Returns: void



#### .disconnect(callback)

1.2.3 (was in the `jsmacros` library until 1.2.9)

`callback` defaults to `null`

Disconnect from a server with callback.

| Parameter | Type | Description |
|---|---|---|
| callback | MethodWrapper<Boolean, Object, Object, ?> | calls your method as a Consumer<Boolean> |

##### Returns: void



#### .shutdown()

1.6.0

Closes the client (stops the game).
Waits until the game has stopped, meaning no further code is executed (for obvious reasons).
Warning: this does not wait on joined threads, so your script may stop at an undefined point.


##### Returns: void



#### .waitTick()

1.2.4


##### Returns: void



#### .waitTick(i)

1.2.6

waits the specified number of client ticks.
don't use this on an event that the main thread waits on (joins)... that'll cause circular waiting.

| Parameter | Type | Description |
|---|---|---|
| i | int |  |

##### Returns: void



#### .ping(ip)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| ip | String |  |

##### Returns: [ServerInfoHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ServerInfoHelper.html)



#### .pingAsync(ip, callback)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| ip | String |  |
| callback | MethodWrapper<ServerInfoHelper, IOException, Object, ?> |  |

##### Returns: void



#### .cancelAllPings()

1.6.5


##### Returns: void



#### .getLoadedMods()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< ? >

a list of all loaded mods.



#### .isModLoaded(modId)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| modId | String | the mod modId |

##### Returns: boolean

`true` if the mod with the given modId is loaded, `false` otherwise.



#### .getMod(modId)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| modId | String | the mod modId |

##### Returns: [ModContainerHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/ModContainerHelper.html)< ? >

the mod container for the given modId or `null` if the mod is not loaded.



#### .grabMouse()

1.8.4

Makes minecraft believe that the mouse is currently inside the window.
This will automatically set pause on lost focus to false.


##### Returns: void



#### .isDevEnv()

1.8.4


##### Returns: boolean

`true` if the mod is loaded inside a development environment, `false` otherwise.



#### .getModLoader()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the mod loader.



#### .getRegisteredBlocks()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)>

a list of all loaded blocks as [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html) objects.



#### .getRegisteredItems()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html)>

a list of all loaded items as [ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html) objects.



#### .exitGamePeacefully()

1.8.4

Tries to peacefully close the game.


##### Returns: void



#### .exitGameForcefully()

1.8.4

Will close the game forcefully.


##### Returns: void



#### .sendPacket(packet)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packet | Packet<?> | the packet to send |

##### Returns: void



#### .receivePacket(packet)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packet | Packet<ClientPlayPacketListener> | the packet to receive |

##### Returns: void




