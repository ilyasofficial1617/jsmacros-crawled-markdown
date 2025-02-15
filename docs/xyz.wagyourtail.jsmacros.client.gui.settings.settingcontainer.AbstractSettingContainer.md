
[AbstractMapSettingContainer](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/AbstractMapSettingContainer.html)<

T

, 

U

 **extends** 

[AbstractMapSettingContainer$MapSettingEntry](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/AbstractMapSettingContainer.MapSettingEntry.html)<

T

>> [ColorMapSetting](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/ColorMapSetting.html) [ProfileSetting](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/ProfileSetting.html) [StringMapSetting](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/StringMapSetting.html) [PrimitiveSettingGroup](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/PrimitiveSettingGroup.html) [FileMapSetting](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingcontainer/FileMapSetting.html)

xyz.wagyourtail.jsmacros.client.gui.settings.settingcontainer.AbstractSettingContainer
--------------------------------------------------------------------------------------

Abstract
#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[SettingsOverlay](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/SettingsOverlay.html)>

### Constructors

#### new AbstractSettingContainer (x, y, width, height, textRenderer, parent, group)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| parent | SettingsOverlay |  |
| group | String[] |  |



#### Fields

[group](#group)
F


[scroll](#scroll)



#### Methods

[addSetting(setting)](#addSetting-SettingsOverlay$SettingField-)
A



### Fields

#### .group

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]



#### .scroll


##### Type: [Scrollbar](1.9.2/xyz/wagyourtail/wagyourgui/elements/Scrollbar.html)



### Methods

#### .addSetting(setting)

Abstract
| Parameter | Type | Description |
|---|---|---|
| setting | SettingsOverlay$SettingField<?> |  |

##### Returns: void




