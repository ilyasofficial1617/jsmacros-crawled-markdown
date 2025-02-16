

xyz.wagyourtail.jsmacros.client.api.classes.worldscanner.WorldScannerBuilder
----------------------------------------------------------------------------

Final
#### 

1.6.5

The builder can be used to create a world scanner with native java functions. This is especially useful for languages like javascript that
don't support multithreading, which causes streams to run sequential instead of parallel.
The builder has two filters for the block and the block state, which need to be configured separately.
If one function is not defined, it will just be ignored when building the scanner.  

The block and block state filters have to start with a 'with' command like [WorldScannerBuilder#withStateFilter(java.lang.String)](#withStateFilter-String-) or [WorldScannerBuilder#withStringBlockFilter()](#withStringBlockFilter-).
This will overwrite all previous filters of the same type. To add more commands, it's possible to use commands with the prefix 'and', 'or', 'xor'.
The 'not' command will just negate the whole block or block state filter and doesn't need any arguments.  


All other commands need some arguments to work. For String functions, it's one of these functions: 'equals', 'contains', 'startsWith', 'endsWith' or 'matches'.
The strings to match are passed as vararg parameters (as many as needed, separated by a comma `is("chest", "barrel", "ore"`) and the filter acts
like a logical or, so only one of the arguments needs to match the criteria. It should be noted, that string functions call the toString method, so
comparing a block with something like "minecraft:stone" will always return false, because the toString method gives "{minecraft:stone}". For doing this
use either contains or the equals method with 'getId', as shown later.  

This will match any block that includes 'stone' or 'diorit' in its name:

```
     withStringBlockFilter().contains("stone") //create new block filter, check if it contains stone
     .orStringBlockFilter().contains("diorit") //append new block filter with or and check if it contains diorit
     
```

For non String functions, the method name must be passed when creating the filter. The names can be any method in [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html) or [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html).
For more complex filters, use the MethodWrapper function [FWorld#getWorldScanner(xyz.wagyourtail.jsmacros.core.MethodWrapper,xyz.wagyourtail.jsmacros.core.MethodWrapper)](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FWorld.html#getWorldScanner-MethodWrapper-MethodWrapper-).
Depending on the return type of the method, the following parameters must be passed to 'is' or 'test'. There are two methods, because 'is' is a keyword in some languages.  


```
     For any number:
       - is(operation, number) with operation = '>', '>=', '<', '<=', '==', '!=' and the number that should be compared to,
         i.e. is(">=", 8) returns true if the returned number is greater or equal to 8.
     For any String:
       - is(method, string) with method = 'EQUALS', 'CONTAINS', 'STARTS_WITH', 'ENDS_WITH', 'MATCHES' and the string is the one to compare the returned value to,
         i.e. is("ENDS_WITH", "ore") checks if the returned string ends with ore (can be used with withBlockFilter("getId")).
     For any Boolean:
       - is(val) with val either true or false
         i.e. is(false) returns true if the returned boolean value is false
     
```
### Constructors

#### new WorldScannerBuilder ()




#### Methods

[withStateFilter(method)](#withStateFilter-String-)


[andStateFilter(method)](#andStateFilter-String-)


[orStateFilter(method)](#orStateFilter-String-)


[notStateFilter()](#notStateFilter-)


[withBlockFilter(method)](#withBlockFilter-String-)


[andBlockFilter(method)](#andBlockFilter-String-)


[orBlockFilter(method)](#orBlockFilter-String-)


[notBlockFilter()](#notBlockFilter-)


[withStringBlockFilter()](#withStringBlockFilter-)


[andStringBlockFilter()](#andStringBlockFilter-)


[orStringBlockFilter()](#orStringBlockFilter-)


[withStringStateFilter()](#withStringStateFilter-)


[andStringStateFilter()](#andStringStateFilter-)


[orStringStateFilter()](#orStringStateFilter-)


[is(args)](#is-Object[]-)


[is(methodArgs, filterArgs)](#is-Object[]-Object[]-)


[test(args)](#test-Object[]-)


[test(methodArgs, filterArgs)](#test-Object[]-Object[]-)


[equals(args)](#equals-String[]-)


[contains(args)](#contains-String[]-)


[startsWith(args)](#startsWith-String[]-)


[endsWith(args)](#endsWith-String[]-)


[matches(args)](#matches-String[]-)


[build()](#build-)



### Methods

#### .withStateFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .andStateFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .orStateFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .notStateFilter()


##### Returns: [WorldScannerBuilder](#)



#### .withBlockFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .andBlockFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .orBlockFilter(method)

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [WorldScannerBuilder](#)



#### .notBlockFilter()


##### Returns: [WorldScannerBuilder](#)



#### .withStringBlockFilter()


##### Returns: [WorldScannerBuilder](#)



#### .andStringBlockFilter()


##### Returns: [WorldScannerBuilder](#)



#### .orStringBlockFilter()


##### Returns: [WorldScannerBuilder](#)



#### .withStringStateFilter()


##### Returns: [WorldScannerBuilder](#)



#### .andStringStateFilter()


##### Returns: [WorldScannerBuilder](#)



#### .orStringStateFilter()


##### Returns: [WorldScannerBuilder](#)



#### .is(args)

| Parameter | Type | Description |
|---|---|---|
| args | Object[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .is(methodArgs, filterArgs)

| Parameter | Type | Description |
|---|---|---|
| methodArgs | Object[] |  |
| filterArgs | Object[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .test(args)

| Parameter | Type | Description |
|---|---|---|
| args | Object[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .test(methodArgs, filterArgs)

| Parameter | Type | Description |
|---|---|---|
| methodArgs | Object[] |  |
| filterArgs | Object[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .equals(args)

| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .contains(args)

| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .startsWith(args)

| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .endsWith(args)

| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .matches(args)

| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: [WorldScannerBuilder](#)



#### .build()


##### Returns: [WorldScanner](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/worldscanner/WorldScanner.html)




