

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.EnchantmentHelper
-----------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Enchantment](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/enchantment/Enchantment)>

1.8.4

### Constructors

#### new EnchantmentHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | Enchantment |  |


#### new EnchantmentHelper (base, level)

| Parameter | Type | Description |
|---|---|---|
| base | Enchantment |  |
| level | int |  |


#### new EnchantmentHelper (enchantment)

| Parameter | Type | Description |
|---|---|---|
| enchantment | String |  |



#### Methods

[getLevel()](#getLevel-)


[getMinLevel()](#getMinLevel-)


[getMaxLevel()](#getMaxLevel-)


[getLevelName(level)](#getLevelName-int-)


[getRomanLevelName()](#getRomanLevelName-)


[getRomanLevelName(level)](#getRomanLevelName-int-)


[getName()](#getName-)


[getId()](#getId-)


[getConflictingEnchantments()](#getConflictingEnchantments-)


[getConflictingEnchantments(ignoreType)](#getConflictingEnchantments-boolean-)


[getCompatibleEnchantments()](#getCompatibleEnchantments-)


[getCompatibleEnchantments(ignoreType)](#getCompatibleEnchantments-boolean-)


[getTargetType()](#getTargetType-)


[getWeight()](#getWeight-)


[isCursed()](#isCursed-)


[isTreasure()](#isTreasure-)


[canBeApplied(item)](#canBeApplied-ItemHelper-)


[canBeApplied(item)](#canBeApplied-ItemStackHelper-)


[getAcceptableItems()](#getAcceptableItems-)


[isCompatible(enchantment)](#isCompatible-String-)


[isCompatible(enchantment)](#isCompatible-EnchantmentHelper-)


[conflictsWith(enchantment)](#conflictsWith-String-)


[conflictsWith(enchantment)](#conflictsWith-EnchantmentHelper-)


[toString()](#toString-)


[equals(o)](#equals-Object-)


[hashCode()](#hashCode-)



### Methods

#### .getLevel()

1.8.4


##### Returns: int

the level of this enchantment.



#### .getMinLevel()

1.8.4


##### Returns: int

the minimum possible level of this enchantment that one can get in vanilla.



#### .getMaxLevel()

1.8.4


##### Returns: int

the maximum possible level of this enchantment that one can get in vanilla.



#### .getLevelName(level)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| level | int | the level for the name |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the translated name of this enchantment for the given level.



#### .getRomanLevelName()

1.8.4

Because roman numerals only support positive integers in the range of 1 to 3999, this method
will return the arabic numeral for any given level outside that range.


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the translated name of this enchantment for the given level in roman numerals.



#### .getRomanLevelName(level)

1.8.4

Because roman numerals only support positive integers in the range of 1 to 3999, this method
will return the arabic numeral for any given level outside that range.

| Parameter | Type | Description |
|---|---|---|
| level | int | the level for the name |

##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

the translated name of this enchantment for the given level in roman numerals.



#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of this enchantment.



#### .getId()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the id of this enchantment.



#### .getConflictingEnchantments()

1.8.4

Only accounts for enchantments of the same target type.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](#)>

a list of all enchantments that conflict with this one.



#### .getConflictingEnchantments(ignoreType)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| ignoreType | boolean | whether to check only enchantments that can be applied to the same target
                                           type. |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](#)>

a list of all enchantments that conflict with this one.



#### .getCompatibleEnchantments()

1.8.4

Only accounts for enchantments of the same target type.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](#)>

a list of all enchantments that can be combined with this one.



#### .getCompatibleEnchantments(ignoreType)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| ignoreType | boolean | whether to check only enchantments that can be applied to the same target
                                           type. |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](#)>

a list of all enchantments that can be combined with this one.



#### .getTargetType()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the type of item this enchantment is compatible with.



#### .getWeight()

1.8.4

The weight of an enchantment is bound to its rarity. The higher the weight, the more likely
it is to be chosen.


##### Returns: int

the relative probability of this enchantment being applied to an enchanted item
through the enchanting table or a loot table.



#### .isCursed()

1.8.4

Curses are enchantments that can't be removed from the item they were applied to. They
usually only have one possible level and can't be upgraded. When combining items with curses
on them, they are transferred like any other enchantment. They can't be obtained through
enchantment tables, but rather from loot chests, fishing or trading with villagers.


##### Returns: boolean

`true` if this enchantment is a curse, `false` otherwise.



#### .isTreasure()

1.8.4

Treasures are enchantments that can't be obtained through enchantment tables, but rather from
loot chests, fishing or trading with villagers.


##### Returns: boolean

`true` if this enchantment is a treasure, `false` otherwise.



#### .canBeApplied(item)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| item | ItemHelper | the item to check |

##### Returns: boolean

`true` if this enchantment can be applied to the given item type, `false`
otherwise.



#### .canBeApplied(item)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| item | ItemStackHelper | the item to check |

##### Returns: boolean

`true` if this enchantment can be applied to the given item, `false`
otherwise.



#### .getAcceptableItems()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html)>

a list of all acceptable item ids for this enchantment.



#### .isCompatible(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | String | the enchantment to check |

##### Returns: boolean

`true` if this enchantment is compatible with the given enchantment,
`false` otherwise.



#### .isCompatible(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to check |

##### Returns: boolean

`true` if this enchantment is compatible with the given enchantment,
`false` otherwise.



#### .conflictsWith(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | String | the enchantment to check |

##### Returns: boolean

`true` if this enchantment conflicts with the given enchantment, `false`
otherwise.



#### .conflictsWith(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to check |

##### Returns: boolean

`true` if this enchantment conflicts with the given enchantment, `false`
otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .hashCode()


##### Returns: int




