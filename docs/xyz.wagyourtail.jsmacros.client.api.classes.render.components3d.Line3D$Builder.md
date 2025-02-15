

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Line3D$Builder
------------------------------------------------------------------------------

Static
#### 

1.8.4

### Constructors

#### new Line3D$Builder (parent)

| Parameter | Type | Description |
|---|---|---|
| parent | Draw3D |  |



#### Methods

[pos1(pos1)](#pos1-Pos3D-)


[pos1(pos1)](#pos1-BlockPosHelper-)


[pos1(x1, y1, z1)](#pos1-double-double-double-)


[getPos1()](#getPos1-)


[pos2(pos2)](#pos2-Pos3D-)


[pos2(pos2)](#pos2-BlockPosHelper-)


[pos2(x2, y2, z2)](#pos2-int-int-int-)


[getPos2()](#getPos2-)


[pos(x1, y1, z1, x2, y2, z2)](#pos-int-int-int-int-int-int-)


[pos(pos1, pos2)](#pos-BlockPosHelper-BlockPosHelper-)


[pos(pos1, pos2)](#pos-Pos3D-Pos3D-)


[color(color)](#color-int-)


[color(color, alpha)](#color-int-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[cull(cull)](#cull-boolean-)


[isCulled()](#isCulled-)


[buildAndAdd()](#buildAndAdd-)


[build()](#build-)



### Methods

#### .pos1(pos1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | Pos3D | the first position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos1(pos1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos1(x1, y1, z1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | double | the x coordinate of the first position of the line |
| y1 | double | the y coordinate of the first position of the line |
| z1 | double | the z coordinate of the first position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .getPos1()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the first position of the line.



#### .pos2(pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos2 | Pos3D | the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos2(pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos2 | BlockPosHelper | the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos2(x2, y2, z2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | int | the x coordinate of the second position of the line |
| y2 | int | the y coordinate of the second position of the line |
| z2 | int | the z coordinate of the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .getPos2()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the second position of the line.



#### .pos(x1, y1, z1, x2, y2, z2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | int | the x coordinate of the first position of the line |
| y1 | int | the y coordinate of the first position of the line |
| z1 | int | the z coordinate of the first position of the line |
| x2 | int | the x coordinate of the second position of the line |
| y2 | int | the x coordinate of the second position of the line |
| z2 | int | the z coordinate of the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos(pos1, pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position of the line |
| pos2 | BlockPosHelper | the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .pos(pos1, pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | Pos3D | the first position of the line |
| pos2 | Pos3D | the second position of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .color(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |
| alpha | int | the alpha value of the line's color |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha value of the color |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the line.



#### .alpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value for the line's color |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the line's color.



#### .cull(cull)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| cull | boolean | whether to cull the line or not |

##### Returns: [Line3D$Builder](#)

self for chaining.



#### .isCulled()

1.8.4


##### Returns: boolean

`true` if the line should be culled, `false` otherwise.



#### .buildAndAdd()

1.8.4

Creates the line for the given values and adds it to the draw3D.


##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)

the build line.



#### .build()

Builds the line from the given values.


##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)

the build line.




