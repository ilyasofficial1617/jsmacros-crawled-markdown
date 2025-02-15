
[ColorMapSetting$ColorEntry](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/ColorMapSetting.ColorEntry.html) [ProfileSetting$ProfileEntry](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/ProfileSetting.ProfileEntry.html) [StringMapSetting$StringEntry](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/StringMapSetting.StringEntry.html) [FileMapSetting$FileEntry](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/FileMapSetting.FileEntry.html)

xyz.wagyourtail.jsmacros.client.gui.settings.settingcontainer.AbstractMapSettingContainer$MapSettingEntry< T >
--------------------------------------------------------------------------------------------------------------

Abstract
Static
#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[AbstractMapSettingContainer](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/AbstractMapSettingContainer.html)< T , [AbstractMapSettingContainer$MapSettingEntry](#)< T >>>

### Constructors

#### new AbstractMapSettingContainer$MapSettingEntry (x, y, width, textRenderer, parent, key, value)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| textRenderer | TextRenderer |  |
| parent | AbstractMapSettingContainer<T, AbstractMapSettingContainer$MapSettingEntry<T>> |  |
| key | String |  |
| value | T |  |



#### Methods

[init()](#init-)


[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[setKey(newKey)](#setKey-String-)


[setValue(newValue)](#setValue-T-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Methods

#### .init()


##### Returns: void



#### .setPos(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: void



#### .setKey(newKey)

| Parameter | Type | Description |
|---|---|---|
| newKey | String |  |

##### Returns: void



#### .setValue(newValue)

| Parameter | Type | Description |
|---|---|---|
| newValue | T |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




