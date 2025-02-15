

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Item$Builder
--------------------------------------------------------------------------

Static
Final
#### extends [RenderElementBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElementBuilder.html)<[Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html)> implements [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Item$Builder](#)>

1.8.4

### Constructors

#### new Item$Builder (draw2D)

| Parameter | Type | Description |
|---|---|---|
| draw2D | IDraw2D<?> |  |



#### Methods

[x(x)](#x-int-)


[getX()](#getX-)


[y(y)](#y-int-)


[getY()](#getY-)


[pos(x, y)](#pos-int-int-)


[item(item)](#item-ItemStackHelper-)


[item(id)](#item-String-)


[item(id, count)](#item-String-int-)


[getItem()](#getItem-)


[overlayText(overlayText)](#overlayText-String-)


[getOverlayText()](#getOverlayText-)


[overlayVisible(visible)](#overlayVisible-boolean-)


[isOverlayVisible()](#isOverlayVisible-)


[scale(scale)](#scale-double-)


[getScale()](#getScale-)


[rotation(rotation)](#rotation-double-)


[getRotation()](#getRotation-)


[rotateCenter(rotateCenter)](#rotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[zIndex(zIndex)](#zIndex-int-)


[getZIndex()](#getZIndex-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)


[moveTo(x, y)](#moveTo-int-int-)



### Methods

#### .x(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the item |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of the item.



#### .y(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the y position of the item |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of the item.



#### .pos(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the item |
| y | int | the y position of the item |

##### Returns: [Item$Builder](#)

self for chaining.



#### .item(item)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| item | ItemStackHelper | the item to draw |

##### Returns: [Item$Builder](#)

self for chaining.



#### .item(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the item to draw |

##### Returns: [Item$Builder](#)

self for chaining.



#### .item(id, count)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the item to draw |
| count | int | the stack size |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getItem()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the item to be drawn.



#### .overlayText(overlayText)

1.8.4

This also sets the overlay to be shown.

| Parameter | Type | Description |
|---|---|---|
| overlayText | String | the overlay text |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getOverlayText()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the overlay text.



#### .overlayVisible(visible)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| visible | boolean | whether the overlay should be visible or not |

##### Returns: [Item$Builder](#)

self for chaining.



#### .isOverlayVisible()

1.8.4


##### Returns: boolean

`true` if the overlay should be visible, `false` otherwise.



#### .scale(scale)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| scale | double | the scale of the item |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getScale()

1.8.4


##### Returns: double

the scale of the item.



#### .rotation(rotation)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotation | double | the rotation (clockwise) of the item in degrees |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getRotation()

1.8.4


##### Returns: float

the rotation (clockwise) of the item in degrees.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether the item should be rotated around its center |

##### Returns: [Item$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this item should be rotated around its center, `false`
otherwise.



#### .zIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the z-index of the item |

##### Returns: [Item$Builder](#)

self for chaining.



#### .getZIndex()

1.8.4


##### Returns: int

the z-index of the item.



#### .getScaledWidth()


##### Returns: int



#### .getParentWidth()


##### Returns: int



#### .getScaledHeight()


##### Returns: int



#### .getParentHeight()


##### Returns: int



#### .getScaledLeft()


##### Returns: int



#### .getScaledTop()


##### Returns: int



#### .moveTo(x, y)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Item$Builder](#)




