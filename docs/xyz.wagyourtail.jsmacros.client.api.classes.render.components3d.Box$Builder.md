

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Box$Builder
---------------------------------------------------------------------------

Static
#### 

1.8.4

### Constructors

#### new Box$Builder (parent)

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


[pos2(x2, y2, z2)](#pos2-double-double-double-)


[getPos2()](#getPos2-)


[pos(x1, y1, z1, x2, y2, z2)](#pos-double-double-double-double-double-double-)


[pos(pos1, pos2)](#pos-BlockPosHelper-BlockPosHelper-)


[pos(pos1, pos2)](#pos-Pos3D-Pos3D-)


[forBlock(x, y, z)](#forBlock-int-int-int-)


[forBlock(pos)](#forBlock-BlockPosHelper-)


[color(color)](#color-int-)


[color(color, alpha)](#color-int-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[fillColor(fillColor)](#fillColor-int-)


[fillColor(fillColor, alpha)](#fillColor-int-int-)


[fillColor(r, g, b)](#fillColor-int-int-int-)


[fillColor(r, g, b, a)](#fillColor-int-int-int-int-)


[getFillColor()](#getFillColor-)


[fillAlpha(fillAlpha)](#fillAlpha-int-)


[getFillAlpha()](#getFillAlpha-)


[fill(fill)](#fill-boolean-)


[isFilled()](#isFilled-)


[cull(cull)](#cull-boolean-)


[isCulled()](#isCulled-)


[buildAndAdd()](#buildAndAdd-)


[build()](#build-)



### Methods

#### .pos1(pos1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | Pos3D | the first position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos1(pos1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos1(x1, y1, z1)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | double | the x coordinate of the first position of the box |
| y1 | double | the y coordinate of the first position of the box |
| z1 | double | the z coordinate of the first position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getPos1()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the first position of the box.



#### .pos2(pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos2 | Pos3D | the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos2(pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos2 | BlockPosHelper | the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos2(x2, y2, z2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x2 | double | the x coordinate of the second position of the box |
| y2 | double | the y coordinate of the second position of the box |
| z2 | double | the z coordinate of the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getPos2()

1.8.4


##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the second position of the box.



#### .pos(x1, y1, z1, x2, y2, z2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x1 | double | the x coordinate of the first position of the box |
| y1 | double | the y coordinate of the first position of the box |
| z1 | double | the z coordinate of the first position of the box |
| x2 | double | the x coordinate of the second position of the box |
| y2 | double | the y coordinate of the second position of the box |
| z2 | double | the z coordinate of the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos(pos1, pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper | the first position of the box |
| pos2 | BlockPosHelper | the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .pos(pos1, pos2)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos1 | Pos3D | the first position of the box |
| pos2 | Pos3D | the second position of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .forBlock(x, y, z)

1.8.4

Highlights the given block position.

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the block |
| y | int | the y coordinate of the block |
| z | int | the z coordinate of the block |

##### Returns: [Box$Builder](#)

self for chaining.



#### .forBlock(pos)

1.8.4

Highlights the given block position.

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the block position |

##### Returns: [Box$Builder](#)

self for chaining.



#### .color(color)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .color(color, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| color | int | the fill color of the box |
| alpha | int | the alpha value for the box's fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .color(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the fill color |
| g | int | the green component of the fill color |
| b | int | the blue component of the fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .color(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the fill color |
| g | int | the green component of the fill color |
| b | int | the blue component of the fill color |
| a | int | the alpha component of the fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getColor()

1.8.4


##### Returns: int

the color of the box.



#### .alpha(alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| alpha | int | the alpha value for the box's color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getAlpha()

1.8.4


##### Returns: int

the alpha value of the box's color.



#### .fillColor(fillColor)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| fillColor | int | the fill color of the box |

##### Returns: [Box$Builder](#)

self for chaining.



#### .fillColor(fillColor, alpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| fillColor | int | the fill color of the box |
| alpha | int | the alpha value for the box's fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .fillColor(r, g, b)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the fill color |
| g | int | the green component of the fill color |
| b | int | the blue component of the fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .fillColor(r, g, b, a)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the fill color |
| g | int | the green component of the fill color |
| b | int | the blue component of the fill color |
| a | int | the alpha component of the fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getFillColor()

1.8.4


##### Returns: int

the fill color of the box.



#### .fillAlpha(fillAlpha)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| fillAlpha | int | the alpha value for the box's fill color |

##### Returns: [Box$Builder](#)

self for chaining.



#### .getFillAlpha()

1.8.4


##### Returns: int

the alpha value of the box's fill color.



#### .fill(fill)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| fill | boolean | true if the box should be filled, false otherwise |

##### Returns: [Box$Builder](#)

self for chaining.



#### .isFilled()

1.8.4


##### Returns: boolean

`true` if the box should be filled, `false` otherwise.



#### .cull(cull)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| cull | boolean | whether to enable culling or not |

##### Returns: [Box$Builder](#)

self for chaining.



#### .isCulled()

1.8.4


##### Returns: boolean

`true` if culling is enabled for this box, `false` otherwise.



#### .buildAndAdd()

1.8.4

Creates the box for the given values and adds it to the draw3D.


##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the build box.



#### .build()

Builds the box from the given values.


##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the build box.




