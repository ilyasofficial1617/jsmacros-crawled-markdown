

xyz.wagyourtail.jsmacros.client.api.event.filterer.FiltererBlockUpdate
----------------------------------------------------------------------

#### implements [EventFilterer](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.html)

1.9.1

### Constructors

#### new FiltererBlockUpdate ()




#### Fields

[pos](#pos)


[pos2](#pos2)


[blockId](#blockId)


[blockState](#blockState)


[updateType](#updateType)



#### Methods

[canFilter(event)](#canFilter-String-)


[test(baseEvent)](#test-BaseEvent-)


[setPos(x, y, z)](#setPos-int-int-int-)


[setPos(pos)](#setPos-BlockPosHelper-)


[setArea(x1, y1, z1, x2, y2, z2)](#setArea-int-int-int-int-int-int-)


[setArea(pos1, pos2)](#setArea-BlockPosHelper-BlockPosHelper-)


[setBlockId(id)](#setBlockId-String-)


[setUpdateType(type)](#setUpdateType-String-)


[setBlockStates(states)](#setBlockStates-Map-)


[setBlockState(property, value)](#setBlockState-String-String-)



### Fields

#### .pos


##### Type: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)



#### .pos2

if this and pos are not null, filters area  

this should always be larger or equal than pos


##### Type: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)



#### .blockId


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .blockState


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .updateType


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .canFilter(event)

| Parameter | Type | Description |
|---|---|---|
| event | String |  |

##### Returns: boolean



#### .test(baseEvent)

| Parameter | Type | Description |
|---|---|---|
| baseEvent | BaseEvent |  |

##### Returns: boolean



#### .setPos(x, y, z)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setPos(pos)

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setArea(x1, y1, z1, x2, y2, z2)

| Parameter | Type | Description |
|---|---|---|
| x1 | int |  |
| y1 | int |  |
| z1 | int |  |
| x2 | int |  |
| y2 | int |  |
| z2 | int |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setArea(pos1, pos2)

| Parameter | Type | Description |
|---|---|---|
| pos1 | BlockPosHelper |  |
| pos2 | BlockPosHelper |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setBlockId(id)

| Parameter | Type | Description |
|---|---|---|
| id | String |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setUpdateType(type)

| Parameter | Type | Description |
|---|---|---|
| type | String |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setBlockStates(states)

| Parameter | Type | Description |
|---|---|---|
| states | Map<String, String> |  |

##### Returns: [FiltererBlockUpdate](#)



#### .setBlockState(property, value)

| Parameter | Type | Description |
|---|---|---|
| property | String |  |
| value | String | setting to null will make sure the block doesn't have this property |

##### Returns: [FiltererBlockUpdate](#)




