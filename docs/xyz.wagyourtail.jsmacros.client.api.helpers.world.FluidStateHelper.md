

xyz.wagyourtail.jsmacros.client.api.helpers.world.FluidStateHelper
------------------------------------------------------------------

#### extends [StateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/StateHelper.html)<[FluidState](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/fluid/FluidState)>

1.8.4

### Constructors

#### new FluidStateHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | FluidState |  |



#### Methods

[getId()](#getId-)


[isStill()](#isStill-)


[isEmpty()](#isEmpty-)


[getHeight()](#getHeight-)


[getLevel()](#getLevel-)


[hasRandomTicks()](#hasRandomTicks-)


[getVelocity(pos)](#getVelocity-BlockPosHelper-)


[getBlockState()](#getBlockState-)


[getBlastResistance()](#getBlastResistance-)


[toString()](#toString-)



### Methods

#### .getId()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the fluid's id.



#### .isStill()

1.8.4


##### Returns: boolean

`true` if this fluid is still, `false` otherwise.



#### .isEmpty()

1.8.4


##### Returns: boolean

`true` if this fluid is empty (the default fluid state for non fluid blocks),
`false` otherwise.



#### .getHeight()

1.8.4


##### Returns: float

the height of this state.



#### .getLevel()

1.8.4


##### Returns: int

the level of this state.



#### .hasRandomTicks()

1.8.4


##### Returns: boolean

`true` if the fluid has some random tick logic (only used by lava to do the
fire spread), `false` otherwise.



#### .getVelocity(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position in the world |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the velocity that will be applied to entities at the given position.



#### .getBlockState()

1.8.4


##### Returns: [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html)

the block state of this fluid.



#### .getBlastResistance()

1.8.4


##### Returns: float

the blast resistance of this fluid.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




