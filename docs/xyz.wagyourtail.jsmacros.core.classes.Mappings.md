

xyz.wagyourtail.jsmacros.core.classes.Mappings
----------------------------------------------

#### 

1.3.1

### Constructors

#### new Mappings (mappingsource)

| Parameter | Type | Description |
|---|---|---|
| mappingsource | String |  |



#### Fields

[mappingsource](#mappingsource)
F



#### Methods

[getMappings()](#getMappings-)


[getReversedMappings()](#getReversedMappings-)


[remapClass(instance)](#remapClass-T-)


[getClass(className)](#getClass-String-)



### Fields

#### .mappingsource

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .getMappings()

1.3.1


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Mappings$ClassData](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.ClassData.html)>

mappings from Intermediary to Named



#### .getReversedMappings()

1.3.1


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Mappings$ClassData](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.ClassData.html)>

mappings from Named to Intermediary



#### .remapClass< T >(instance)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| instance | T |  |

##### Returns: [Mappings$MappedClass](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.MappedClass.html)< T >



#### .getClass(className)

gets the class without instance, so can only access static methods/fields

| Parameter | Type | Description |
|---|---|---|
| className | String |  |

##### Returns: [Mappings$MappedClass](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.MappedClass.html)< ? >




