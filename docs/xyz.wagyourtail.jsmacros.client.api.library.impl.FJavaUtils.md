

xyz.wagyourtail.jsmacros.client.api.library.impl.FJavaUtils
-----------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.8.4

#### Methods

[createArrayList()](#createArrayList-)


[createArrayList(array)](#createArrayList-T[]-)


[createHashMap()](#createHashMap-)


[createHashSet()](#createHashSet-)


[getRandom()](#getRandom-)


[getRandom(seed)](#getRandom-long-)


[getHelperFromRaw(raw)](#getHelperFromRaw-Object-)


[arrayToString(array)](#arrayToString-Object[]-)


[arrayDeepToString(array)](#arrayDeepToString-Object[]-)



### Methods

#### .createArrayList()

1.8.4

Creates a java [ArrayList](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/ArrayList.html).


##### Returns: [ArrayList](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/ArrayList.html)< ? >

a java ArrayList.



#### .createArrayList< T >(array)

1.8.4

Creates a java [ArrayList](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/ArrayList.html).

| Parameter | Type | Description |
|---|---|---|
| array | T[] | the array to add to the list |

##### Returns: [ArrayList](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/ArrayList.html)< T >

a java ArrayList from the given array.



#### .createHashMap()

1.8.4

Creates a java [HashMap](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/HashMap.html).


##### Returns: [HashMap](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/HashMap.html)< ? , ? >

a java HashMap.



#### .createHashSet()

1.8.4

Creates a java [HashSet](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/HashSet.html).


##### Returns: [HashSet](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/HashSet.html)< ? >

a java HashSet.



#### .getRandom()

1.8.4

Returns a [SplittableRandom](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/SplittableRandom.html).


##### Returns: [SplittableRandom](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/SplittableRandom.html)

a SplittableRandom.



#### .getRandom(seed)

1.8.4

Returns [SplittableRandom](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/SplittableRandom.html), initialized with the seed to get identical sequences of
values at all times.

| Parameter | Type | Description |
|---|---|---|
| seed | long | the seed |

##### Returns: [SplittableRandom](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/SplittableRandom.html)

a SplittableRandom.



#### .getHelperFromRaw(raw)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| raw | Object | the object to wrap |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)

the correct instance of [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html) for the given object if it exists and
`null` otherwise.



#### .arrayToString(array)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| array | Object[] | the array to convert |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the String representation of the given array.



#### .arrayDeepToString(array)

1.8.4

This method will convert any objects hold in the array data to Strings and should be used for
multidimensional arrays.

| Parameter | Type | Description |
|---|---|---|
| array | Object[] | the array to convert |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the String representation of the given array.




