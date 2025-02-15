

xyz.wagyourtail.jsmacros.client.config.ClientConfigV2
-----------------------------------------------------

#### 

### Constructors

#### new ClientConfigV2 ()




#### Fields

[sortMethod](#sortMethod)


[sortServicesMethod](#sortServicesMethod)


[showSlotIndexes](1.9.2/)


[disableKeyWhenScreenOpen](1.9.2/)


[editorTheme](#editorTheme)


[editorLinterOverrides](#editorLinterOverrides)


[editorHistorySize](1.9.2/)


[editorSuggestions](1.9.2/)


[editorFont](#editorFont)


[externalEditor](1.9.2/)


[externalEditorCommand](#externalEditorCommand)


[showRunningServices](1.9.2/)


[serviceAutoReload](1.9.2/)



#### Methods

[languages()](#languages-)


[getFonts()](#getFonts-)


[getThemeData()](#getThemeData-)


[setServiceAutoReload(value)](#setServiceAutoReload-boolean-)


[getSortComparator()](#getSortComparator-)


[getServiceSortComparator()](#getServiceSortComparator-)


[fromV1(v1)](#fromV1-JsonObject-)
D



### Fields

#### .sortMethod


##### Type: [Sorting$MacroSortMethod](1.9.2/xyz/wagyourtail/jsmacros/client/config/Sorting.MacroSortMethod.html)



#### .sortServicesMethod


##### Type: [Sorting$ServiceSortMethod](1.9.2/xyz/wagyourtail/jsmacros/client/config/Sorting.ServiceSortMethod.html)



#### .showSlotIndexes


##### Type: boolean



#### .disableKeyWhenScreenOpen


##### Type: boolean



#### .editorTheme


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), short []>



#### .editorLinterOverrides


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .editorHistorySize


##### Type: int



#### .editorSuggestions


##### Type: boolean



#### .editorFont


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .externalEditor


##### Type: boolean



#### .externalEditorCommand


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .showRunningServices


##### Type: boolean



#### .serviceAutoReload


##### Type: boolean



### Methods

#### .languages()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getFonts()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getThemeData()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), short []>



#### .setServiceAutoReload(value)

| Parameter | Type | Description |
|---|---|---|
| value | boolean |  |

##### Returns: void



#### .getSortComparator()


##### Returns: [Comparator](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Comparator.html)<[ScriptTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/config/ScriptTrigger.html)>



#### .getServiceSortComparator()


##### Returns: [Comparator](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Comparator.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .fromV1(v1)

Deprecated
| Parameter | Type | Description |
|---|---|---|
| v1 | JsonObject |  |

##### Returns: void




