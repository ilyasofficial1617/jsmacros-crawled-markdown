

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.Line3D
----------------------------------------------------------------------

#### implements [RenderElement3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/RenderElement3D.html)<[Line3D](#)>

### Constructors

#### new Line3D (x1, y1, z1, x2, y2, z2, color, cull)

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |
| color | int |  |
| cull | boolean |  |


#### new Line3D (x1, y1, z1, x2, y2, z2, color, alpha, cull)

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
| cull | boolean |  |



#### Fields

[pos](#pos)


[color](1.9.2/)


[cull](1.9.2/)



#### Methods

[setPos(x1, y1, z1, x2, y2, z2)](#setPos-double-double-double-double-double-double-)


[setColor(color)](#setColor-int-)


[setColor(color, alpha)](#setColor-int-int-)


[setAlpha(alpha)](#setAlpha-int-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)


[compareToSame(o)](#compareToSame-Line3D-)


[render(drawContext, builder, tickDelta)](#render-DrawContext-BufferBuilder-float-)



### Fields

#### .pos


##### Type: [Vec3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Vec3D.html)



#### .color


##### Type: int



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



#### .setColor(color)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

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



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int



#### .compareToSame(o)

| Parameter | Type | Description |
|---|---|---|
| o | Line3D |  |

##### Returns: int



#### .render(drawContext, builder, tickDelta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| builder | BufferBuilder |  |
| tickDelta | float |  |

##### Returns: void




