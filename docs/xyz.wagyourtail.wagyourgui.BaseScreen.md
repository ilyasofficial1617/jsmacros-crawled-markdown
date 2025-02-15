
[ScriptScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/ScriptScreen.html) [KeyMacrosScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/KeyMacrosScreen.html) [CancelScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/CancelScreen.html) [EventMacrosScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/EventMacrosScreen.html) [ServiceScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/ServiceScreen.html) [EditorScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/EditorScreen.html) [MacroScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/MacroScreen.html)

xyz.wagyourtail.wagyourgui.BaseScreen
-------------------------------------

Abstract
#### extends [Screen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/Screen) implements [IOverlayParent](1.9.2/xyz/wagyourtail/wagyourgui/overlays/IOverlayParent.html)

#### Methods

[trimmed(textRenderer, str, width)](#trimmed-TextRenderer-StringVisitable-int-)
S


[setParent(parent)](#setParent-Screen-)


[reload()](#reload-)


[removed()](#removed-)


[openOverlay(overlay)](#openOverlay-OverlayContainer-)


[getFirstOverlayParent()](#getFirstOverlayParent-)


[getChildOverlay()](#getChildOverlay-)


[openOverlay(overlay, disableButtons)](#openOverlay-OverlayContainer-boolean-)


[closeOverlay(overlay)](#closeOverlay-OverlayContainer-)


[remove(btn)](#remove-Element-)


[addDrawableChild(drawableElement)](#addDrawableChild-T-)


[setFocused(focused)](#setFocused-Element-)


[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[mouseScrolled(mouseX, mouseY, horiz, vert)](#mouseScrolled-double-double-double-double-)


[mouseClicked(mouseX, mouseY, button)](#mouseClicked-double-double-int-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[shouldCloseOnEsc()](#shouldCloseOnEsc-)


[updateSettings()](#updateSettings-)


[close()](#close-)


[openParent()](#openParent-)



### Methods

#### .trimmed(textRenderer, str, width)

Static
| Parameter | Type | Description |
|---|---|---|
| textRenderer | TextRenderer |  |
| str | StringVisitable |  |
| width | int |  |

##### Returns: [OrderedText](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/OrderedText)



#### .setParent(parent)

| Parameter | Type | Description |
|---|---|---|
| parent | Screen |  |

##### Returns: void



#### .reload()


##### Returns: void



#### .removed()


##### Returns: void



#### .openOverlay(overlay)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |

##### Returns: void



#### .getFirstOverlayParent()


##### Returns: [IOverlayParent](1.9.2/xyz/wagyourtail/wagyourgui/overlays/IOverlayParent.html)



#### .getChildOverlay()


##### Returns: [OverlayContainer](1.9.2/xyz/wagyourtail/wagyourgui/overlays/OverlayContainer.html)



#### .openOverlay(overlay, disableButtons)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |
| disableButtons | boolean |  |

##### Returns: void



#### .closeOverlay(overlay)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |

##### Returns: void



#### .remove(btn)

| Parameter | Type | Description |
|---|---|---|
| btn | Element |  |

##### Returns: void



#### .addDrawableChild< T **extends** >(drawableElement)

| Parameter | Type | Description |
|---|---|---|
| drawableElement | T
                             extends |  |

##### Returns: T **extends**



#### .setFocused(focused)

| Parameter | Type | Description |
|---|---|---|
| focused | Element |  |

##### Returns: void



#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean



#### .mouseScrolled(mouseX, mouseY, horiz, vert)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| horiz | double |  |
| vert | double |  |

##### Returns: boolean



#### .mouseClicked(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: boolean



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .shouldCloseOnEsc()


##### Returns: boolean



#### .updateSettings()


##### Returns: void



#### .close()


##### Returns: void



#### .openParent()


##### Returns: void




