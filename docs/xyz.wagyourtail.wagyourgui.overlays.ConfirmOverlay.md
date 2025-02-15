

xyz.wagyourtail.wagyourgui.overlays.ConfirmOverlay
--------------------------------------------------

#### extends [OverlayContainer](1.9.2/xyz/wagyourtail/wagyourgui/overlays/OverlayContainer.html)

### Constructors

#### new ConfirmOverlay (x, y, width, height, textRenderer, message, parent, accept)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| message | Text |  |
| parent | IOverlayParent |  |
| accept | Consumer<ConfirmOverlay> |  |


#### new ConfirmOverlay (x, y, width, height, hcenter, textRenderer, message, parent, accept)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| hcenter | boolean |  |
| textRenderer | TextRenderer |  |
| message | Text |  |
| parent | IOverlayParent |  |
| accept | Consumer<ConfirmOverlay> |  |



#### Fields

[hcenter](1.9.2/)



#### Methods

[setMessage(message)](#setMessage-Text-)


[init()](#init-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .hcenter


##### Type: boolean



### Methods

#### .setMessage(message)

| Parameter | Type | Description |
|---|---|---|
| message | Text |  |

##### Returns: void



#### .init()


##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




