

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper$MusicOptionsHelper
----------------------------------------------------------------------------

#### 

### Constructors

#### new OptionsHelper$MusicOptionsHelper (OptionsHelper)

| Parameter | Type | Description |
|---|---|---|
| OptionsHelper | OptionsHelper |  |



#### Fields

[parent](#parent)
F



#### Methods

[getParent()](#getParent-)


[getMasterVolume()](#getMasterVolume-)


[setMasterVolume(volume)](#setMasterVolume-double-)


[getMusicVolume()](#getMusicVolume-)


[setMusicVolume(volume)](#setMusicVolume-double-)


[getRecordsVolume()](#getRecordsVolume-)


[setRecordsVolume(volume)](#setRecordsVolume-double-)


[getWeatherVolume()](#getWeatherVolume-)


[setWeatherVolume(volume)](#setWeatherVolume-double-)


[getBlocksVolume()](#getBlocksVolume-)


[setBlocksVolume(volume)](#setBlocksVolume-double-)


[getHostileVolume()](#getHostileVolume-)


[setHostileVolume(volume)](#setHostileVolume-double-)


[getNeutralVolume()](#getNeutralVolume-)


[setNeutralVolume(volume)](#setNeutralVolume-double-)


[getPlayerVolume()](#getPlayerVolume-)


[setPlayerVolume(volume)](#setPlayerVolume-double-)


[getAmbientVolume()](#getAmbientVolume-)


[setAmbientVolume(volume)](#setAmbientVolume-double-)


[getVoiceVolume()](#getVoiceVolume-)


[setVoiceVolume(volume)](#setVoiceVolume-double-)


[getVolume(category)](#getVolume-String-)


[getVolumes()](#getVolumes-)


[setVolume(category, volume)](#setVolume-String-double-)


[getSoundDevice()](#getSoundDevice-)


[setSoundDevice(audioDevice)](#setSoundDevice-String-)


[getAudioDevices()](#getAudioDevices-)


[areSubtitlesShown()](#areSubtitlesShown-)


[showSubtitles(val)](#showSubtitles-boolean-)



### Fields

#### .parent

Final

##### Type: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)



### Methods

#### .getParent()

1.8.4


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

the parent options helper.



#### .getMasterVolume()

1.8.4


##### Returns: float

the current master volume.



#### .setMasterVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new master volume |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getMusicVolume()

1.8.4


##### Returns: float

the current music volume.



#### .setMusicVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new music volume |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getRecordsVolume()

1.8.4


##### Returns: float

the current value of played recods.



#### .setRecordsVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new volume for playing records |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getWeatherVolume()

1.8.4


##### Returns: float

the current volume of the weather.



#### .setWeatherVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new volume for the weather |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getBlocksVolume()

1.8.4


##### Returns: float

the current volume of block related sounds.



#### .setBlocksVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new volume for block sounds |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getHostileVolume()

1.8.4


##### Returns: float

the current volume of hostile mobs.



#### .setHostileVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new volume for hostile mobs |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getNeutralVolume()

1.8.4


##### Returns: float

the current volume of neutral mobs.



#### .setNeutralVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new volume for neutral mobs |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getPlayerVolume()

1.8.4


##### Returns: float

the current player volume.



#### .setPlayerVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new player volume |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getAmbientVolume()

1.8.4


##### Returns: float

the current ambient volume.



#### .setAmbientVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double | the new ambient volume |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getVoiceVolume()

1.8.4


##### Returns: float

the current voice volume.



#### .setVoiceVolume(volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| volume | double |  |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getVolume(category)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| category | String | the category to get the volume of |

##### Returns: float

the volume of the given sound category.



#### .getVolumes()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Float](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Float.html)>

a map of all sound categories and their volumes.



#### .setVolume(category, volume)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| category | String | the category to set the volume for |
| volume | double | the new volume |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getSoundDevice()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the currently selected sound device.



#### .setSoundDevice(audioDevice)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| audioDevice | String | the audio device to use |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.



#### .getAudioDevices()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all connected audio devices.



#### .areSubtitlesShown()

1.8.4


##### Returns: boolean

`true` if subtitles should be shown, `false` otherwise.



#### .showSubtitles(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether subtitles should be shown or not |

##### Returns: [OptionsHelper$MusicOptionsHelper](#)

self for chaining.




