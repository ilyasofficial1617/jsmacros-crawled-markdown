

xyz.wagyourtail.jsmacros.client.api.classes.math.Pos3D
------------------------------------------------------

#### extends [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)

1.2.6 [citation needed]

### Constructors

#### new Pos3D (vec)

| Parameter | Type | Description |
|---|---|---|
| vec | Vec3d |  |


#### new Pos3D (x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |



#### Fields

[ZERO](#ZERO)
S
F


[z](1.9.2/)



#### Methods

[getZ()](#getZ-)


[add(pos)](#add-Pos3D-)


[add(x, y, z)](#add-double-double-double-)


[sub(pos)](#sub-Pos3D-)


[sub(x, y, z)](#sub-double-double-double-)


[multiply(pos)](#multiply-Pos3D-)


[multiply(x, y, z)](#multiply-double-double-double-)


[divide(pos)](#divide-Pos3D-)


[divide(x, y, z)](#divide-double-double-double-)


[scale(scale)](#scale-double-)


[toString()](#toString-)


[toVector()](#toVector-)


[toVector(start\_pos)](#toVector-Pos2D-)


[toVector(start\_pos)](#toVector-Pos3D-)


[toVector(start\_x, start\_y, start\_z)](#toVector-double-double-double-)


[toReverseVector()](#toReverseVector-)


[toReverseVector(end\_pos)](#toReverseVector-Pos2D-)


[toReverseVector(end\_pos)](#toReverseVector-Pos3D-)


[toReverseVector(end\_x, end\_y, end\_z)](#toReverseVector-double-double-double-)


[toBlockPos()](#toBlockPos-)


[toRawBlockPos()](#toRawBlockPos-)


[toMojangDoubleVector()](#toMojangDoubleVector-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)


[compareTo(o)](#compareTo-Pos3D-)



### Fields

#### .ZERO

Static
Final

##### Type: [Pos3D](#)



#### .z


##### Type: double



### Methods

#### .getZ()


##### Returns: double



#### .add(pos)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |

##### Returns: [Pos3D](#)



#### .add(x, y, z)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: [Pos3D](#)



#### .sub(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position to subtract |

##### Returns: [Pos3D](#)

the new position.



#### .sub(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x coordinate to subtract |
| y | double | the y coordinate to subtract |
| z | double | the z coordinate to subtract |

##### Returns: [Pos3D](#)

the new position.



#### .multiply(pos)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |

##### Returns: [Pos3D](#)



#### .multiply(x, y, z)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: [Pos3D](#)



#### .divide(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position to divide by |

##### Returns: [Pos3D](#)

the new position.



#### .divide(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x coordinate to divide by |
| y | double | the y coordinate to divide by |
| z | double | the z coordinate to divide by |

##### Returns: [Pos3D](#)

the new position.



#### .scale(scale)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| scale | double |  |

##### Returns: [Pos3D](#)



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .toVector()


##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toVector(start\_pos)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| start_pos | Pos2D |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toVector(start\_pos)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| start_pos | Pos3D |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toVector(start\_x, start\_y, start\_z)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| start_x | double |  |
| start_y | double |  |
| start_z | double |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toReverseVector()

1.6.4


##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toReverseVector(end\_pos)

| Parameter | Type | Description |
|---|---|---|
| end_pos | Pos2D |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toReverseVector(end\_pos)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| end_pos | Pos3D |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toReverseVector(end\_x, end\_y, end\_z)

1.6.4

| Parameter | Type | Description |
|---|---|---|
| end_x | double |  |
| end_y | double |  |
| end_z | double |  |

##### Returns: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .toBlockPos()

1.8.0


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)



#### .toRawBlockPos()

1.8.0


##### Returns: [BlockPos](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/BlockPos)



#### .toMojangDoubleVector()

1.8.4


##### Returns: [Vec3d](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/Vec3d)

the raw minecraft double vector with the same coordinates as this position.



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int



#### .compareTo(o)

| Parameter | Type | Description |
|---|---|---|
| o | Pos3D |  |

##### Returns: int




