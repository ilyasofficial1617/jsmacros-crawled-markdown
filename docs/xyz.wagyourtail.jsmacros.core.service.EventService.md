

xyz.wagyourtail.jsmacros.core.service.EventService
--------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.6.4

### Constructors

#### new EventService (name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |



#### Fields

[serviceName](#serviceName)
F


[stopListener](#stopListener)


[postStopListener](#postStopListener)



#### Methods

[unregisterOnStop(offEvents, list)](#unregisterOnStop-boolean-Registrable[]-)


[toString()](#toString-)


[putInt(name, i)](#putInt-String-int-)


[putString(name, str)](#putString-String-String-)


[putDouble(name, d)](#putDouble-String-double-)


[putBoolean(name, b)](#putBoolean-String-boolean-)


[putObject(name, o)](#putObject-String-Object-)


[getType(name)](#getType-String-)


[getInt(name)](#getInt-String-)


[getAndIncrementInt(name)](#getAndIncrementInt-String-)


[getAndDecrementInt(name)](#getAndDecrementInt-String-)


[incrementAndGetInt(name)](#incrementAndGetInt-String-)


[decrementAndGetInt(name)](#decrementAndGetInt-String-)


[getString(name)](#getString-String-)


[getDouble(name)](#getDouble-String-)


[getBoolean(name)](#getBoolean-String-)


[toggleBoolean(name)](#toggleBoolean-String-)


[getObject(name)](#getObject-String-)


[remove(key)](#remove-String-)


[getRaw()](#getRaw-)



### Fields

#### .serviceName

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .stopListener

when this service is stopped, this is run...


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .postStopListener

1.9.1


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



### Methods

#### .unregisterOnStop(offEvents, list)

1.9.1

Setup unregister on stop. For example, `event.unregisterOnStop(false, d2d);` is
the equivalent of `event.stopListener = JavaWrapper.methodToJava(() => d2d.unregister());`.  

  

If this is called multiple times, the previous ones would be discarded.  

  

The order of execution is run stopListener -> off events -> unregister stuff -> run postStopListener.  

  

If anything was set to unregister, the service won't stop by itself even if it reaches the end.

| Parameter | Type | Description |
|---|---|---|
| offEvents | boolean | whether the service manager should clear event listeners that the callback doesn't belong to this context. |
| list | Registrable<?>[] | the list of registrable, such as Draw2D, Draw3D and CommandBuilder. |

##### Returns: void



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .putInt(name, i)

1.6.5

Put an Integer into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| i | int |  |

##### Returns: int



#### .putString(name, str)

1.6.5

put a String into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| str | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .putDouble(name, d)

1.6.5

put a Double into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| d | double |  |

##### Returns: double



#### .putBoolean(name, b)

1.6.5

put a Boolean into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| b | boolean |  |

##### Returns: boolean



#### .putObject(name, o)

1.6.5

put anything else into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| o | Object |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .getType(name)

1.6.5

Returns the type of the defined item in the global variable space as a string.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getInt(name)

1.6.5

Gets an Integer from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .getAndIncrementInt(name)

1.6.5

Gets an Integer from the global variable space. and then increment it there.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .getAndDecrementInt(name)

1.6.5

Gets an integer from the global variable pace. and then decrement it there.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .incrementAndGetInt(name)

1.6.5

increment an Integer in the global variable space. then return it.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .decrementAndGetInt(name)

1.6.5

decrement an Integer in the global variable space. then return it.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)



#### .getString(name)

1.6.5

Gets a String from the global variable space

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getDouble(name)

1.6.5

Gets a Double from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Double](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Double.html)



#### .getBoolean(name)

1.6.5

Gets a Boolean from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html)



#### .toggleBoolean(name)

1.6.5

toggles a global boolean and returns its new value

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html)



#### .getObject(name)

1.6.5

Gets an Object from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .remove(key)

1.6.5

removes a key from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| key | String |  |

##### Returns: void



#### .getRaw()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>




