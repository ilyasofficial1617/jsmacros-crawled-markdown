
[EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.TraceLine
-------------------------------------------------------------------------

#### implements [RenderElement3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/RenderElement3D.html)<[TraceLine](#)>

1.9.0

### Constructors

#### new TraceLine (x, y, z, color)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| color | int |  |


#### new TraceLine (x, y, z, color, alpha)

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| color | int |  |
| alpha | int |  |


#### new TraceLine (pos, color)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| color | int |  |


#### new TraceLine (pos, color, alpha)

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| color | int |  |
| alpha | int |  |



#### Fields

[screenPos](#screenPos)


[pos](#pos)


[color](1.9.2/)



#### Methods

[setPos(x, y, z)](#setPos-double-double-double-)


[setPos(pos)](#setPos-Pos3D-)


[setColor(color)](#setColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


[setAlpha(alpha)](#setAlpha-int-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)


[compareToSame(other)](#compareToSame-TraceLine-)


[render(drawContext, builder, tickDelta)](#render-DrawContext-BufferBuilder-float-)



### Fields

#### .screenPos

this is not meant to be exposed because it works in a poor way  

it needs fov and aspect ratio info to render normally when not on center  

but for customize availability I just put it here as a field


##### Type: [Pos2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos2D.html)



#### .pos


##### Type: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)



#### .color


##### Type: int



### Methods

#### .setPos(x, y, z)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |

##### Returns: [TraceLine](#)

self for chaining



#### .setPos(pos)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |

##### Returns: [TraceLine](#)

self for chaining



#### .setColor(color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [TraceLine](#)

self for chaining



#### .setColor(color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| color | int |  |
| alpha | int |  |

##### Returns: [TraceLine](#)

self for chaining



#### .setAlpha(alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| alpha | int |  |

##### Returns: [TraceLine](#)

self for chaining



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int



#### .compareToSame(other)

| Parameter | Type | Description |
|---|---|---|
| other | TraceLine |  |

##### Returns: int



#### .render(drawContext, builder, tickDelta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| builder | BufferBuilder |  |
| tickDelta | float |  |

##### Returns: void




