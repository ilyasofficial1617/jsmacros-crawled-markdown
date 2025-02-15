

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.TraceLine$Builder
---------------------------------------------------------------------------------

Static
#### 

### Constructors

#### new TraceLine$Builder (parent)

| Parameter | Type | Description |
|---|---|---|
| parent | Draw3D |  |



#### Fields

[screenPos](#screenPos)



#### Methods

[pos(pos)](#pos-Pos3D-)


[pos(pos)](#pos-BlockPosHelper-)


[pos(x, y, z)](#pos-int-int-int-)


[getPos()](#getPos-)


[color(color)](#color-int-)


[color(color, alpha)](#color-int-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[buildAndAdd()](#buildAndAdd-)


[build()](#build-)



### Fields

#### .screenPos


##### Type: [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)



### Methods

#### .pos(pos)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position of the target |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .pos(pos)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the position of the target |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .pos(x, y, z)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the target |
| y | int | the y coordinate of the target |
| z | int | the z coordinate of the target |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .getPos()

1.9.0


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the position of the target



#### .color(color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .color(color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |
| alpha | int | the alpha value of the line's color |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .color(r, g, b)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .color(r, g, b, a)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha value of the color |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .getColor()

1.9.0


##### Returns: int

the color of the line



#### .alpha(alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value for the line's color |

##### Returns: [TraceLine$Builder](#)

self for chaining



#### .getAlpha()

1.9.0


##### Returns: int

the alpha value of the line's color



#### .buildAndAdd()

1.9.0

Creates the trace line for the given values and adds it to the draw3D


##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)

the build line



#### .build()

1.9.0

Builds the line from the given values


##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)

the build line




