

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Box
-------------------------------------------------------------------

#### implements [RenderElement3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/RenderElement3D.html)<[Box](#)>

### Constructors

#### new Box (x1, y1, z1, x2, y2, z2, color, fillColor, fill, cull)

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |
| color | int |  |
| fillColor | int |  |
| fill | boolean |  |
| cull | boolean |  |


#### new Box (x1, y1, z1, x2, y2, z2, color, alpha, fillColor, fillAlpha, fill, cull)

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |
| color | int |  |
| alpha | int |  |
| fillColor | int |  |
| fillAlpha | int |  |
| fill | boolean |  |
| cull | boolean |  |



#### Fields

[pos](#pos)


[color](1.9.2/)


[fillColor](1.9.2/)


[fill](1.9.2/)


[cull](1.9.2/)



#### Methods

[setPos(x1, y1, z1, x2, y2, z2)](#setPos-double-double-double-double-double-double-)


[setPosToBlock(pos)](#setPosToBlock-BlockPosHelper-)


[setPosToBlock(x, y, z)](#setPosToBlock-int-int-int-)


[setPosToPoint(pos, radius)](#setPosToPoint-Pos3D-double-)


[setPosToPoint(x, y, z, radius)](#setPosToPoint-double-double-double-double-)


[setColor(color)](#setColor-int-)


[setFillColor(fillColor)](#setFillColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


[setAlpha(alpha)](#setAlpha-int-)


[setFillColor(fillColor, alpha)](#setFillColor-int-int-)


[setFillAlpha(alpha)](#setFillAlpha-int-)


[setFill(fill)](#setFill-boolean-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)


[compareToSame(other)](#compareToSame-Box-)


[render(drawContext, builder, tickDelta)](#render-DrawContext-BufferBuilder-float-)



### Fields

#### .pos


##### Type: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .color


##### Type: int



#### .fillColor


##### Type: int



#### .fill


##### Type: boolean



#### .cull


##### Type: boolean



### Methods

#### .setPos(x1, y1, z1, x2, y2, z2)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |

##### Returns: void



#### .setPosToBlock(pos)

1.9.0

set this component's pos to a block

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |

##### Returns: void



#### .setPosToBlock(x, y, z)

1.9.0

set this component's pos to a block

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: void



#### .setPosToPoint(pos, radius)

1.9.0

set this component's pos to a point

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| radius | double |  |

##### Returns: void



#### .setPosToPoint(x, y, z, radius)

1.9.0

set this component's pos to a point

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| radius | double |  |

##### Returns: void



#### .setColor(color)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: void



#### .setFillColor(fillColor)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| fillColor | int |  |

##### Returns: void



#### .setColor(color, alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| color | int |  |
| alpha | int |  |

##### Returns: void



#### .setAlpha(alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| alpha | int |  |

##### Returns: void



#### .setFillColor(fillColor, alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| fillColor | int |  |
| alpha | int |  |

##### Returns: void



#### .setFillAlpha(alpha)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| alpha | int |  |

##### Returns: void



#### .setFill(fill)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| fill | boolean |  |

##### Returns: void



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
| other | Box |  |

##### Returns: int



#### .render(drawContext, builder, tickDelta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| builder | BufferBuilder |  |
| tickDelta | float |  |

##### Returns: void




