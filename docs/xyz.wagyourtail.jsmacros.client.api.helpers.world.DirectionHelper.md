

xyz.wagyourtail.jsmacros.client.api.helpers.world.DirectionHelper
-----------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Direction](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/Direction)>

1.8.4

### Constructors

#### new DirectionHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | Direction |  |



#### Methods

[getName()](#getName-)


[getAxis()](#getAxis-)


[isVertical()](#isVertical-)


[isHorizontal()](#isHorizontal-)


[isTowardsPositive()](#isTowardsPositive-)


[getYaw()](#getYaw-)


[getPitch()](#getPitch-)


[getOpposite()](#getOpposite-)


[getLeft()](#getLeft-)


[getRight()](#getRight-)


[getVector()](#getVector-)


[pointsTo(yaw)](#pointsTo-double-)


[toString()](#toString-)



### Methods

#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of this direction.



#### .getAxis()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the axis this direction is aligned to.



#### .isVertical()

1.8.4


##### Returns: boolean

`true` if this direction is vertical, `false` otherwise.



#### .isHorizontal()

1.8.4


##### Returns: boolean

`true` if this direction is horizontal, `false` otherwise.



#### .isTowardsPositive()

1.8.4


##### Returns: boolean

`true` if this direction is pointing in a positive direction, `false`
otherwise.



#### .getYaw()

1.8.4


##### Returns: float

the yaw of this direction.



#### .getPitch()

1.8.4


##### Returns: float

the pitch of this direction.



#### .getOpposite()

1.8.4


##### Returns: [DirectionHelper](#)

the opposite direction.



#### .getLeft()

1.8.4


##### Returns: [DirectionHelper](#)

the direction to the left.



#### .getRight()

1.8.4


##### Returns: [DirectionHelper](#)

the direction to the right.



#### .getVector()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the direction as a directional vector.



#### .pointsTo(yaw)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| yaw | double | the yaw to check |

##### Returns: boolean

`true` if the yaw is facing this direction more than any other one,
`false` otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




