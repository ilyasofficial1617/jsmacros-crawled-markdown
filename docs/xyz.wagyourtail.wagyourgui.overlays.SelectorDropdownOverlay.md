

xyz.wagyourtail.wagyourgui.overlays.SelectorDropdownOverlay
-----------------------------------------------------------

#### extends [OverlayContainer](1.9.2/xyz/wagyourtail/wagyourgui/overlays/OverlayContainer.html)

### Constructors

#### new SelectorDropdownOverlay (x, y, width, height, choices, textRenderer, parent, onChoice)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| choices | Collection<Text> |  |
| textRenderer | TextRenderer |  |
| parent | IOverlayParent |  |
| onChoice | Consumer<Integer> |  |



#### Methods

[init()](#init-)


[onScroll(page)](#onScroll-double-)


[onClick(mouseX, mouseY, button)](#onClick-double-double-int-)


[setSelected(sel)](#setSelected-int-)


[keyPressed(keyCode, scanCode, modifiers)](#keyPressed-int-int-int-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Methods

#### .init()


##### Returns: void



#### .onScroll(page)

| Parameter | Type | Description |
|---|---|---|
| page | double |  |

##### Returns: void



#### .onClick(mouseX, mouseY, button)

| Parameter | Type | Description |
|---|---|---|
| mouseX | double |  |
| mouseY | double |  |
| button | int |  |

##### Returns: void



#### .setSelected(sel)

| Parameter | Type | Description |
|---|---|---|
| sel | int |  |

##### Returns: void



#### .keyPressed(keyCode, scanCode, modifiers)

| Parameter | Type | Description |
|---|---|---|
| keyCode | int |  |
| scanCode | int |  |
| modifiers | int |  |

##### Returns: boolean



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




