

xyz.wagyourtail.jsmacros.client.api.helpers.OptionsHelper$AccessibilityOptionsHelper
------------------------------------------------------------------------------------

#### 

### Constructors

#### new OptionsHelper$AccessibilityOptionsHelper (OptionsHelper)

| Parameter | Type | Description |
|---|---|---|
| OptionsHelper | OptionsHelper |  |



#### Fields

[parent](#parent)
F



#### Methods

[getParent()](#getParent-)


[getNarratorMode()](#getNarratorMode-)


[setNarratorMode(mode)](#setNarratorMode-String-)


[areSubtitlesShown()](#areSubtitlesShown-)


[showSubtitles(val)](#showSubtitles-boolean-)


[setTextBackgroundOpacity(val)](#setTextBackgroundOpacity-double-)


[getTextBackgroundOpacity()](#getTextBackgroundOpacity-)


[isBackgroundForChatOnly()](#isBackgroundForChatOnly-)


[enableBackgroundForChatOnly(val)](#enableBackgroundForChatOnly-boolean-)


[getChatOpacity()](#getChatOpacity-)


[setChatOpacity(val)](#setChatOpacity-double-)


[getChatLineSpacing()](#getChatLineSpacing-)


[setChatLineSpacing(val)](#setChatLineSpacing-double-)


[getChatDelay()](#getChatDelay-)


[setChatDelay(val)](#setChatDelay-double-)


[isAutoJumpEnabled()](#isAutoJumpEnabled-)


[enableAutoJump(val)](#enableAutoJump-boolean-)


[isSneakTogglingEnabled()](#isSneakTogglingEnabled-)


[toggleSneak(val)](#toggleSneak-boolean-)


[isSprintTogglingEnabled()](#isSprintTogglingEnabled-)


[toggleSprint(val)](#toggleSprint-boolean-)


[getDistortionEffect()](#getDistortionEffect-)


[setDistortionEffect(val)](#setDistortionEffect-double-)


[getFovEffect()](#getFovEffect-)


[setFovEffect(val)](#setFovEffect-double-)


[isMonochromeLogoEnabled()](#isMonochromeLogoEnabled-)


[enableMonochromeLogo(val)](#enableMonochromeLogo-boolean-)


[areLightningFlashesHidden()](#areLightningFlashesHidden-)


[setFovEffect(val)](#setFovEffect-boolean-)



### Fields

#### .parent

Final

##### Type: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)



### Methods

#### .getParent()

1.8.4


##### Returns: [OptionsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/OptionsHelper.html)

the parent options helper.



#### .getNarratorMode()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the current narrator mode.



#### .setNarratorMode(mode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| mode | String | the mode to set the narrator to. Must be either "OFF", "ALL", "CHAT", or
                                     "SYSTEM" |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .areSubtitlesShown()

1.8.4


##### Returns: boolean

`true` if subtitles are enabled.



#### .showSubtitles(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to show subtitles or not |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .setTextBackgroundOpacity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new opacity for the text background |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getTextBackgroundOpacity()

1.8.4


##### Returns: double

the opacity of the text background.



#### .isBackgroundForChatOnly()

1.8.4


##### Returns: boolean



#### .enableBackgroundForChatOnly(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean |  |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getChatOpacity()

1.8.4


##### Returns: double

the current chat opacity.



#### .setChatOpacity(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat opacity |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getChatLineSpacing()

1.8.4


##### Returns: double

the current chat line spacing.



#### .setChatLineSpacing(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat line spacing |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getChatDelay()

1.8.4


##### Returns: double

the current chat delay in seconds.



#### .setChatDelay(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new chat delay in seconds |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .isAutoJumpEnabled()

1.8.4


##### Returns: boolean

`true` if auto jump is enabled, `false` otherwise.



#### .enableAutoJump(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable auto jump or not or not |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .isSneakTogglingEnabled()

1.8.4


##### Returns: boolean

`true` if the toggle functionality for sneaking is enabled, `false`
otherwise.



#### .toggleSneak(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable or disable the toggle functionality for sneaking |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .isSprintTogglingEnabled()

1.8.4


##### Returns: boolean

`true` if the toggle functionality for sprinting is enabled, `false`
otherwise.



#### .toggleSprint(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable or disable the toggle functionality for sprinting |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getDistortionEffect()

1.8.4


##### Returns: double

the current distortion effect scale.



#### .setDistortionEffect(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new distortion effect scale |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .getFovEffect()

1.8.4


##### Returns: double

the current fov effect scale.



#### .setFovEffect(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | double | the new fov effect scale |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.



#### .isMonochromeLogoEnabled()

1.8.4


##### Returns: boolean

`true` if the monochrome logo is enabled, `false` otherwise.



#### .enableMonochromeLogo(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | whether to enable the monochrome logo or not |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

the current helper instance for chaining.



#### .areLightningFlashesHidden()

1.8.4


##### Returns: boolean

`true` if lighting flashes are hidden, `false` otherwise.



#### .setFovEffect(val)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| val | boolean | the new fov value |

##### Returns: [OptionsHelper$AccessibilityOptionsHelper](#)

self for chaining.




