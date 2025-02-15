

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper
---------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[GameOptions](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/option/GameOptions)>

1.8.4

### Constructors

#### new OptionsHelper (options)

| Parameter | Type | Description |
|---|---|---|
| options | GameOptions |  |



#### Fields

[skin](#skin)
F


[video](#video)
F


[music](#music)
F


[control](#control)
F


[chat](#chat)
F


[accessibility](#accessibility)
F



#### Methods

[getSkinOptions()](#getSkinOptions-)


[getVideoOptions()](#getVideoOptions-)


[getMusicOptions()](#getMusicOptions-)


[getControlOptions()](#getControlOptions-)


[getChatOptions()](#getChatOptions-)


[getAccessibilityOptions()](#getAccessibilityOptions-)


[saveOptions()](#saveOptions-)


[getResourcePacks()](#getResourcePacks-)


[getEnabledResourcePacks()](#getEnabledResourcePacks-)


[setEnabledResourcePacks(enabled)](#setEnabledResourcePacks-String[]-)


[removeServerResourcePack(state)](#removeServerResourcePack-boolean-)


[getLanguage()](#getLanguage-)


[setLanguage(languageCode)](#setLanguage-String-)


[getDifficulty()](#getDifficulty-)


[setDifficulty(name)](#setDifficulty-String-)


[isDifficultyLocked()](#isDifficultyLocked-)


[lockDifficulty()](#lockDifficulty-)


[unlockDifficulty()](#unlockDifficulty-)


[getFov()](#getFov-)


[setFov(fov)](#setFov-int-)


[getCameraMode()](#getCameraMode-)


[setCameraMode(mode)](#setCameraMode-int-)


[getSmoothCamera()](#getSmoothCamera-)


[setSmoothCamera(val)](#setSmoothCamera-boolean-)


[getWidth()](#getWidth-)


[getHeight()](#getHeight-)


[setWidth(w)](#setWidth-int-)


[setHeight(h)](#setHeight-int-)


[setSize(w, h)](#setSize-int-int-)


[getCloudMode()](#getCloudMode-)
D


[setCloudMode(mode)](#setCloudMode-int-)
D


[getGraphicsMode()](#getGraphicsMode-)
D


[setGraphicsMode(mode)](#setGraphicsMode-int-)
D


[isRightHanded()](#isRightHanded-)
D


[setRightHanded(val)](#setRightHanded-boolean-)
D


[getRenderDistance()](#getRenderDistance-)
D


[setRenderDistance(d)](#setRenderDistance-int-)
D


[getGamma()](#getGamma-)
D


[setGamma(gamma)](#setGamma-double-)
D


[setVolume(vol)](#setVolume-double-)
D


[setVolume(category, volume)](#setVolume-String-double-)
D


[getVolumes()](#getVolumes-)
D


[setGuiScale(scale)](#setGuiScale-int-)
D


[getGuiScale()](#getGuiScale-)
D


[getVolume(category)](#getVolume-String-)
D



### Fields

#### .skin

Final

##### Type: [OptionsHelper$SkinOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.SkinOptionsHelper.html)



#### .video

Final

##### Type: [OptionsHelper$VideoOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.VideoOptionsHelper.html)



#### .music

Final

##### Type: [OptionsHelper$MusicOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.MusicOptionsHelper.html)



#### .control

Final

##### Type: [OptionsHelper$ControlOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.ControlOptionsHelper.html)



#### .chat

Final

##### Type: [OptionsHelper$ChatOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.ChatOptionsHelper.html)



#### .accessibility

Final

##### Type: [OptionsHelper$AccessibilityOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.AccessibilityOptionsHelper.html)



### Methods

#### .getSkinOptions()

1.8.4


##### Returns: [OptionsHelper$SkinOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.SkinOptionsHelper.html)

a helper for the skin options.



#### .getVideoOptions()

1.8.4


##### Returns: [OptionsHelper$VideoOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.VideoOptionsHelper.html)

a helper for the video options.



#### .getMusicOptions()

1.8.4


##### Returns: [OptionsHelper$MusicOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.MusicOptionsHelper.html)

a helper for the music options.



#### .getControlOptions()

1.8.4


##### Returns: [OptionsHelper$ControlOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.ControlOptionsHelper.html)

a helper for the control options.



#### .getChatOptions()

1.8.4


##### Returns: [OptionsHelper$ChatOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.ChatOptionsHelper.html)

a helper for the chat options.



#### .getAccessibilityOptions()

1.8.4


##### Returns: [OptionsHelper$AccessibilityOptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.AccessibilityOptionsHelper.html)

a helper for the accessibility options.



#### .saveOptions()

1.8.4


##### Returns: [OptionsHelper](#)

self for chaining.



#### .getResourcePacks()

1.1.7


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

list of names of resource packs.



#### .getEnabledResourcePacks()

1.2.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

list of names of enabled resource packs.



#### .setEnabledResourcePacks(enabled)

1.2.0

Set the enabled resource packs to the provided list.

| Parameter | Type | Description |
|---|---|---|
| enabled | String[] |  |

##### Returns: [OptionsHelper](#)

self for chaining.



#### .removeServerResourcePack(state)

1.8.3

| Parameter | Type | Description |
|---|---|---|
| state | boolean | false to put it back |

##### Returns: [OptionsHelper](#)



#### .getLanguage()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the active language.



#### .setLanguage(languageCode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| languageCode | String | the language to change to |

##### Returns: [OptionsHelper](#)

self for chaining.



#### .getDifficulty()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the active difficulty.



#### .setDifficulty(name)

1.8.4

The name be either "peaceful", "easy", "normal", or "hard".

| Parameter | Type | Description |
|---|---|---|
| name | String | the name of the difficulty to change to |

##### Returns: [OptionsHelper](#)

self for chaining.



#### .isDifficultyLocked()

1.8.4


##### Returns: boolean

`true` if the difficulty is locked, `false` otherwise.



#### .lockDifficulty()

1.8.4


##### Returns: [OptionsHelper](#)

self for chaining.



#### .unlockDifficulty()

1.8.4

Unlocks the difficulty of the world. This can't be done in an unmodified client.


##### Returns: [OptionsHelper](#)

self for chaining.



#### .getFov()

1.1.7


##### Returns: int

the current fov value.



#### .setFov(fov)

1.1.7

| Parameter | Type | Description |
|---|---|---|
| fov | int | the new fov value |

##### Returns: [OptionsHelper](#)

self for chaining.



#### .getCameraMode()

1.5.0


##### Returns: int

0 for 1st person, 2 for in front.



#### .setCameraMode(mode)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| mode | int | 0: first, 2: front |

##### Returns: [OptionsHelper](#)



#### .getSmoothCamera()

1.5.0


##### Returns: boolean



#### .setSmoothCamera(val)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| val | boolean |  |

##### Returns: [OptionsHelper](#)



#### .getWidth()

1.2.6


##### Returns: int



#### .getHeight()

1.2.6


##### Returns: int



#### .setWidth(w)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| w | int |  |

##### Returns: [OptionsHelper](#)



#### .setHeight(h)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| h | int |  |

##### Returns: [OptionsHelper](#)



#### .setSize(w, h)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| w | int |  |
| h | int |  |

##### Returns: [OptionsHelper](#)



#### .getCloudMode()

Deprecated

1.1.7


##### Returns: int

0: off, 2: fancy



#### .setCloudMode(mode)

Deprecated

1.1.7

| Parameter | Type | Description |
|---|---|---|
| mode | int | 0: off, 2: fancy |

##### Returns: [OptionsHelper](#)



#### .getGraphicsMode()

Deprecated

1.1.7


##### Returns: int



#### .setGraphicsMode(mode)

Deprecated

1.1.7

| Parameter | Type | Description |
|---|---|---|
| mode | int | 0: fast, 2: fabulous |

##### Returns: [OptionsHelper](#)



#### .isRightHanded()

Deprecated

1.1.7


##### Returns: boolean



#### .setRightHanded(val)

Deprecated

1.1.7

| Parameter | Type | Description |
|---|---|---|
| val | boolean |  |

##### Returns: [OptionsHelper](#)



#### .getRenderDistance()

Deprecated

1.1.7


##### Returns: int



#### .setRenderDistance(d)

Deprecated

1.1.7

| Parameter | Type | Description |
|---|---|---|
| d | int |  |

##### Returns: [OptionsHelper](#)



#### .getGamma()

Deprecated

1.3.0 normal values for gamma are between `0` and `1`


##### Returns: double



#### .setGamma(gamma)

Deprecated

1.3.0 normal values for gamma are between `0` and `1`

| Parameter | Type | Description |
|---|---|---|
| gamma | double |  |

##### Returns: [OptionsHelper](#)



#### .setVolume(vol)

Deprecated

1.3.1

| Parameter | Type | Description |
|---|---|---|
| vol | double |  |

##### Returns: [OptionsHelper](#)



#### .setVolume(category, volume)

Deprecated

1.3.1

set volume by category.

| Parameter | Type | Description |
|---|---|---|
| category | String |  |
| volume | double |  |

##### Returns: [OptionsHelper](#)



#### .getVolumes()

Deprecated

1.3.1


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Float](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Float.html)>



#### .setGuiScale(scale)

Deprecated

1.3.1

sets gui scale, `0` for auto.

| Parameter | Type | Description |
|---|---|---|
| scale | int |  |

##### Returns: [OptionsHelper](#)



#### .getGuiScale()

Deprecated

1.3.1


##### Returns: int

gui scale, `0` for auto.



#### .getVolume(category)

Deprecated

1.3.1

| Parameter | Type | Description |
|---|---|---|
| category | String |  |

##### Returns: float




