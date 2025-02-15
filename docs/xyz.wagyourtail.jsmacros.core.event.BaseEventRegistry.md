
[EventRegistry](1.9.2/xyz/wagyourtail/jsmacros/client/event/EventRegistry.html)

xyz.wagyourtail.jsmacros.core.event.BaseEventRegistry
-----------------------------------------------------

Abstract
#### 

1.2.7

### Constructors

#### new BaseEventRegistry (runner)

| Parameter | Type | Description |
|---|---|---|
| runner | Core |  |



#### Fields

[oldEvents](#oldEvents)
F


[events](#events)
F


[cancellableEvents](#cancellableEvents)
F


[joinableEvents](#joinableEvents)
F


[filterableEvents](#filterableEvents)
F



#### Methods

[clearMacros()](#clearMacros-)


[addScriptTrigger(rawmacro)](#addScriptTrigger-ScriptTrigger-)
A


[addListener(event, listener)](#addListener-String-IEventListener-)


[removeListener(event, listener)](#removeListener-String-IEventListener-)


[removeListener(listener)](#removeListener-IEventListener-)
D


[removeScriptTrigger(rawmacro)](#removeScriptTrigger-ScriptTrigger-)
A


[getListeners()](#getListeners-)


[getListeners(key)](#getListeners-String-)


[getScriptTriggers()](#getScriptTriggers-)
A


[addEvent(eventName)](#addEvent-String-)


[addEvent(eventName, joinable)](#addEvent-String-boolean-)


[addEvent(eventName, joinable, cancellable)](#addEvent-String-boolean-boolean-)


[addEvent(clazz)](#addEvent-Class-)



### Fields

#### .oldEvents

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .events

Final

##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .cancellableEvents

Final

##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .joinableEvents

Final

##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .filterableEvents

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>



### Methods

#### .clearMacros()


##### Returns: void



#### .addScriptTrigger(rawmacro)

Abstract

1.1.2 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| rawmacro | ScriptTrigger |  |

##### Returns: void



#### .addListener(event, listener)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| listener | IEventListener |  |

##### Returns: void



#### .removeListener(event, listener)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| listener | IEventListener |  |

##### Returns: boolean



#### .removeListener(listener)

Deprecated

1.2.3

| Parameter | Type | Description |
|---|---|---|
| listener | IEventListener |  |

##### Returns: boolean



#### .removeScriptTrigger(rawmacro)

Abstract

1.1.2 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| rawmacro | ScriptTrigger |  |

##### Returns: boolean



#### .getListeners()

1.2.3


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)>>



#### .getListeners(key)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| key | String |  |

##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)>



#### .getScriptTriggers()

Abstract

1.1.2 [citation needed]


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ScriptTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/config/ScriptTrigger.html)>



#### .addEvent(eventName)

1.1.2 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| eventName | String |  |

##### Returns: void



#### .addEvent(eventName, joinable)

| Parameter | Type | Description |
|---|---|---|
| eventName | String |  |
| joinable | boolean |  |

##### Returns: void



#### .addEvent(eventName, joinable, cancellable)

| Parameter | Type | Description |
|---|---|---|
| eventName | String |  |
| joinable | boolean |  |
| cancellable | boolean |  |

##### Returns: void



#### .addEvent(clazz)

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> |  |

##### Returns: void




