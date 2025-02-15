

xyz.wagyourtail.jsmacros.client.access.BossBarConsumer
------------------------------------------------------

#### implements [BossBarS2CPacket$Consumer](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/s2c/play/BossBarS2CPacket$Consumer)

### Constructors

#### new BossBarConsumer ()




#### Methods

[add(uuid, name, percent, color, style, darkenSky, dragonMusic, thickenFog)](#add-UUID-Text-float-BossBar$Color-BossBar$Style-boolean-boolean-boolean-)


[remove(uuid)](#remove-UUID-)


[updateProgress(uuid, percent)](#updateProgress-UUID-float-)


[updateName(uuid, name)](#updateName-UUID-Text-)


[updateStyle(id, color, style)](#updateStyle-UUID-BossBar$Color-BossBar$Style-)


[updateProperties(uuid, darkenSky, dragonMusic, thickenFog)](#updateProperties-UUID-boolean-boolean-boolean-)



### Methods

#### .add(uuid, name, percent, color, style, darkenSky, dragonMusic, thickenFog)

| Parameter | Type | Description |
|---|---|---|
| uuid | UUID |  |
| name | Text |  |
| percent | float |  |
| color | BossBar$Color |  |
| style | BossBar$Style |  |
| darkenSky | boolean |  |
| dragonMusic | boolean |  |
| thickenFog | boolean |  |

##### Returns: void



#### .remove(uuid)

| Parameter | Type | Description |
|---|---|---|
| uuid | UUID |  |

##### Returns: void



#### .updateProgress(uuid, percent)

| Parameter | Type | Description |
|---|---|---|
| uuid | UUID |  |
| percent | float |  |

##### Returns: void



#### .updateName(uuid, name)

| Parameter | Type | Description |
|---|---|---|
| uuid | UUID |  |
| name | Text |  |

##### Returns: void



#### .updateStyle(id, color, style)

| Parameter | Type | Description |
|---|---|---|
| id | UUID |  |
| color | BossBar$Color |  |
| style | BossBar$Style |  |

##### Returns: void



#### .updateProperties(uuid, darkenSky, dragonMusic, thickenFog)

| Parameter | Type | Description |
|---|---|---|
| uuid | UUID |  |
| darkenSky | boolean |  |
| dragonMusic | boolean |  |
| thickenFog | boolean |  |

##### Returns: void




