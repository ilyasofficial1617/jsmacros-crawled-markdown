

xyz.wagyourtail.jsmacros.client.mixins.events.MixinMinecraftClient
------------------------------------------------------------------

Abstract
#### 

### Constructors

#### new MixinMinecraftClient ()




#### Fields

[currentScreen](#currentScreen)


[interactionManager](#interactionManager)



#### Methods

[setScreen(screen)](#setScreen-Screen-)
A


[onJoinWorld(world, worldEntryReason, ci)](#onJoinWorld-ClientWorld-DownloadingTerrainScreen$WorldEntryReason-CallbackInfo-)


[onOpenScreen(screen, info)](#onOpenScreen-Screen-CallbackInfo-)


[afterOpenScreen(screen, info)](#afterOpenScreen-Screen-CallbackInfo-)


[onDisconnect(s, transferring, ci)](#onDisconnect-Screen-boolean-CallbackInfo-)



### Fields

#### .currentScreen


##### Type: [Screen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/Screen)



#### .interactionManager


##### Type: [ClientPlayerInteractionManager](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/network/ClientPlayerInteractionManager)



### Methods

#### .setScreen(screen)

Abstract
| Parameter | Type | Description |
|---|---|---|
| screen | Screen |  |

##### Returns: void



#### .onJoinWorld(world, worldEntryReason, ci)

| Parameter | Type | Description |
|---|---|---|
| world | ClientWorld |  |
| worldEntryReason | DownloadingTerrainScreen$WorldEntryReason |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onOpenScreen(screen, info)

| Parameter | Type | Description |
|---|---|---|
| screen | Screen |  |
| info | CallbackInfo |  |

##### Returns: void



#### .afterOpenScreen(screen, info)

| Parameter | Type | Description |
|---|---|---|
| screen | Screen |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onDisconnect(s, transferring, ci)

| Parameter | Type | Description |
|---|---|---|
| s | Screen |  |
| transferring | boolean |  |
| ci | CallbackInfo |  |

##### Returns: void




