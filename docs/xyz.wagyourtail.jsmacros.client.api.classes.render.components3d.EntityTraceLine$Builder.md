

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.EntityTraceLine$Builder
---------------------------------------------------------------------------------------

Static
#### 

### Constructors

#### new EntityTraceLine$Builder (parent)

| Parameter | Type | Description |
|---|---|---|
| parent | Draw3D |  |



#### Fields

[screenPos](#screenPos)



#### Methods

[entity(entity)](#entity-EntityHelper-)


[getEntity()](#getEntity-)


[yOffset(yOffset)](#yOffset-double-)


[getYOffset()](#getYOffset-)


[color(color)](#color-int-)


[color(color, alpha)](#color-int-int-)


[color(r, g, b)](#color-int-int-int-)


[color(r, g, b, a)](#color-int-int-int-int-)


[getColor()](#getColor-)


[alpha(alpha)](#alpha-int-)


[getAlpha()](#getAlpha-)


[buildAndAdd(entity)](#buildAndAdd-EntityHelper-)


[buildAndAdd()](#buildAndAdd-)


[build(entity)](#build-EntityHelper-)


[build()](#build-)



### Fields

#### .screenPos


##### Type: [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)



### Methods

#### .entity(entity)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> | the target entity |

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .getEntity()

1.9.0


##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

the target entity



#### .yOffset(yOffset)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| yOffset | double | the offset of y-axis |

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .getYOffset()

1.9.0


##### Returns: double

the offset of y-axis



#### .color(color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .color(color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int | the color of the line |
| alpha | int | the alpha value of the line's color |

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .color(r, g, b)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .color(r, g, b, a)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| r | int | the red component of the color |
| g | int | the green component of the color |
| b | int | the blue component of the color |
| a | int | the alpha value of the color |

##### Returns: [EntityTraceLine$Builder](#)

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

##### Returns: [EntityTraceLine$Builder](#)

self for chaining



#### .getAlpha()

1.9.0


##### Returns: int

the alpha value of the line's color



#### .buildAndAdd(entity)

1.9.0

Creates the trace line for the given values and adds it to the draw3D

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> | the target entity |

##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)

the build line



#### .buildAndAdd()

1.9.0

Creates the trace line for the given values and adds it to the draw3D


##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)

the build line



#### .build(entity)

1.9.0

Builds the line from the given values

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> | the target entity |

##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)

the build line



#### .build()

1.9.0

Builds the line from the given values


##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)

the build line




