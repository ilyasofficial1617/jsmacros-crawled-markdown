

xyz.wagyourtail.jsmacros.client.api.helpers.AdvancementManagerHelper
--------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[AdvancementManager](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/advancement/AdvancementManager)>

1.8.4

### Constructors

#### new AdvancementManagerHelper (advancementManager)

| Parameter | Type | Description |
|---|---|---|
| advancementManager | AdvancementManager |  |



#### Methods

[getAdvancementsForIdentifiers()](#getAdvancementsForIdentifiers-)


[getAdvancements()](#getAdvancements-)


[getStartedAdvancements()](#getStartedAdvancements-)


[getMissingAdvancements()](#getMissingAdvancements-)


[getCompletedAdvancements()](#getCompletedAdvancements-)


[getRootAdvancements()](#getRootAdvancements-)


[getSubAdvancements()](#getSubAdvancements-)


[getAdvancement(identifier)](#getAdvancement-String-)


[getAdvancementsProgress()](#getAdvancementsProgress-)


[getAdvancementProgress(identifier)](#getAdvancementProgress-String-)


[toString()](#toString-)



### Methods

#### .getAdvancementsForIdentifiers()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a map of all advancement ids and their advancement.



#### .getAdvancements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all advancements.



#### .getStartedAdvancements()

1.8.4

Started advancements are advancements that have been started, so at least one task has been
completed so far, but not fully completed.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all started advancements.



#### .getMissingAdvancements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all missing advancements.



#### .getCompletedAdvancements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all completed advancements.



#### .getRootAdvancements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all the root advancements.



#### .getSubAdvancements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)>

a list of all advancements that are not a root.



#### .getAdvancement(identifier)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifier | String | the identifier of the advancement |

##### Returns: [AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html)

the advancement for the given identifier.



#### .getAdvancementsProgress()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[AdvancementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementHelper.html), [AdvancementProgressHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementProgressHelper.html)>

a map of all advancements and their progress.



#### .getAdvancementProgress(identifier)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifier | String |  |

##### Returns: [AdvancementProgressHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/AdvancementProgressHelper.html)

the progress of the given advancement.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




