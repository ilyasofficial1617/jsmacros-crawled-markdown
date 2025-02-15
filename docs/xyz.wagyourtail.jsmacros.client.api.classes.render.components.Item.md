

xyz.wagyourtail.jsmacros.client.api.classes.render.components.Item
------------------------------------------------------------------

#### implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [Alignable](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Alignable.html)<[Item](#)>

1.0.5

### Constructors

#### new Item (x, y, zIndex, id, overlay, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| id | String |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | float |  |


#### new Item (x, y, zIndex, i, overlay, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| i | ItemStackHelper |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | float |  |


#### new Item (x, y, zIndex, itemStack, overlay, scale, rotation, ovText)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| zIndex | int |  |
| itemStack | ItemStackHelper |  |
| overlay | boolean |  |
| scale | double |  |
| rotation | float |  |
| ovText | String |  |



#### Fields

[parent](#parent)


[item](#item)


[ovText](#ovText)


[overlay](1.9.2/)


[scale](1.9.2/)


[rotation](1.9.2/)


[rotateCenter](1.9.2/)


[x](1.9.2/)


[y](1.9.2/)


[zIndex](1.9.2/)



#### Methods

[setItem(i)](#setItem-ItemStackHelper-)


[setItem(id, count)](#setItem-String-int-)


[getItem()](#getItem-)


[setX(x)](#setX-int-)


[getX()](#getX-)


[setY(y)](#setY-int-)


[getY()](#getY-)


[setPos(x, y)](#setPos-int-int-)


[setScale(scale)](#setScale-double-)


[getScale()](#getScale-)


[setRotation(rotation)](#setRotation-double-)


[getRotation()](#getRotation-)


[setRotateCenter(rotateCenter)](#setRotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[setOverlay(overlay)](#setOverlay-boolean-)


[shouldShowOverlay()](#shouldShowOverlay-)


[setOverlayText(ovText)](#setOverlayText-String-)


[getOverlayText()](#getOverlayText-)


[setZIndex(zIndex)](#setZIndex-int-)


[getZIndex()](#getZIndex-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[render3D(drawContext, mouseX, mouseY, delta)](#render3D-DrawContext-int-int-float-)


[render(drawContext, mouseX, mouseY, delta, is3dRender)](#render-DrawContext-int-int-float-boolean-)


[setParent(parent)](#setParent-IDraw2D-)


[getScaledWidth()](#getScaledWidth-)


[getParentWidth()](#getParentWidth-)


[getScaledHeight()](#getScaledHeight-)


[getParentHeight()](#getParentHeight-)


[getScaledLeft()](#getScaledLeft-)


[getScaledTop()](#getScaledTop-)


[moveTo(x, y)](#moveTo-int-int-)



### Fields

#### .parent


##### Type: [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)< ? >



#### .item


##### Type: [ItemStack](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/ItemStack)



#### .ovText


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .overlay


##### Type: boolean



#### .scale


##### Type: double



#### .rotation


##### Type: float



#### .rotateCenter


##### Type: boolean



#### .x


##### Type: int



#### .y


##### Type: int



#### .zIndex


##### Type: int



### Methods

#### .setItem(i)

1.0.5 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| i | ItemStackHelper |  |

##### Returns: [Item](#)



#### .setItem(id, count)

1.0.5 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| count | int |  |

##### Returns: [Item](#)



#### .getItem()

1.0.5 [citation needed]


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)



#### .setX(x)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the new x position of this element |

##### Returns: [Item](#)

self for chaining.



#### .getX()

1.8.4


##### Returns: int

the x position of this element.



#### .setY(y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| y | int | the new y position of this element |

##### Returns: [Item](#)

self for chaining.



#### .getY()

1.8.4


##### Returns: int

the y position of this element.



#### .setPos(x, y)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |

##### Returns: [Item](#)



#### .setScale(scale)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| scale | double |  |

##### Returns: [Item](#)



#### .getScale()

1.8.4


##### Returns: double

the scale of this item.



#### .setRotation(rotation)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| rotation | double |  |

##### Returns: [Item](#)



#### .getRotation()

1.8.4


##### Returns: float

the rotation of this item.



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether the item should be rotated around its center |

##### Returns: [Item](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this item should be rotated around its center, `false`
otherwise.



#### .setOverlay(overlay)

1.2.0

| Parameter | Type | Description |
|---|---|---|
| overlay | boolean |  |

##### Returns: [Item](#)



#### .shouldShowOverlay()

1.8.4


##### Returns: boolean

`true`, if the overlay, i.e. the durability bar, and the overlay text or
item count should be shown, `false` otherwise.



#### .setOverlayText(ovText)

1.2.0

| Parameter | Type | Description |
|---|---|---|
| ovText | String |  |

##### Returns: [Item](#)



#### .getOverlayText()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the overlay text of this item.



#### .setZIndex(zIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndex | int | the new z-index of this item |

##### Returns: [Item](#)

self for chaining.



#### .getZIndex()


##### Returns: int



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .render3D(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta, is3dRender)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |
| is3dRender | boolean |  |

##### Returns: void



#### .setParent(parent)

| Parameter | Type | Description |
|---|---|---|
| parent | IDraw2D<?> |  |

##### Returns: [Item](#)



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

##### Returns: [Item](#)




