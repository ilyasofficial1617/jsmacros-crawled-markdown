

xyz.wagyourtail.jsmacros.core.library.impl.FGlobalVars
------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.0.4

"Global" variables for passing to other contexts.

An instance of this class is passed to scripts as the `GlobalVars` variable.

#### Fields

[globalRaw](#globalRaw)
S



#### Methods

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

#### .globalRaw

Static

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>



### Methods

#### .putInt(name, i)

1.0.4

Put an Integer into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| i | int |  |

##### Returns: int



#### .putString(name, str)

1.0.4

put a String into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| str | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .putDouble(name, d)

1.0.8

put a Double into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| d | double |  |

##### Returns: double



#### .putBoolean(name, b)

1.1.7

put a Boolean into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| b | boolean |  |

##### Returns: boolean



#### .putObject(name, o)

1.1.7

put anything else into the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| o | Object |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .getType(name)

1.0.4

Returns the type of the defined item in the global variable space as a string.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getInt(name)

1.0.4

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

Gets an integer from the global variable space. and then decrement it there.

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

1.0.4

Gets a String from the global variable space

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getDouble(name)

1.0.8

Gets a Double from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Double](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Double.html)



#### .getBoolean(name)

1.1.7

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

1.1.7

Gets an Object from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .remove(key)

1.2.0

removes a key from the global variable space.

| Parameter | Type | Description |
|---|---|---|
| key | String |  |

##### Returns: void



#### .getRaw()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>




