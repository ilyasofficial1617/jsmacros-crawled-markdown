

xyz.wagyourtail.jsmacros.client.gui.containers.MacroContainer
-------------------------------------------------------------

#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[MacroScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/MacroScreen.html)>

### Constructors

#### new MacroContainer (x, y, width, height, textRenderer, macro, parent)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| macro | ScriptTrigger |  |
| parent | MacroScreen |  |



#### Methods

[getRawMacro()](#getRawMacro-)


[init()](#init-)


[setEventType(type)](#setEventType-String-)


[setFile(f)](#setFile-File-)


[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[onKey(translationKey)](#onKey-String-)


[buildKeyName(translationKeys)](#buildKeyName-String-)
S


[setKey(translationKeys)](#setKey-String-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Methods

#### .getRawMacro()


##### Returns: [ScriptTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/config/ScriptTrigger.html)



#### .init()


##### Returns: void



#### .setEventType(type)

| Parameter | Type | Description |
|---|---|---|
| type | String |  |

##### Returns: void



#### .setFile(f)

| Parameter | Type | Description |
|---|---|---|
| f | File |  |

##### Returns: void



#### .setPos(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: void



#### .onKey(translationKey)

| Parameter | Type | Description |
|---|---|---|
| translationKey | String |  |

##### Returns: boolean



#### .buildKeyName(translationKeys)

Static
| Parameter | Type | Description |
|---|---|---|
| translationKeys | String |  |

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .setKey(translationKeys)

| Parameter | Type | Description |
|---|---|---|
| translationKeys | String |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




