

xyz.wagyourtail.jsmacros.client.api.helpers.SuggestionsBuilderHelper
--------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[SuggestionsBuilder](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=com/mojang/brigadier/suggestion/SuggestionsBuilder)>

1.6.5

### Constructors

#### new SuggestionsBuilderHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | SuggestionsBuilder |  |



#### Methods

[getInput()](#getInput-)


[getStart()](#getStart-)


[getRemaining()](#getRemaining-)


[getRemainingLowerCase()](#getRemainingLowerCase-)


[suggest(suggestion)](#suggest-String-)


[suggest(value)](#suggest-int-)


[suggestWithTooltip(suggestion, tooltip)](#suggestWithTooltip-String-TextHelper-)


[suggestWithTooltip(value, tooltip)](#suggestWithTooltip-int-TextHelper-)


[suggestMatching(suggestions)](#suggestMatching-String[]-)


[suggestMatching(suggestions)](#suggestMatching-Collection-)


[suggestIdentifier(identifiers)](#suggestIdentifier-String[]-)


[suggestIdentifier(identifiers)](#suggestIdentifier-Collection-)


[suggestBlockPositions(positions)](#suggestBlockPositions-BlockPosHelper[]-)


[suggestBlockPositions(positions)](#suggestBlockPositions-Collection-)


[suggestPositions(positions)](#suggestPositions-String[]-)


[suggestPositions(positions)](#suggestPositions-Collection-)



### Methods

#### .getInput()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getStart()


##### Returns: int



#### .getRemaining()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getRemainingLowerCase()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .suggest(suggestion)

| Parameter | Type | Description |
|---|---|---|
| suggestion | String |  |

##### Returns: [SuggestionsBuilderHelper](#)



#### .suggest(value)

| Parameter | Type | Description |
|---|---|---|
| value | int |  |

##### Returns: [SuggestionsBuilderHelper](#)



#### .suggestWithTooltip(suggestion, tooltip)

| Parameter | Type | Description |
|---|---|---|
| suggestion | String |  |
| tooltip | TextHelper |  |

##### Returns: [SuggestionsBuilderHelper](#)



#### .suggestWithTooltip(value, tooltip)

| Parameter | Type | Description |
|---|---|---|
| value | int |  |
| tooltip | TextHelper |  |

##### Returns: [SuggestionsBuilderHelper](#)



#### .suggestMatching(suggestions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestions | String[] | the strings to match |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestMatching(suggestions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestions | Collection<String> | the strings to match |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestIdentifier(identifiers)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifiers | String[] | the identifiers to match |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestIdentifier(identifiers)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifiers | Collection<String> | the identifiers to match |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestBlockPositions(positions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| positions | BlockPosHelper[] | the positions to suggest |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestBlockPositions(positions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| positions | Collection<BlockPosHelper> | the positions to suggest |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestPositions(positions)

1.8.4

Positions are strings of the form "x y z" where x, y, and z are numbers or the default
minecraft selectors "~" and "^" followed by a number.

| Parameter | Type | Description |
|---|---|---|
| positions | String[] | the positions to suggest |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.



#### .suggestPositions(positions)

1.8.4

Positions are strings of the form "x y z" where x, y, and z are numbers or the default
minecraft selectors "~" and "^" followed by a number.

| Parameter | Type | Description |
|---|---|---|
| positions | Collection<String> | the relative positions to suggest |

##### Returns: [SuggestionsBuilderHelper](#)

self for chaining.




