

xyz.wagyourtail.jsmacros.client.gui.settings.settingfields.FileField
--------------------------------------------------------------------

#### extends [AbstractSettingField](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/settingfields/AbstractSettingField.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

### Constructors

#### new FileField (x, y, width, textRenderer, parent, field)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| textRenderer | TextRenderer |  |
| parent | AbstractSettingContainer |  |
| field | SettingsOverlay$SettingField<String> |  |



#### Methods

[getTopLevel(setting)](#getTopLevel-SettingsOverlay$SettingField-)
S


[relativize(setting, file)](#relativize-SettingsOverlay$SettingField-File-)
S


[init()](#init-)


[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Methods

#### .getTopLevel(setting)

Static
| Parameter | Type | Description |
|---|---|---|
| setting | SettingsOverlay$SettingField<?> |  |

##### Returns: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .relativize(setting, file)

Static
| Parameter | Type | Description |
|---|---|---|
| setting | SettingsOverlay$SettingField<?> |  |
| file | File |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



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



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




