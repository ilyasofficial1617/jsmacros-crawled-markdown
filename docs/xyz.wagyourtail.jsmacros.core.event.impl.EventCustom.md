

xyz.wagyourtail.jsmacros.core.event.impl.EventCustom
----------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.2.8

Custom Events

### Constructors

#### new EventCustom (eventName)

| Parameter | Type | Description |
|---|---|---|
| eventName | String | name of the event. please don't use an existing one... your scripts might not like that. |



#### Fields

[eventName](#eventName)


[joinable](1.9.2/)


[cancelable](1.9.2/)



#### Methods

[joinable()](#joinable-)


[cancellable()](#cancellable-)


[trigger()](#trigger-)


[triggerAsync(callback)](#triggerAsync-MethodWrapper-)


[putInt(name, i)](#putInt-String-int-)


[putString(name, str)](#putString-String-String-)


[putDouble(name, d)](#putDouble-String-double-)


[putBoolean(name, b)](#putBoolean-String-boolean-)


[putObject(name, o)](#putObject-String-Object-)


[getType(name)](#getType-String-)


[getInt(name)](#getInt-String-)


[getString(name)](#getString-String-)


[getDouble(name)](#getDouble-String-)


[getBoolean(name)](#getBoolean-String-)


[getObject(name)](#getObject-String-)


[getUnderlyingMap()](#getUnderlyingMap-)


[registerEvent()](#registerEvent-)



### Fields

#### .eventName


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .joinable


##### Type: boolean



#### .cancelable


##### Type: boolean



### Methods

#### .joinable()


##### Returns: boolean



#### .cancellable()


##### Returns: boolean



#### .trigger()

1.2.8

Triggers the event.
Try not to cause infinite looping by triggering the same [EventCustom](#) from its own listeners.


##### Returns: void



#### .triggerAsync(callback)

1.9.0

trigger the event listeners, then run `callback` when they finish.

| Parameter | Type | Description |
|---|---|---|
| callback | MethodWrapper<Object, Object, Object, ?> | used as a Runnable, so no args, no return value. |

##### Returns: void



#### .putInt(name, i)

1.2.8

Put an Integer into the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| i | int |  |

##### Returns: int



#### .putString(name, str)

1.2.8

put a String into the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| str | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .putDouble(name, d)

1.2.8

put a Double into the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| d | double |  |

##### Returns: double



#### .putBoolean(name, b)

1.2.8

put a Boolean into the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| b | boolean |  |

##### Returns: boolean



#### .putObject(name, o)

1.2.8

put anything else into the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| o | Object |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .getType(name)

1.2.8

Returns the type of the defined item in the event as a string.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getInt(name)

1.2.8

Gets an Integer from the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .getString(name)

1.2.8

Gets a String from the event

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getDouble(name)

1.2.8

Gets a Double from the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Double](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Double.html)



#### .getBoolean(name)

1.2.8

Gets a Boolean from the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html)



#### .getObject(name)

1.2.8

Gets an Object from the event.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .getUnderlyingMap()

1.6.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>

map backing the event



#### .registerEvent()

1.3.0

registers event so you can see it in the gui


##### Returns: void




