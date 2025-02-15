

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper$VideoOptionsHelper
----------------------------------------------------------------------------

#### 

### Constructors

#### new OptionsHelper$VideoOptionsHelper (OptionsHelper)

| Parameter | Type | Description |
|---|---|---|
| OptionsHelper | OptionsHelper |  |



#### Fields

[parent](#parent)
F



#### Methods

[getParent()](#getParent-)


[getFullscreenResolution()](#getFullscreenResolution-)


[getBiomeBlendRadius()](#getBiomeBlendRadius-)


[setBiomeBlendRadius(radius)](#setBiomeBlendRadius-int-)


[getGraphicsMode()](#getGraphicsMode-)


[setGraphicsMode(mode)](#setGraphicsMode-String-)


[getChunkBuilderMode()](#getChunkBuilderMode-)


[setChunkBuilderMode(mode)](#setChunkBuilderMode-String-)


[getSmoothLightningMode()](#getSmoothLightningMode-)


[setSmoothLightningMode(mode)](#setSmoothLightningMode-boolean-)


[getRenderDistance()](#getRenderDistance-)


[setRenderDistance(radius)](#setRenderDistance-int-)


[getSimulationDistance()](#getSimulationDistance-)


[setSimulationDistance(radius)](#setSimulationDistance-int-)


[getMaxFps()](#getMaxFps-)


[setMaxFps(maxFps)](#setMaxFps-int-)


[isVsyncEnabled()](#isVsyncEnabled-)


[enableVsync(val)](#enableVsync-boolean-)


[isViewBobbingEnabled()](#isViewBobbingEnabled-)


[enableViewBobbing(val)](#enableViewBobbing-boolean-)


[getGuiScale()](#getGuiScale-)


[setGuiScale(scale)](#setGuiScale-int-)


[getAttackIndicatorType()](#getAttackIndicatorType-)


[setAttackIndicatorType(type)](#setAttackIndicatorType-String-)


[getGamma()](#getGamma-)


[setGamma(gamma)](#setGamma-double-)


[getBrightness()](#getBrightness-)


[setBrightness(gamma)](#setBrightness-double-)


[getCloudsMode()](#getCloudsMode-)


[setCloudsMode(mode)](#setCloudsMode-String-)


[isFullscreen()](#isFullscreen-)


[setFullScreen(fullscreen)](#setFullScreen-boolean-)


[getParticleMode()](#getParticleMode-)


[setParticleMode(mode)](#setParticleMode-String-)


[getMipMapLevels()](#getMipMapLevels-)


[setMipMapLevels(val)](#setMipMapLevels-int-)


[areEntityShadowsEnabled()](#areEntityShadowsEnabled-)


[enableEntityShadows(val)](#enableEntityShadows-boolean-)


[getDistortionEffect()](#getDistortionEffect-)


[setDistortionEffects(val)](#setDistortionEffects-double-)


[getEntityDistance()](#getEntityDistance-)


[setEntityDistance(val)](#setEntityDistance-double-)


[getFovEffects()](#getFovEffects-)


[setFovEffects(val)](#setFovEffects-double-)


[isAutosaveIndicatorEnabled()](#isAutosaveIndicatorEnabled-)


[enableAutosaveIndicator(val)](#enableAutosaveIndicator-boolean-)



### Fields

#### .parent

Final

##### Type: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)



### Methods

#### .getParent()

1.8.4


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

the parent options helper.



#### .getFullscreenResolution()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the full screen resolution as a string.



#### .getBiomeBlendRadius()

1.8.4


##### Returns: int

the current biome blend radius.



#### .setBiomeBlendRadius(radius)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| radius | int | the new biome blend radius |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getGraphicsMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the selected graphics mode.



#### .setGraphicsMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the graphics mode to select. Must be either "fast", "fancy" or "fabulous" |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getChunkBuilderMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the selected chunk builder mode.



#### .setChunkBuilderMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the chunk builder mode to select. Must be either "none", "nearby" or
                                     "player_affected" |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getSmoothLightningMode()

1.8.4


##### Returns: boolean

the selected smooth lightning mode.



#### .setSmoothLightningMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | boolean | the smooth lightning mode to select. boolean value |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getRenderDistance()

1.8.4


##### Returns: int

the current render distance in chunks.



#### .setRenderDistance(radius)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| radius | int | the new render distance in chunks |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getSimulationDistance()

1.8.4


##### Returns: int

the current simulation distance in chunks.



#### .setSimulationDistance(radius)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| radius | int | the new simulation distance in chunks |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getMaxFps()

1.8.4


##### Returns: int

the current upper fps limit.



#### .setMaxFps(maxFps)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| maxFps | int | the new maximum fps limit |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .isVsyncEnabled()

1.8.4


##### Returns: boolean

`true` if vsync is enabled, `false` otherwise.



#### .enableVsync(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable vsync or not |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .isViewBobbingEnabled()

1.8.4


##### Returns: boolean

`true` if view bobbing is enabled, `false` otherwise.



#### .enableViewBobbing(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable view bobbing or not |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getGuiScale()

1.8.4


##### Returns: int

the current gui scale.



#### .setGuiScale(scale)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| scale | int | the gui scale to set. Must be 1, 2, 3 or 4 |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getAttackIndicatorType()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current attack indicator type.



#### .setAttackIndicatorType(type)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| type | String | the attack indicator type. Must be either "off", "crosshair", or "hotbar" |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getGamma()

1.8.4


##### Returns: double

the current gamma value.



#### .setGamma(gamma)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| gamma | double | the new gamma value |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getBrightness()

1.8.4


##### Returns: double

the current brightness value.



#### .setBrightness(gamma)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| gamma | double | the new brightness value |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getCloudsMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current cloud rendering mode.



#### .setCloudsMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the cloud rendering mode to select. Must be either "off", "fast" or "fancy" |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .isFullscreen()

1.8.4


##### Returns: boolean

`true` if the game is running in fullscreen mode, `false` otherwise.



#### .setFullScreen(fullscreen)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| fullscreen | boolean | whether to enable fullscreen mode or not |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getParticleMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current particle rendering mode.



#### .setParticleMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the particle rendering mode to select. Must be either "minimal", "decreased"
                                     or "all" |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getMipMapLevels()

1.8.4


##### Returns: int

the current mip map level.



#### .setMipMapLevels(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | int | the new mip map level |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .areEntityShadowsEnabled()

1.8.4


##### Returns: boolean

`true` if entity shadows should be rendered, `false` otherwise.



#### .enableEntityShadows(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable entity shadows or not |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getDistortionEffect()

1.8.4


##### Returns: double

the current distortion effect scale.



#### .setDistortionEffects(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new distortion effect scale |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getEntityDistance()

1.8.4


##### Returns: double

the current entity render distance.



#### .setEntityDistance(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new entity render distance |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .getFovEffects()

1.8.4


##### Returns: double

the current fov value.



#### .setFovEffects(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new fov value |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.



#### .isAutosaveIndicatorEnabled()

1.8.4


##### Returns: boolean

`true` if the autosave indicator is enabled, `false` otherwise.



#### .enableAutosaveIndicator(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean |  |

##### Returns: [OptionsHelper$VideoOptionsHelper](#)

self for chaining.




