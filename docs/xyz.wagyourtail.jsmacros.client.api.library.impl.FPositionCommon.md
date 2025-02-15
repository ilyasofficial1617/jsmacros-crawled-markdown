

xyz.wagyourtail.jsmacros.client.api.library.impl.FPositionCommon
----------------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.6.3

position helper classes

#### Methods

[createVec(x1, y1, z1, x2, y2, z2)](#createVec-double-double-double-double-double-double-)


[createLookingVector(entity)](#createLookingVector-EntityHelper-)


[createLookingVector(yaw, pitch)](#createLookingVector-double-double-)


[createVec(x1, y1, x2, y2)](#createVec-double-double-double-double-)


[createPos(x, y, z)](#createPos-double-double-double-)


[createPos(x, y)](#createPos-double-double-)


[createBlockPos(x, y, z)](#createBlockPos-int-int-int-)



### Methods

#### .createVec(x1, y1, z1, x2, y2, z2)

1.6.3

create a new vector object

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .createLookingVector(entity)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .createLookingVector(yaw, pitch)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| yaw | double |  |
| pitch | double |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .createVec(x1, y1, x2, y2)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| x2 | double |  |
| y2 | double |  |

##### Returns: [Vec2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec2D.html)



#### .createPos(x, y, z)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .createPos(x, y)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |

##### Returns: [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)



#### .createBlockPos(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the block |
| y | int | the y position of the block |
| z | int | the z position of the block |

##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

a [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html) for the given coordinates.




