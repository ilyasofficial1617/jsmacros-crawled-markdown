

xyz.wagyourtail.jsmacros.client.mixins.events.MixinClientPlayNetworkHandler
---------------------------------------------------------------------------

Abstract
#### extends [ClientCommonNetworkHandler](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/network/ClientCommonNetworkHandler)

#### Methods

[onPlayerList(packet, ci, var2, entry, playerListEntry)](#onPlayerList-PlayerListS2CPacket-CallbackInfo-Iterator-PlayerListS2CPacket$Entry-PlayerListEntry-)


[onPlayerListEnd(packet, ci, var2, uUID, playerListEntry)](#onPlayerListEnd-PlayerRemoveS2CPacket-CallbackInfo-Iterator-UUID-PlayerListEntry-)


[onTitle(title)](#onTitle-Text-)


[onSubtitle(title)](#onSubtitle-Text-)


[onBossBar(packet, info)](#onBossBar-BossBarS2CPacket-CallbackInfo-)


[onItemPickupAnimation(packet, info)](#onItemPickupAnimation-ItemPickupAnimationS2CPacket-CallbackInfo-)


[onGameJoin(packet, info)](#onGameJoin-GameJoinS2CPacket-CallbackInfo-)


[onChunkData(packet, info)](#onChunkData-ChunkDataS2CPacket-CallbackInfo-)


[onBlockUpdate(packet, info)](#onBlockUpdate-BlockUpdateS2CPacket-CallbackInfo-)


[onChunkDeltaUpdate(packet, info)](#onChunkDeltaUpdate-ChunkDeltaUpdateS2CPacket-CallbackInfo-)


[onBlockEntityUpdate(packet, info)](#onBlockEntityUpdate-BlockEntityUpdateS2CPacket-CallbackInfo-)


[onUnloadChunk(packet, info)](#onUnloadChunk-UnloadChunkS2CPacket-CallbackInfo-)


[onEntityStatusEffect(packet, info)](#onEntityStatusEffect-EntityStatusEffectS2CPacket-CallbackInfo-)


[onEntityStatusEffect(packet, info)](#onEntityStatusEffect-RemoveEntityStatusEffectS2CPacket-CallbackInfo-)


[onHeldSlotUpdate(packet, ci)](#onHeldSlotUpdate-ScreenHandlerSlotUpdateS2CPacket-CallbackInfo-)


[onInventorySlotUpdate(packet, ci)](#onInventorySlotUpdate-ScreenHandlerSlotUpdateS2CPacket-CallbackInfo-)


[onScreenSlotUpdate(packet, ci)](#onScreenSlotUpdate-ScreenHandlerSlotUpdateS2CPacket-CallbackInfo-)


[onScreenSlotUpdate2(packet, ci)](#onScreenSlotUpdate2-ScreenHandlerSlotUpdateS2CPacket-CallbackInfo-)


[onInventoryUpdate(packet, ci)](#onInventoryUpdate-InventoryS2CPacket-CallbackInfo-)



### Methods

#### .onPlayerList(packet, ci, var2, entry, playerListEntry)

| Parameter | Type | Description |
|---|---|---|
| packet | PlayerListS2CPacket |  |
| ci | CallbackInfo |  |
| var2 | Iterator |  |
| entry | PlayerListS2CPacket$Entry |  |
| playerListEntry | PlayerListEntry |  |

##### Returns: void



#### .onPlayerListEnd(packet, ci, var2, uUID, playerListEntry)

| Parameter | Type | Description |
|---|---|---|
| packet | PlayerRemoveS2CPacket |  |
| ci | CallbackInfo |  |
| var2 | Iterator |  |
| uUID | UUID |  |
| playerListEntry | PlayerListEntry |  |

##### Returns: void



#### .onTitle(title)

| Parameter | Type | Description |
|---|---|---|
| title | Text |  |

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .onSubtitle(title)

| Parameter | Type | Description |
|---|---|---|
| title | Text |  |

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .onBossBar(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | BossBarS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onItemPickupAnimation(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | ItemPickupAnimationS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onGameJoin(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | GameJoinS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onChunkData(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | ChunkDataS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onBlockUpdate(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | BlockUpdateS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onChunkDeltaUpdate(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | ChunkDeltaUpdateS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onBlockEntityUpdate(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | BlockEntityUpdateS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onUnloadChunk(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | UnloadChunkS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onEntityStatusEffect(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | EntityStatusEffectS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onEntityStatusEffect(packet, info)

| Parameter | Type | Description |
|---|---|---|
| packet | RemoveEntityStatusEffectS2CPacket |  |
| info | CallbackInfo |  |

##### Returns: void



#### .onHeldSlotUpdate(packet, ci)

| Parameter | Type | Description |
|---|---|---|
| packet | ScreenHandlerSlotUpdateS2CPacket |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onInventorySlotUpdate(packet, ci)

| Parameter | Type | Description |
|---|---|---|
| packet | ScreenHandlerSlotUpdateS2CPacket |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onScreenSlotUpdate(packet, ci)

| Parameter | Type | Description |
|---|---|---|
| packet | ScreenHandlerSlotUpdateS2CPacket |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onScreenSlotUpdate2(packet, ci)

| Parameter | Type | Description |
|---|---|---|
| packet | ScreenHandlerSlotUpdateS2CPacket |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onInventoryUpdate(packet, ci)

| Parameter | Type | Description |
|---|---|---|
| packet | InventoryS2CPacket |  |
| ci | CallbackInfo |  |

##### Returns: void




