

xyz.wagyourtail.jsmacros.client.api.classes.render.components3d.EntityTraceLine
-------------------------------------------------------------------------------

#### extends [TraceLine](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/TraceLine.html)

1.9.0

### Constructors

#### new EntityTraceLine (entity, color, yOffset)

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| color | int |  |
| yOffset | double |  |


#### new EntityTraceLine (entity, color, alpha, yOffset)

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| color | int |  |
| alpha | int |  |
| yOffset | double |  |



#### Fields

[dirty](1.9.2/)
S


[entity](#entity)


[yOffset](1.9.2/)


[shouldRemove](1.9.2/)



#### Methods

[setEntity(entity)](#setEntity-EntityHelper-)


[setYOffset(yOffset)](#setYOffset-double-)


[render(drawContext, builder, tickDelta)](#render-DrawContext-BufferBuilder-float-)



### Fields

#### .dirty

Static

##### Type: boolean



#### .entity


##### Type: [Entity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/Entity)



#### .yOffset


##### Type: double



#### .shouldRemove


##### Type: boolean



### Methods

#### .setEntity(entity)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |

##### Returns: [EntityTraceLine](#)

self for chaining



#### .setYOffset(yOffset)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| yOffset | double |  |

##### Returns: [EntityTraceLine](#)

self for chaining



#### .render(drawContext, builder, tickDelta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| builder | BufferBuilder |  |
| tickDelta | float |  |

##### Returns: void




