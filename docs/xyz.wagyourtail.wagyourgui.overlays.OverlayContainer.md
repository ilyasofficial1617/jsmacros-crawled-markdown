
[TextPrompt](1.9.2/xyz/wagyourtail/wagyourgui/overlays/TextPrompt.html) [ConfirmOverlay](1.9.2/xyz/wagyourtail/wagyourgui/overlays/ConfirmOverlay.html) [SelectorDropdownOverlay](1.9.2/xyz/wagyourtail/wagyourgui/overlays/SelectorDropdownOverlay.html) [EventChooser](1.9.2/xyz/wagyourtail/jsmacros/client/gui/overlays/EventChooser.html) [FileChooser](1.9.2/xyz/wagyourtail/jsmacros/client/gui/overlays/FileChooser.html) [TextOverlay](1.9.2/xyz/wagyourtail/jsmacros/client/gui/overlays/TextOverlay.html) [AboutOverlay](1.9.2/xyz/wagyourtail/jsmacros/client/gui/overlays/AboutOverlay.html) [SettingsOverlay](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/SettingsOverlay.html)

xyz.wagyourtail.wagyourgui.overlays.OverlayContainer
----------------------------------------------------

Abstract
#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[IOverlayParent](1.9.2/xyz/wagyourtail/wagyourgui/overlays/IOverlayParent.html)> implements [IOverlayParent](1.9.2/xyz/wagyourtail/wagyourgui/overlays/IOverlayParent.html)

### Constructors

#### new OverlayContainer (x, y, width, height, textRenderer, parent)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| parent | IOverlayParent |  |



#### Fields

[savedBtnStates](#savedBtnStates)


[scroll](#scroll)



#### Methods

[remove(btn)](#remove-Element-)


[openOverlay(overlay)](#openOverlay-OverlayContainer-)


[getFirstOverlayParent()](#getFirstOverlayParent-)


[openOverlay(overlay, disableButtons)](#openOverlay-OverlayContainer-boolean-)


[getChildOverlay()](#getChildOverlay-)


[closeOverlay(overlay)](#closeOverlay-OverlayContainer-)


[setFocused(focused)](#setFocused-Element-)


[onClick(mouseX, mouseY, button)](#onClick-double-double-int-)


[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[close()](#close-)


[onClose()](#onClose-)


[renderBackground(drawContext)](#renderBackground-DrawContext-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .savedBtnStates


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[ClickableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ClickableWidget), [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html)>



#### .scroll


##### Type: [Scrollbar](1.9.2/xyz/wagyourtail/wagyourgui/elements/Scrollbar.html)



### Methods

#### .remove(btn)

| Parameter | Type | Description |
|---|---|---|
| btn | Element |  |

##### Returns: void



#### .openOverlay(overlay)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |

##### Returns: void



#### .getFirstOverlayParent()


##### Returns: [IOverlayParent](1.9.2/xyz/wagyourtail/wagyourgui/overlays/IOverlayParent.html)



#### .openOverlay(overlay, disableButtons)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |
| disableButtons | boolean |  |

##### Returns: void



#### .getChildOverlay()


##### Returns: [OverlayContainer](#)



#### .closeOverlay(overlay)

| Parameter | Type | Description |
|---|---|---|
| overlay | OverlayContainer |  |

##### Returns: void



#### .setFocused(focused)

| Parameter | Type | Description |
|---|---|---|
| focused | Element |  |

##### Returns: void



#### .onClick(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: void



#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean

true if should be handled by overlay



#### .close()


##### Returns: void



#### .onClose()


##### Returns: void



#### .renderBackground(drawContext)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




