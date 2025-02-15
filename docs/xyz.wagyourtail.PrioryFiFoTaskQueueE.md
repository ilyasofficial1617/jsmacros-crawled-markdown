

xyz.wagyourtail.PrioryFiFoTaskQueue< E >
----------------------------------------

#### implements [Queue](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Queue.html)< E >

### Constructors

#### new PrioryFiFoTaskQueue (priorityFunction)

| Parameter | Type | Description |
|---|---|---|
| priorityFunction | Function<E, Integer> |  |



#### Methods

[size()](#size-)


[isEmpty()](#isEmpty-)


[contains(o)](#contains-Object-)


[iterator()](#iterator-)


[toArray()](#toArray-)


[toArray(ts)](#toArray-T[]-)


[add(e)](#add-E-)


[remove(o)](#remove-Object-)


[containsAll(collection)](#containsAll-Collection-)


[addAll(collection)](#addAll-Collection-)


[removeAll(collection)](#removeAll-Collection-)


[retainAll(collection)](#retainAll-Collection-)


[clear()](#clear-)


[offer(e)](#offer-E-)


[remove()](#remove-)


[poll()](#poll-)


[pollWaiting()](#pollWaiting-)


[pollWaiting(timeout)](#pollWaiting-long-)


[peekWaiting()](#peekWaiting-)


[peekWaiting(timeout)](#peekWaiting-long-)


[element()](#element-)


[peek()](#peek-)



### Methods

#### .size()


##### Returns: int



#### .isEmpty()


##### Returns: boolean



#### .contains(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .iterator()


##### Returns: [Iterator](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Iterator.html)< E >



#### .toArray()


##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)[]



#### .toArray< T >(ts)

| Parameter | Type | Description |
|---|---|---|
| ts | T[] |  |

##### Returns: T []



#### .add(e)

| Parameter | Type | Description |
|---|---|---|
| e | E |  |

##### Returns: boolean



#### .remove(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .containsAll(collection)

| Parameter | Type | Description |
|---|---|---|
| collection | Collection<?> |  |

##### Returns: boolean



#### .addAll(collection)

| Parameter | Type | Description |
|---|---|---|
| collection | Collection<?> |  |

##### Returns: boolean



#### .removeAll(collection)

| Parameter | Type | Description |
|---|---|---|
| collection | Collection<?> |  |

##### Returns: boolean



#### .retainAll(collection)

| Parameter | Type | Description |
|---|---|---|
| collection | Collection<?> |  |

##### Returns: boolean



#### .clear()


##### Returns: void



#### .offer(e)

| Parameter | Type | Description |
|---|---|---|
| e | E |  |

##### Returns: boolean



#### .remove()


##### Returns: E



#### .poll()


##### Returns: E



#### .pollWaiting()


##### Returns: E



#### .pollWaiting(timeout)

| Parameter | Type | Description |
|---|---|---|
| timeout | long |  |

##### Returns: E



#### .peekWaiting()


##### Returns: E



#### .peekWaiting(timeout)

| Parameter | Type | Description |
|---|---|---|
| timeout | long |  |

##### Returns: E



#### .element()


##### Returns: E



#### .peek()


##### Returns: E




