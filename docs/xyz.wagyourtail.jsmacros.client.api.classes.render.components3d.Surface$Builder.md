

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Surface$Builder
-------------------------------------------------------------------------------

Static
#### 

1.8.4

### Constructors

#### new Surface$Builder (parent)

| Parameter | Type | Description |
|---|---|---|
| parent | Draw3D |  |



#### Methods

[pos(pos)](#pos-Pos3D-)


[pos(pos)](#pos-BlockPosHelper-)


[pos(x, y, z)](#pos-double-double-double-)


[getPos()](#getPos-)


[bindToEntity(boundEntity)](#bindToEntity-EntityHelper-)


[getBoundEntity()](#getBoundEntity-)


[boundOffset(entityOffset)](#boundOffset-Pos3D-)


[boundOffset(x, y, z)](#boundOffset-double-double-double-)


[getBoundOffset()](#getBoundOffset-)


[xRotation(xRot)](#xRotation-double-)


[getXRotation()](#getXRotation-)


[yRotation(yRot)](#yRotation-double-)


[getYRotation()](#getYRotation-)


[zRotation(zRot)](#zRotation-double-)


[getZRotation()](#getZRotation-)


[rotation(xRot, yRot, zRot)](#rotation-double-double-double-)


[rotateCenter(rotateCenter)](#rotateCenter-boolean-)


[isRotatingCenter()](#isRotatingCenter-)


[rotateToPlayer(rotateToPlayer)](#rotateToPlayer-boolean-)


[doesRotateToPlayer()](#doesRotateToPlayer-)


[width(width)](#width-double-)


[getWidth()](#getWidth-)


[height(height)](#height-double-)


[getHeight()](#getHeight-)


[size(width, height)](#size-double-double-)


[minSubdivisions(minSubdivisions)](#minSubdivisions-int-)


[getMinSubdivisions()](#getMinSubdivisions-)


[renderBack(renderBack)](#renderBack-boolean-)


[shouldRenderBack()](#shouldRenderBack-)


[cull(cull)](#cull-boolean-)


[isCulled()](#isCulled-)


[zIndex(zIndexScale)](#zIndex-double-)


[getZIndexScale()](#getZIndexScale-)


[buildAndAdd()](#buildAndAdd-)


[build()](#build-)



### Methods

#### .pos(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .pos(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .pos(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x position of the surface |
| y | double | the y position of the surface |
| z | double | the z position of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getPos()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the position of the surface.



#### .bindToEntity(boundEntity)

1.8.4

The surface will move with the entity at the offset location.

| Parameter | Type | Description |
|---|---|---|
| boundEntity | EntityHelper<?> | the entity to bind the surface to |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getBoundEntity()

1.8.4


##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

the entity the surface is bound to, or `null` if it is not bound to an
entity.



#### .boundOffset(entityOffset)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| entityOffset | Pos3D | the offset from the entity's position to render the surface at |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .boundOffset(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x offset from the entity's position to render the surface at |
| y | double | the y offset from the entity's position to render the surface at |
| z | double | the z offset from the entity's position to render the surface at |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getBoundOffset()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the offset from the entity's position to render the surface at.



#### .xRotation(xRot)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| xRot | double | the x rotation of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getXRotation()

1.8.4


##### Returns: double

the x rotation of the surface.



#### .yRotation(yRot)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| yRot | double | the y rotation of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getYRotation()

1.8.4


##### Returns: double

the y rotation of the surface.



#### .zRotation(zRot)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zRot | double | the z rotation of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getZRotation()

1.8.4


##### Returns: double

the z rotation of the surface.



#### .rotation(xRot, yRot, zRot)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| xRot | double | the x rotation of the surface |
| yRot | double | the y rotation of the surface |
| zRot | double | the z rotation of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .rotateCenter(rotateCenter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateCenter | boolean | whether to rotate around the center of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .isRotatingCenter()

1.8.4


##### Returns: boolean

`true` if this surface should be rotated around its center,
`false` otherwise.



#### .rotateToPlayer(rotateToPlayer)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| rotateToPlayer | boolean | whether to rotate the surface to face the player or not |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .doesRotateToPlayer()

1.8.4


##### Returns: boolean

`true` if the surface should be rotated to face the player,
`false` otherwise.



#### .width(width)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | double | the width of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getWidth()

1.8.4


##### Returns: double

the width of the surface.



#### .height(height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| height | double | the height of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getHeight()

1.8.4


##### Returns: double

the height of the surface.



#### .size(width, height)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | double | the width of the surface |
| height | double | the height of the surface |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .minSubdivisions(minSubdivisions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| minSubdivisions | int | the minimum number of subdivisions |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getMinSubdivisions()

1.8.4


##### Returns: int

the minimum number of subdivisions.



#### .renderBack(renderBack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| renderBack | boolean | whether the back of the surface should be rendered or not |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .shouldRenderBack()

1.8.4


##### Returns: boolean

`true` if the back of the surface should be rendered, `false`
otherwise.



#### .cull(cull)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| cull | boolean | whether to enable culling or not |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .isCulled()

1.8.4


##### Returns: boolean

`true` if culling is enabled for this box, `false` otherwise.



#### .zIndex(zIndexScale)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| zIndexScale | double | the scale of the z-index |

##### Returns: [Surface$Builder](#)

self for chaining.



#### .getZIndexScale()

1.8.4


##### Returns: double

the scale of the z-index.



#### .buildAndAdd()

1.8.4

Creates the surface for the given values and adds it to the draw3D.


##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)

the build surface.



#### .build()

Builds the surface from the given values.


##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)

the build surface.




