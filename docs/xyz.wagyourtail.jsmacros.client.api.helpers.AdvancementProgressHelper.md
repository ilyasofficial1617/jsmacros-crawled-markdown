

xyz.wagyourtail.jsmacros.client.api.helpers.AdvancementProgressHelper
---------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[AdvancementProgress](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/advancement/AdvancementProgress)>

1.8.4

### Constructors

#### new AdvancementProgressHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | AdvancementProgress |  |



#### Methods

[isDone()](#isDone-)


[isAnyObtained()](#isAnyObtained-)


[getCriteria()](#getCriteria-)


[getRequirements()](#getRequirements-)


[getPercentage()](#getPercentage-)


[getFraction()](#getFraction-)


[countObtainedRequirements()](#countObtainedRequirements-)


[getUnobtainedCriteria()](#getUnobtainedCriteria-)


[getObtainedCriteria()](#getObtainedCriteria-)


[getEarliestProgressObtainDate()](#getEarliestProgressObtainDate-)


[getCriterionProgress(criteria)](#getCriterionProgress-String-)


[isCriteriaObtained(criteria)](#isCriteriaObtained-String-)


[toString()](#toString-)



### Methods

#### .isDone()

1.8.4


##### Returns: boolean

`true` if the advancement is finished, `false` otherwise.



#### .isAnyObtained()

1.8.4


##### Returns: boolean

`true` if any criteria has already been met, `false` otherwise.



#### .getCriteria()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Long](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Long.html)>

a map of all criteria and their completion date.



#### .getRequirements()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>

all requirements of this advancement.



#### .getPercentage()

1.8.4


##### Returns: float

the percentage of finished requirements.



#### .getFraction()

1.8.4


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the fraction of finished requirements to total requirements.



#### .countObtainedRequirements()

1.8.4


##### Returns: int

the amount of requirements criteria.



#### .getUnobtainedCriteria()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

the amount/values of missing criteria.



#### .getObtainedCriteria()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

the ids of the finished requirements.



#### .getEarliestProgressObtainDate()

1.8.4


##### Returns: long

the earliest completion date of all criteria.



#### .getCriterionProgress(criteria)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| criteria | String | the criteria |

##### Returns: long

the completion date of the given criteria or `-1` if the criteria is not met
yet.



#### .isCriteriaObtained(criteria)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| criteria | String | the criteria |

##### Returns: boolean

`true` if the given criteria is met, `false` otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




