

xyz.wagyourtail.StringHashTrie
------------------------------

#### implements [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

Is this even faster than just iterating through a LinkedHashSet / HashSet at this point?
also should the node-length just always be 1?

### Constructors

#### new StringHashTrie ()




#### Methods

[size()](#size-)


[isEmpty()](#isEmpty-)


[contains(o)](#contains-Object-)


[iterator()](#iterator-)


[toArray()](#toArray-)


[toArray(a)](#toArray-T[]-)


[add(s)](#add-String-)


[remove(o)](#remove-Object-)


[containsAll(c)](#containsAll-Collection-)


[containsAll(o)](#containsAll-String[]-)


[addAll(c)](#addAll-Collection-)


[addAll(o)](#addAll-String[]-)


[removeAll(c)](#removeAll-Collection-)


[removeAll(o)](#removeAll-String[]-)


[retainAll(c)](#retainAll-Collection-)


[retainAll(o)](#retainAll-String[]-)


[clear()](#clear-)


[getAllWithPrefix(prefix)](#getAllWithPrefix-String-)


[getAllWithPrefixCaseInsensitive(prefix)](#getAllWithPrefixCaseInsensitive-String-)


[getAll()](#getAll-)


[toString()](#toString-)



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


##### Returns: [Iterator](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Iterator.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .toArray()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]



#### .toArray< T >(a)

| Parameter | Type | Description |
|---|---|---|
| a | T[] |  |

##### Returns: T []



#### .add(s)

| Parameter | Type | Description |
|---|---|---|
| s | String |  |

##### Returns: boolean



#### .remove(o)

this can make the StringHashTrie sparse, this can cause extra steps in lookup that are no longer needed,
at some point it would be best to rebase the StringHashTrie with `new StringHashTrie().addAll(current.getAll())`

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .containsAll(c)

| Parameter | Type | Description |
|---|---|---|
| c | Collection<?> |  |

##### Returns: boolean



#### .containsAll(o)

| Parameter | Type | Description |
|---|---|---|
| o | String[] |  |

##### Returns: boolean



#### .addAll(c)

| Parameter | Type | Description |
|---|---|---|
| c | Collection<?> |  |

##### Returns: boolean



#### .addAll(o)

| Parameter | Type | Description |
|---|---|---|
| o | String[] |  |

##### Returns: boolean



#### .removeAll(c)

| Parameter | Type | Description |
|---|---|---|
| c | Collection<?> |  |

##### Returns: boolean



#### .removeAll(o)

| Parameter | Type | Description |
|---|---|---|
| o | String[] |  |

##### Returns: boolean



#### .retainAll(c)

| Parameter | Type | Description |
|---|---|---|
| c | Collection<?> |  |

##### Returns: boolean



#### .retainAll(o)

| Parameter | Type | Description |
|---|---|---|
| o | String[] |  |

##### Returns: boolean



#### .clear()


##### Returns: void



#### .getAllWithPrefix(prefix)

| Parameter | Type | Description |
|---|---|---|
| prefix | String | prefix to search with |

##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

all elements that start with the given prefix



#### .getAllWithPrefixCaseInsensitive(prefix)

| Parameter | Type | Description |
|---|---|---|
| prefix | String | prefix to search with |

##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

all elements that start with the given prefix (case insensitive)



#### .getAll()

all contained elements as a [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

json representation, mainly for debugging.




