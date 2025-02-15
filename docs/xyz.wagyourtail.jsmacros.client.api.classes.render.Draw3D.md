

xyz.wagyourtail.jsmacros.client.api.classes.render.Draw3D
---------------------------------------------------------

#### implements [Registrable](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Registrable.html)<[Draw3D](#)>

1.0.6

[Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html) is cool

### Constructors

#### new Draw3D ()




#### Methods

[getBoxes()](#getBoxes-)


[getLines()](#getLines-)


[getTraceLines()](#getTraceLines-)


[getEntityTraceLines()](#getEntityTraceLines-)


[getDraw2Ds()](#getDraw2Ds-)


[clear()](#clear-)


[reAddElement(element)](#reAddElement-RenderElement3D-)


[addBox(box)](#addBox-Box-)


[addLine(line)](#addLine-Line3D-)


[addTraceLine(line)](#addTraceLine-TraceLine-)


[addSurface(surface)](#addSurface-Surface-)


[addBox(x1, y1, z1, x2, y2, z2, color, fillColor, fill)](#addBox-double-double-double-double-double-double-int-int-boolean-)


[addBox(x1, y1, z1, x2, y2, z2, color, fillColor, fill, cull)](#addBox-double-double-double-double-double-double-int-int-boolean-boolean-)


[addBox(x1, y1, z1, x2, y2, z2, color, alpha, fillColor, fillAlpha, fill)](#addBox-double-double-double-double-double-double-int-int-int-int-boolean-)


[addBox(x1, y1, z1, x2, y2, z2, color, alpha, fillColor, fillAlpha, fill, cull)](#addBox-double-double-double-double-double-double-int-int-int-int-boolean-boolean-)


[removeBox(b)](#removeBox-Box-)


[addLine(x1, y1, z1, x2, y2, z2, color)](#addLine-double-double-double-double-double-double-int-)


[addLine(x1, y1, z1, x2, y2, z2, color, cull)](#addLine-double-double-double-double-double-double-int-boolean-)


[addLine(x1, y1, z1, x2, y2, z2, color, alpha)](#addLine-double-double-double-double-double-double-int-int-)


[addLine(x1, y1, z1, x2, y2, z2, color, alpha, cull)](#addLine-double-double-double-double-double-double-int-int-boolean-)


[removeLine(l)](#removeLine-Line3D-)


[addTraceLine(x, y, z, color)](#addTraceLine-double-double-double-int-)


[addTraceLine(x, y, z, color, alpha)](#addTraceLine-double-double-double-int-int-)


[addTraceLine(pos, color)](#addTraceLine-Pos3D-int-)


[addTraceLine(pos, color, alpha)](#addTraceLine-Pos3D-int-int-)


[addEntityTraceLine(entity, color)](#addEntityTraceLine-EntityHelper-int-)


[addEntityTraceLine(entity, color, alpha)](#addEntityTraceLine-EntityHelper-int-int-)


[addEntityTraceLine(entity, color, alpha, yOffset)](#addEntityTraceLine-EntityHelper-int-int-double-)


[removeTraceLine(traceLine)](#removeTraceLine-TraceLine-)


[addPoint(point, radius, color)](#addPoint-Pos3D-double-int-)


[addPoint(x, y, z, radius, color)](#addPoint-double-double-double-double-int-)


[addPoint(x, y, z, radius, color, alpha, cull)](#addPoint-double-double-double-double-int-int-boolean-)


[addDraw2D(x, y, z)](#addDraw2D-double-double-double-)


[addDraw2D(x, y, z, width, height)](#addDraw2D-double-double-double-double-double-)


[addDraw2D(x, y, z, xRot, yRot, zRot)](#addDraw2D-double-double-double-double-double-double-)


[addDraw2D(x, y, z, xRot, yRot, zRot, width, height)](#addDraw2D-double-double-double-double-double-double-double-double-)


[addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions)](#addDraw2D-double-double-double-double-double-double-double-double-int-)


[addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions, renderBack)](#addDraw2D-double-double-double-double-double-double-double-double-int-boolean-)


[addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions, renderBack, cull)](#addDraw2D-double-double-double-double-double-double-double-double-int-boolean-boolean-)


[removeDraw2D(surface)](#removeDraw2D-Surface-)


[boxBuilder()](#boxBuilder-)


[boxBuilder(pos)](#boxBuilder-BlockPosHelper-)


[boxBuilder(x, y, z)](#boxBuilder-int-int-int-)


[lineBuilder()](#lineBuilder-)


[traceLineBuilder()](#traceLineBuilder-)


[entityTraceLineBuilder()](#entityTraceLineBuilder-)


[surfaceBuilder()](#surfaceBuilder-)


[register()](#register-)


[unregister()](#unregister-)


[render(drawContext, tickDelta)](#render-DrawContext-float-)



### Methods

#### .getBoxes()

1.0.6


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)>



#### .getLines()

1.0.6


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)>



#### .getTraceLines()

1.9.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)>



#### .getEntityTraceLines()

1.9.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)>



#### .getDraw2Ds()

1.6.5


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)>



#### .clear()

1.8.4


##### Returns: void



#### .reAddElement(element)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| element | RenderElement3D |  |

##### Returns: void



#### .addBox(box)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| box | Box |  |

##### Returns: void



#### .addLine(line)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| line | Line3D |  |

##### Returns: void



#### .addTraceLine(line)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| line | TraceLine |  |

##### Returns: void



#### .addSurface(surface)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| surface | Surface |  |

##### Returns: void



#### .addBox(x1, y1, z1, x2, y2, z2, color, fillColor, fill)

1.0.6

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

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

The [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html) you added.



#### .addBox(x1, y1, z1, x2, y2, z2, color, fillColor, fill, cull)

1.3.1

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

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)



#### .addBox(x1, y1, z1, x2, y2, z2, color, alpha, fillColor, fillAlpha, fill)

1.1.8

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

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html) you added.



#### .addBox(x1, y1, z1, x2, y2, z2, color, alpha, fillColor, fillAlpha, fill, cull)

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

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)



#### .removeBox(b)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| b | Box |  |

##### Returns: [Draw3D](#)



#### .addLine(x1, y1, z1, x2, y2, z2, color)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| x1 | double |  |
| y1 | double |  |
| z1 | double |  |
| x2 | double |  |
| y2 | double |  |
| z2 | double |  |
| color | int |  |

##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)

the [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html) you added.



#### .addLine(x1, y1, z1, x2, y2, z2, color, cull)

1.3.1

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

##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)



#### .addLine(x1, y1, z1, x2, y2, z2, color, alpha)

1.1.8

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

##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)

the [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html) you added.



#### .addLine(x1, y1, z1, x2, y2, z2, color, alpha, cull)

1.3.1

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

##### Returns: [Line3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.html)



#### .removeLine(l)

1.0.6

| Parameter | Type | Description |
|---|---|---|
| l | Line3D |  |

##### Returns: [Draw3D](#)



#### .addTraceLine(x, y, z, color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| color | int |  |

##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)



#### .addTraceLine(x, y, z, color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| color | int |  |
| alpha | int |  |

##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)



#### .addTraceLine(pos, color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| color | int |  |

##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)



#### .addTraceLine(pos, color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D |  |
| color | int |  |
| alpha | int |  |

##### Returns: [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)



#### .addEntityTraceLine(entity, color)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| color | int |  |

##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)



#### .addEntityTraceLine(entity, color, alpha)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| color | int |  |
| alpha | int |  |

##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)



#### .addEntityTraceLine(entity, color, alpha, yOffset)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| color | int |  |
| alpha | int |  |
| yOffset | double |  |

##### Returns: [EntityTraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.html)



#### .removeTraceLine(traceLine)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| traceLine | TraceLine |  |

##### Returns: [Draw3D](#)

self for chaining



#### .addPoint(point, radius, color)

1.4.0

Draws a cube([Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)) with a specific radius(`side length = 2*radius`)

| Parameter | Type | Description |
|---|---|---|
| point | Pos3D | the center point |
| radius | double | 1/2 of the side length of the cube |
| color | int | point color |

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html) generated, and visualized



#### .addPoint(x, y, z, radius, color)

1.4.0

Draws a cube([Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)) with a specific radius(`side length = 2*radius`)

| Parameter | Type | Description |
|---|---|---|
| x | double | x value of the center point |
| y | double | y value of the center point |
| z | double | z value of the center point |
| radius | double | 1/2 of the side length of the cube |
| color | int | point color |

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html) generated, and visualized



#### .addPoint(x, y, z, radius, color, alpha, cull)

1.4.0

Draws a cube([Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)) with a specific radius(`side length = 2*radius`)

| Parameter | Type | Description |
|---|---|---|
| x | double | x value of the center point |
| y | double | y value of the center point |
| z | double | z value of the center point |
| radius | double | 1/2 of the side length of the cube |
| color | int | point color |
| alpha | int | alpha of the point |
| cull | boolean | whether to cull the point or not |

##### Returns: [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html)

the [Box](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.html) generated, and visualized



#### .addDraw2D(x, y, z)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double | top left |
| y | double |  |
| z | double |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, width, height)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| width | double |  |
| height | double |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, xRot, yRot, zRot)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| xRot | double |  |
| yRot | double |  |
| zRot | double |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, xRot, yRot, zRot, width, height)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| xRot | double |  |
| yRot | double |  |
| zRot | double |  |
| width | double |  |
| height | double |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| xRot | double |  |
| yRot | double |  |
| zRot | double |  |
| width | double |  |
| height | double |  |
| minSubdivisions | int |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions, renderBack)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double |  |
| y | double |  |
| z | double |  |
| xRot | double |  |
| yRot | double |  |
| zRot | double |  |
| width | double |  |
| height | double |  |
| minSubdivisions | int |  |
| renderBack | boolean |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .addDraw2D(x, y, z, xRot, yRot, zRot, width, height, minSubdivisions, renderBack, cull)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| x | double | top left |
| y | double |  |
| z | double |  |
| xRot | double |  |
| yRot | double |  |
| zRot | double |  |
| width | double |  |
| height | double |  |
| minSubdivisions | int |  |
| renderBack | boolean |  |
| cull | boolean |  |

##### Returns: [Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html)



#### .removeDraw2D(surface)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| surface | Surface |  |

##### Returns: void



#### .boxBuilder()

1.8.4


##### Returns: [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html)

a new [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html) instance.



#### .boxBuilder(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the block position of the box |

##### Returns: [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html)

a new [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html) instance.



#### .boxBuilder(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the box |
| y | int | the y coordinate of the box |
| z | int | the z coordinate of the box |

##### Returns: [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html)

a new [Box$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Box.Builder.html) instance.



#### .lineBuilder()

1.8.4


##### Returns: [Line3D$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.Builder.html)

a new [Line3D$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Line3D.Builder.html) instance.



#### .traceLineBuilder()

1.9.0


##### Returns: [TraceLine$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.Builder.html)

a new [TraceLine$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.Builder.html) instance.



#### .entityTraceLineBuilder()

1.9.0


##### Returns: [EntityTraceLine$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.Builder.html)

a new [EntityTraceLine$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/EntityTraceLine.Builder.html) instance.



#### .surfaceBuilder()

1.8.4


##### Returns: [Surface$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.Builder.html)

a new [Surface$Builder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.Builder.html) instance.



#### .register()

1.6.5

register so it actually shows up


##### Returns: [Draw3D](#)

self for chaining



#### .unregister()

1.6.5


##### Returns: [Draw3D](#)

self for chaining



#### .render(drawContext, tickDelta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| tickDelta | float |  |

##### Returns: void




