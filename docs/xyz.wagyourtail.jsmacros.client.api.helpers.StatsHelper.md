

xyz.wagyourtail.jsmacros.client.api.helpers.StatsHelper
-------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[StatHandler](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/stat/StatHandler)>

### Constructors

#### new StatsHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | StatHandler |  |



#### Methods

[getStatList()](#getStatList-)


[getStatText(statKey)](#getStatText-String-)


[getRawStatValue(statKey)](#getRawStatValue-String-)


[getFormattedStatValue(statKey)](#getFormattedStatValue-String-)


[getFormattedStatMap()](#getFormattedStatMap-)


[getRawStatMap()](#getRawStatMap-)


[getEntityKilled(id)](#getEntityKilled-String-)


[getKilledByEntity(id)](#getKilledByEntity-String-)


[getBlockMined(id)](#getBlockMined-String-)


[getItemBroken(id)](#getItemBroken-String-)


[getItemCrafted(id)](#getItemCrafted-String-)


[getItemUsed(id)](#getItemUsed-String-)


[getItemPickedUp(id)](#getItemPickedUp-String-)


[getItemDropped(id)](#getItemDropped-String-)


[getCustomStat(id)](#getCustomStat-String-)


[getCustomFormattedStat(id)](#getCustomFormattedStat-String-)


[updateStatistics()](#updateStatistics-)


[toString()](#toString-)



### Methods

#### .getStatList()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getStatText(statKey)

| Parameter | Type | Description |
|---|---|---|
| statKey | String |  |

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .getRawStatValue(statKey)

| Parameter | Type | Description |
|---|---|---|
| statKey | String |  |

##### Returns: int



#### .getFormattedStatValue(statKey)

| Parameter | Type | Description |
|---|---|---|
| statKey | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getFormattedStatMap()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getRawStatMap()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)>



#### .getEntityKilled(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the entity |

##### Returns: int

how many times the player has killed the entity.



#### .getKilledByEntity(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the entity |

##### Returns: int

how many times the player has killed the specified entity.



#### .getBlockMined(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the block |

##### Returns: int

how many times the player has mined the block.



#### .getItemBroken(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the item |

##### Returns: int

how many times the player has broken the item.



#### .getItemCrafted(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the item |

##### Returns: int

how many times the player has crafted the item.



#### .getItemUsed(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the item |

##### Returns: int

how many times the player has used the item.



#### .getItemPickedUp(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the item |

##### Returns: int

how many times the player has picked up the item.



#### .getItemDropped(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the item |

##### Returns: int

how many times the player has dropped the item.



#### .getCustomStat(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the custom stat |

##### Returns: int

the value of the custom stat.



#### .getCustomFormattedStat(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier of the custom stat |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the formatted value of the custom stat.



#### .updateStatistics()

1.8.4

Used to request an update of the statistics from the server.


##### Returns: [StatsHelper](#)

self for chaining.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




