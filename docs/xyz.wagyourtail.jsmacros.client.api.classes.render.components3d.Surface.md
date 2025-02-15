

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Surface
-----------------------------------------------------------------------

#### extends [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html) implements [RenderElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/RenderElement.html) [RenderElement3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/RenderElement3D.html)<[Surface](#)>

1.6.5

### Constructors

#### new Surface (pos, rotations, sizes, minSubdivisions, renderBack, cull)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| rotations | Pos3D |  |
| sizes | Pos2D |  |
| minSubdivisions | int |  |
| renderBack | boolean |  |
| cull | boolean |  |



#### Fields

[rotateToPlayer](1.9.2/)


[rotateCenter](1.9.2/)


[boundEntity](#boundEntity)


[boundOffset](#boundOffset)


[pos](#pos)
F


[rotations](#rotations)
F


[zIndexScale](1.9.2/)


[renderBack](1.9.2/)


[cull](1.9.2/)



#### Methods

[setPos(pos)](#setPos-Pos3D-)


[setPos(pos)](#setPos-BlockPosHelper-)


[setPos(x, y, z)](#setPos-double-double-double-)


[bindToEntity(boundEntity)](#bindToEntity-EntityHelper-)


[getBoundEntity()](#getBoundEntity-)


[setBoundOffset(boundOffset)](#setBoundOffset-Pos3D-)


[setBoundOffset(x, y, z)](#setBoundOffset-double-double-double-)


[getBoundOffset()](#getBoundOffset-)


[setRotateToPlayer(rotateToPlayer)](#setRotateToPlayer-boolean-)


[doesRotateToPlayer()](#doesRotateToPlayer-)


[setRotations(x, y, z)](#setRotations-double-double-double-)


[setSizes(x, y)](#setSizes-double-double-)


[getSizes()](#getSizes-)


[setMinSubdivisions(minSubdivisions)](#setMinSubdivisions-int-)


[getMinSubdivisions()](#getMinSubdivisions-)


[getHeight()](#getHeight-)


[getWidth()](#getWidth-)


[setRotateCenter(rotateCenter)](#setRotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[init()](#init-)


[getZIndex()](#getZIndex-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)


[compareToSame(other)](#compareToSame-Surface-)


[render(drawContext, builder, delta)](#render-DrawContext-BufferBuilder-float-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .rotateToPlayer


##### Type: boolean



#### .rotateCenter


##### Type: boolean



#### .boundEntity


##### Type: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >



#### .boundOffset


##### Type: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .pos

Final

##### Type: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .rotations

Final

##### Type: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .zIndexScale

1.6.5

scale that zIndex is multiplied by to get the actual offset (in blocks) for rendering
default: `1/1000` if there is still z-fighting, increase this value


##### Type: double



#### .renderBack


##### Type: boolean



#### .cull


##### Type: boolean



### Methods

#### .setPos(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position of the surface |

##### Returns: [Surface](#)

self for chaining.



#### .setPos(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position of the surface |

##### Returns: [Surface](#)

self for chaining.



#### .setPos(x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: [Surface](#)



#### .bindToEntity(boundEntity)

1.8.4

The surface will move with the entity at the offset location.

| Parameter | Type | Description |
|---|---|---|
| boundEntity | EntityHelper<?> | the entity to bind the surface to |

##### Returns: [Surface](#)

self for chaining.



#### .getBoundEntity()

1.8.4


##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

the entity the surface is bound to, or `null` if it is not bound to an
entity.



#### .setBoundOffset(boundOffset)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| boundOffset | Pos3D | the offset from the entity's position to render the surface at |

##### Returns: [Surface](#)

self for chaining.



#### .setBoundOffset(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x offset from the entity's position to render the surface at |
| y | double | the y offset from the entity's position to render the surface at |
| z | double | the z offset from the entity's position to render the surface at |

##### Returns: [Surface](#)

self for chaining.



#### .getBoundOffset()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the offset from the entity's position to render the surface at.



#### .setRotateToPlayer(rotateToPlayer)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateToPlayer | boolean | whether to rotate the surface to face the player or not |

##### Returns: [Surface](#)

self for chaining.



#### .doesRotateToPlayer()

1.8.4


##### Returns: boolean

`true` if the surface should be rotated to face the player, `false`
otherwise.



#### .setRotations(x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: void



#### .setSizes(x, y)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |

##### Returns: void



#### .getSizes()


##### Returns: [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)



#### .setMinSubdivisions(minSubdivisions)

| Parameter | Type | Description |
|---|---|---|
| minSubdivisions | int |  |

##### Returns: void



#### .getMinSubdivisions()


##### Returns: int



#### .getHeight()


##### Returns: int



#### .getWidth()


##### Returns: int



#### .setRotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether to rotate the surface around its center or not |

##### Returns: [Surface](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this surface is rotated around it's center, `false`
otherwise.



#### .init()


##### Returns: void



#### .getZIndex()


##### Returns: int



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int



#### .compareToSame(other)

| Parameter | Type | Description |
|---|---|---|
| other | Surface |  |

##### Returns: int



#### .render(drawContext, builder, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| builder | BufferBuilder |  |
| delta | float |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




