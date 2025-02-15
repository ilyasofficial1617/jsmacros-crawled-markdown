

xyz.wagyourtail.jsmacros.client.api.classes.inventory.CommandBuilder
--------------------------------------------------------------------

Abstract
#### implements [Registrable](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Registrable.html)<[CommandBuilder](#)>

1.4.2

### Constructors

#### new CommandBuilder ()




#### Methods

[literalArg(name)](#literalArg-String-)
A


[booleanArg(name)](#booleanArg-String-)


[intArg(name)](#intArg-String-)


[intArg(name, min, max)](#intArg-String-int-int-)


[intRangeArg(name)](#intRangeArg-String-)


[longArg(name)](#longArg-String-)


[longArg(name, min, max)](#longArg-String-long-long-)


[floatRangeArg(name)](#floatRangeArg-String-)


[doubleArg(name)](#doubleArg-String-)


[doubleArg(name, min, max)](#doubleArg-String-double-double-)


[uuidArgType(name)](#uuidArgType-String-)


[greedyStringArg(name)](#greedyStringArg-String-)


[quotedStringArg(name)](#quotedStringArg-String-)


[wordArg(name)](#wordArg-String-)


[regexArgType(name, regex, flags)](#regexArgType-String-String-String-)


[textArgType(name)](#textArgType-String-)


[timeArg(name)](#timeArg-String-)


[identifierArg(name)](#identifierArg-String-)


[nbtArg(name)](#nbtArg-String-)


[nbtElementArg(name)](#nbtElementArg-String-)


[nbtCompoundArg(name)](#nbtCompoundArg-String-)


[colorArg(name)](#colorArg-String-)


[angleArg(name)](#angleArg-String-)


[itemArg(name)](#itemArg-String-)


[itemStackArg(name)](#itemStackArg-String-)


[itemPredicateArg(name)](#itemPredicateArg-String-)


[blockArg(name)](#blockArg-String-)


[blockStateArg(name)](#blockStateArg-String-)


[blockPredicateArg(name)](#blockPredicateArg-String-)


[blockPosArg(name)](#blockPosArg-String-)


[columnPosArg(name)](#columnPosArg-String-)


[dimensionArg(name)](#dimensionArg-String-)


[itemSlotArg(name)](#itemSlotArg-String-)


[particleArg(name)](#particleArg-String-)


[executes(callback)](#executes-MethodWrapper-)
A


[suggestMatching(suggestions)](#suggestMatching-String[]-)


[suggestMatching(suggestions)](#suggestMatching-Collection-)


[suggestIdentifier(suggestions)](#suggestIdentifier-String[]-)


[suggestIdentifier(suggestions)](#suggestIdentifier-Collection-)


[suggestBlockPositions(positions)](#suggestBlockPositions-BlockPosHelper[]-)


[suggestBlockPositions(positions)](#suggestBlockPositions-Collection-)


[suggestPositions(positions)](#suggestPositions-String[]-)


[suggestPositions(positions)](#suggestPositions-Collection-)


[suggest(callback)](#suggest-MethodWrapper-)


[or()](#or-)
A


[otherwise()](#otherwise-)


[or(argumentLevel)](#or-int-)
A


[otherwise(argLevel)](#otherwise-int-)


[register()](#register-)
A


[unregister()](#unregister-)
A



### Methods

#### .literalArg(name)

Abstract
| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .booleanArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .intArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .intArg(name, min, max)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| min | int |  |
| max | int |  |

##### Returns: [CommandBuilder](#)



#### .intRangeArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .longArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .longArg(name, min, max)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| min | long |  |
| max | long |  |

##### Returns: [CommandBuilder](#)



#### .floatRangeArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .doubleArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .doubleArg(name, min, max)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| min | double |  |
| max | double |  |

##### Returns: [CommandBuilder](#)



#### .uuidArgType(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .greedyStringArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .quotedStringArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .wordArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .regexArgType(name, regex, flags)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| regex | String |  |
| flags | String |  |

##### Returns: [CommandBuilder](#)



#### .textArgType(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .timeArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .identifierArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .nbtArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .nbtElementArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .nbtCompoundArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .colorArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .angleArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .itemArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .itemStackArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .itemPredicateArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .blockArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .blockStateArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .blockPredicateArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .blockPosArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .columnPosArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .dimensionArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .itemSlotArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .particleArg(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](#)



#### .executes(callback)

Abstract

it is recommended to use [FJsMacros#runScript(java.lang.String,xyz.wagyourtail.jsmacros.core.event.BaseEvent)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.html#runScript-String-BaseEvent-)
in the callback if you expect to actually do anything complicated with waits.

the [CommandContextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/CommandContextHelper.html) arg is an [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)
so you can pass it directly to [FJsMacros#runScript(java.lang.String,xyz.wagyourtail.jsmacros.core.event.BaseEvent)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.html#runScript-String-BaseEvent-).

make sure your callback returns a boolean success = true.

| Parameter | Type | Description |
|---|---|---|
| callback | MethodWrapper<CommandContextHelper, Object, Object, ?> |  |

##### Returns: [CommandBuilder](#)



#### .suggestMatching(suggestions)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| suggestions | String[] |  |

##### Returns: [CommandBuilder](#)



#### .suggestMatching(suggestions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestions | Collection<String> | the strings to match |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggestIdentifier(suggestions)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| suggestions | String[] |  |

##### Returns: [CommandBuilder](#)



#### .suggestIdentifier(suggestions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| suggestions | Collection<String> | the identifiers to match |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggestBlockPositions(positions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| positions | BlockPosHelper[] | the positions to suggest |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggestBlockPositions(positions)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| positions | Collection<BlockPosHelper> | the positions to suggest |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggestPositions(positions)

1.8.4

Positions are strings of the form "x y z" where x, y, and z are numbers or the default
minecraft selectors "~" and "^" followed by a number.

| Parameter | Type | Description |
|---|---|---|
| positions | String[] | the positions to suggest |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggestPositions(positions)

1.8.4

Positions are strings of the form "x y z" where x, y, and z are numbers or the default
minecraft selectors "~" and "^" followed by a number.

| Parameter | Type | Description |
|---|---|---|
| positions | Collection<String> | the positions to match |

##### Returns: [CommandBuilder](#)

self for chaining.



#### .suggest(callback)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| callback | MethodWrapper<CommandContextHelper, SuggestionsBuilderHelper, Object, ?> |  |

##### Returns: [CommandBuilder](#)



#### .or()

Abstract

##### Returns: [CommandBuilder](#)



#### .otherwise()

1.5.2

name overload for [CommandBuilder#or()](#or-) to work around language keyword restrictions


##### Returns: [CommandBuilder](#)



#### .or(argumentLevel)

Abstract
| Parameter | Type | Description |
|---|---|---|
| argumentLevel | int |  |

##### Returns: [CommandBuilder](#)



#### .otherwise(argLevel)

1.5.2

name overload for [CommandBuilder#or(int)](#or-int-) to work around language keyword restrictions

| Parameter | Type | Description |
|---|---|---|
| argLevel | int |  |

##### Returns: [CommandBuilder](#)



#### .register()

Abstract

##### Returns: [CommandBuilder](#)



#### .unregister()

Abstract

1.6.5
removes this command


##### Returns: [CommandBuilder](#)




