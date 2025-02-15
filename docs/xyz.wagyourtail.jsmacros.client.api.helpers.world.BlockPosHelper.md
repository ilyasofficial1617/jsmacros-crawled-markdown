

xyz.wagyourtail.jsmacros.client.api.helpers.world.BlockPosHelper
----------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[BlockPos](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/BlockPos)>

1.2.6

### Constructors

#### new BlockPosHelper (b)

| Parameter | Type | Description |
|---|---|---|
| b | BlockPos |  |


#### new BlockPosHelper (x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |



#### Methods

[getX()](#getX-)


[getY()](#getY-)


[getZ()](#getZ-)


[up()](#up-)


[up(distance)](#up-int-)


[down()](#down-)


[down(distance)](#down-int-)


[north()](#north-)


[north(distance)](#north-int-)


[south()](#south-)


[south(distance)](#south-int-)


[east()](#east-)


[east(distance)](#east-int-)


[west()](#west-)


[west(distance)](#west-int-)


[offset(direction)](#offset-String-)


[offset(direction, distance)](#offset-String-int-)


[offset(x, y, z)](#offset-int-int-int-)


[toNetherCoords()](#toNetherCoords-)


[toOverworldCoords()](#toOverworldCoords-)


[distanceTo(entity)](#distanceTo-EntityHelper-)


[distanceTo(pos)](#distanceTo-BlockPosHelper-)


[distanceTo(pos)](#distanceTo-Pos3D-)


[distanceTo(x, y, z)](#distanceTo-double-double-double-)


[toPos3D()](#toPos3D-)


[equals(obj)](#equals-Object-)


[hashCode()](#hashCode-)


[toString()](#toString-)



### Methods

#### .getX()

1.2.6


##### Returns: int

the `x` value of the block.



#### .getY()

1.2.6


##### Returns: int

the `y` value of the block.



#### .getZ()

1.2.6


##### Returns: int

the `z` value of the block.



#### .up()

1.6.5


##### Returns: [BlockPosHelper](#)

the block above.



#### .up(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move up |

##### Returns: [BlockPosHelper](#)

the block n-th block above.



#### .down()

1.6.5


##### Returns: [BlockPosHelper](#)

the block below.



#### .down(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move down |

##### Returns: [BlockPosHelper](#)

the block n-th block below.



#### .north()

1.6.5


##### Returns: [BlockPosHelper](#)

the block to the north.



#### .north(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move north |

##### Returns: [BlockPosHelper](#)

the n-th block to the north.



#### .south()

1.6.5


##### Returns: [BlockPosHelper](#)

the block to the south.



#### .south(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move south |

##### Returns: [BlockPosHelper](#)

the n-th block to the south.



#### .east()

1.6.5


##### Returns: [BlockPosHelper](#)

the block to the east.



#### .east(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move east |

##### Returns: [BlockPosHelper](#)

the n-th block to the east.



#### .west()

1.6.5


##### Returns: [BlockPosHelper](#)

the block to the west.



#### .west(distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| distance | int | the distance to move west |

##### Returns: [BlockPosHelper](#)

the n-th block to the west.



#### .offset(direction)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| direction | String | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |

##### Returns: [BlockPosHelper](#)

the block offset by the given direction.



#### .offset(direction, distance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| direction | String | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |
| distance | int | the distance to move in the given direction |

##### Returns: [BlockPosHelper](#)

the n-th block offset by the given direction.



#### .offset(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x offset |
| y | int | the y offset |
| z | int | the y offset |

##### Returns: [BlockPosHelper](#)

the block offset by the given values.



#### .toNetherCoords()

1.8.4


##### Returns: [BlockPosHelper](#)

the block position converted to the respective nether coordinates.



#### .toOverworldCoords()

1.8.4


##### Returns: [BlockPosHelper](#)

the block position converted to the respective overworld coordinates.



#### .distanceTo(entity)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> | the entity to get the distance to |

##### Returns: double

the distance of this position to the given entity.



#### .distanceTo(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position to get the distance to |

##### Returns: double

the distance of this position to the given position.



#### .distanceTo(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position to get the distance to |

##### Returns: double

the distance of this position to the given position.



#### .distanceTo(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | double | the x coordinate to get the distance to |
| y | double | the y coordinate to get the distance to |
| z | double | the z coordinate to get the distance to |

##### Returns: double

the distance of this position to the given position.



#### .toPos3D()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html) representation of this position.



#### .equals(obj)

| Parameter | Type | Description |
|---|---|---|
| obj | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




