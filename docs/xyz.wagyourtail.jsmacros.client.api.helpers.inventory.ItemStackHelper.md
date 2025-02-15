
[CreativeItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html)

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.ItemStackHelper
---------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[ItemStack](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/ItemStack)>

### Constructors

#### new ItemStackHelper (id, count)

| Parameter | Type | Description |
|---|---|---|
| id | String |  |
| count | int |  |


#### new ItemStackHelper (i)

| Parameter | Type | Description |
|---|---|---|
| i | ItemStack |  |



#### Methods

[setDamage(damage)](#setDamage-int-)
D


[isDamageable()](#isDamageable-)


[isUnbreakable()](#isUnbreakable-)


[isEnchantable()](#isEnchantable-)


[isEnchanted()](#isEnchanted-)


[getEnchantments()](#getEnchantments-)


[getEnchantment(id)](#getEnchantment-String-)


[canBeApplied(enchantment)](#canBeApplied-EnchantmentHelper-)


[hasEnchantment(enchantment)](#hasEnchantment-EnchantmentHelper-)


[hasEnchantment(enchantment)](#hasEnchantment-String-)


[getPossibleEnchantments()](#getPossibleEnchantments-)


[getPossibleEnchantmentsFromTable()](#getPossibleEnchantmentsFromTable-)


[getLore()](#getLore-)


[getMaxDurability()](#getMaxDurability-)


[getDurability()](#getDurability-)


[getRepairCost()](#getRepairCost-)


[getDamage()](#getDamage-)


[getMaxDamage()](#getMaxDamage-)


[getAttackDamage()](#getAttackDamage-)


[getDefaultName()](#getDefaultName-)


[getName()](#getName-)


[getCount()](#getCount-)


[getMaxCount()](#getMaxCount-)


[getNBT()](#getNBT-)


[getCreativeTab()](#getCreativeTab-)


[getItemID()](#getItemID-)
D


[getItemId()](#getItemId-)


[getTags()](#getTags-)


[isFood()](#isFood-)


[isTool()](#isTool-)


[isWearable()](#isWearable-)


[isEmpty()](#isEmpty-)


[toString()](#toString-)


[equals(ish)](#equals-ItemStackHelper-)


[equals(is)](#equals-ItemStack-)


[isItemEqual(ish)](#isItemEqual-ItemStackHelper-)


[isItemEqual(is)](#isItemEqual-ItemStack-)


[isItemEqualIgnoreDamage(ish)](#isItemEqualIgnoreDamage-ItemStackHelper-)


[isItemEqualIgnoreDamage(is)](#isItemEqualIgnoreDamage-ItemStack-)


[isNBTEqual(ish)](#isNBTEqual-ItemStackHelper-)


[isNBTEqual(is)](#isNBTEqual-ItemStack-)


[isOnCooldown()](#isOnCooldown-)


[getCooldownProgress()](#getCooldownProgress-)


[isSuitableFor(block)](#isSuitableFor-BlockHelper-)


[isSuitableFor(block)](#isSuitableFor-BlockStateHelper-)


[getCreative()](#getCreative-)


[getItem()](#getItem-)


[copy()](#copy-)


[hasDestroyRestrictions()](#hasDestroyRestrictions-)


[hasPlaceRestrictions()](#hasPlaceRestrictions-)


[getDestroyRestrictions()](#getDestroyRestrictions-)


[getPlaceRestrictions()](#getPlaceRestrictions-)


[areEnchantmentsHidden()](#areEnchantmentsHidden-)


[areModifiersHidden()](#areModifiersHidden-)


[isUnbreakableHidden()](#isUnbreakableHidden-)


[isCanDestroyHidden()](#isCanDestroyHidden-)


[isCanPlaceHidden()](#isCanPlaceHidden-)


[isDyeHidden()](#isDyeHidden-)



### Methods

#### .setDamage(damage)

Deprecated

1.2.0

Sets the item damage value.
You should use [CreativeItemStackHelper#setDamage(int)](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html#setDamage-int-) instead.
You may want to use [ItemStackHelper#copy()](#copy-) first.

| Parameter | Type | Description |
|---|---|---|
| damage | int |  |

##### Returns: [ItemStackHelper](#)

self



#### .isDamageable()

1.2.0


##### Returns: boolean



#### .isUnbreakable()

1.8.4


##### Returns: boolean

`true` if this item is unbreakable, `false` otherwise.



#### .isEnchantable()

1.2.0


##### Returns: boolean



#### .isEnchanted()

1.8.4


##### Returns: boolean

`true` if the item is enchanted, `false` otherwise.



#### .getEnchantments()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)>

a list of all enchantments on this item.



#### .getEnchantment(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the enchantment to check for |

##### Returns: [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)

the enchantment instance, containing the level, or `null` if the item is not
enchanted with the specified enchantment.



#### .canBeApplied(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to check for |

##### Returns: boolean

`true` if the specified enchantment can be applied to this item, `false`
otherwise.



#### .hasEnchantment(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to check for |

##### Returns: boolean

`true` if the item is enchanted with the specified enchantment of the same
level, `false` otherwise.



#### .hasEnchantment(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | String | the id of the enchantment to check for |

##### Returns: boolean

`true` if the item is enchanted with the specified enchantment, `false`
otherwise.



#### .getPossibleEnchantments()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)>

a list of all enchantments that can be applied to this item.



#### .getPossibleEnchantmentsFromTable()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)>

a list of all enchantments that can be applied to this item through an enchanting table.



#### .getLore()

1.8.4

The returned list is a copy of the original list and can be modified without affecting the
original item. For editing the actual lore see
[CreativeItemStackHelper#addLore(java.lang.Object...)](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html#addLore-Object[]-).


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)>

a list of all lines of lore on this item.



#### .getMaxDurability()

1.8.4


##### Returns: int

the maximum durability of this item.



#### .getDurability()

1.8.4


##### Returns: int

the current durability of this item.



#### .getRepairCost()

1.8.4


##### Returns: int

the current repair cost of this item.



#### .getDamage()


##### Returns: int

the damage taken by this item.



#### .getMaxDamage()


##### Returns: int

the maximum damage this item can take.



#### .getAttackDamage()

1.8.4


##### Returns: double

the default attack damage of this item.



#### .getDefaultName()

1.2.0


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

was string before 1.6.5



#### .getName()


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

was string before 1.6.5



#### .getCount()


##### Returns: int

the item count this stack is holding.



#### .getMaxCount()


##### Returns: int

the maximum amount of items this stack can hold.



#### .getNBT()

1.1.6, was a [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) until 1.5.1


##### Returns: [NBTElementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/NBTElementHelper.html)



#### .getCreativeTab()

1.1.3


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)>



#### .getItemID()

Deprecated

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getItemId()

1.6.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getTags()

1.8.2


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .isFood()

1.8.2


##### Returns: boolean



#### .isTool()

1.8.2


##### Returns: boolean



#### .isWearable()

1.8.2


##### Returns: boolean



#### .isEmpty()


##### Returns: boolean



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .equals(ish)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| ish | ItemStackHelper |  |

##### Returns: boolean



#### .equals(is)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| is | ItemStack |  |

##### Returns: boolean



#### .isItemEqual(ish)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| ish | ItemStackHelper |  |

##### Returns: boolean



#### .isItemEqual(is)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| is | ItemStack |  |

##### Returns: boolean



#### .isItemEqualIgnoreDamage(ish)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| ish | ItemStackHelper |  |

##### Returns: boolean



#### .isItemEqualIgnoreDamage(is)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| is | ItemStack |  |

##### Returns: boolean



#### .isNBTEqual(ish)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| ish | ItemStackHelper |  |

##### Returns: boolean



#### .isNBTEqual(is)

1.1.3 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| is | ItemStack |  |

##### Returns: boolean



#### .isOnCooldown()

1.6.5


##### Returns: boolean



#### .getCooldownProgress()

1.6.5


##### Returns: float



#### .isSuitableFor(block)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| block | BlockHelper | the block to check |

##### Returns: boolean

`true` if the given block can be mined and drops when broken with this item,
`false` otherwise.



#### .isSuitableFor(block)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| block | BlockStateHelper | the block to check |

##### Returns: boolean

`true` if the given block can be mined and drops when broken with this item,
`false` otherwise.



#### .getCreative()

1.8.4

[CreativeItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html) adds methods for manipulating the item's nbt data.


##### Returns: [CreativeItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html)

a [CreativeItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/CreativeItemStackHelper.html) instance for this item.



#### .getItem()

1.8.4


##### Returns: [ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html)

the item this stack is made of.



#### .copy()

1.2.0


##### Returns: [ItemStackHelper](#)



#### .hasDestroyRestrictions()

1.8.4

This flag only affects players in adventure mode and makes sure only specified blocks can be
destroyed by this item.


##### Returns: boolean

`true` if the can destroy flag is set, `false` otherwise.



#### .hasPlaceRestrictions()

1.8.4

This flag only affects players in adventure mode and makes sure this item can only be placed
on specified blocks.


##### Returns: boolean

`true` if the can place on flag is set, `false` otherwise.



#### .getDestroyRestrictions()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BlockPredicateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/BlockPredicateHelper.html)>

a list of all filters set for the can destroy flag.



#### .getPlaceRestrictions()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BlockPredicateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/BlockPredicateHelper.html)>

a list of all filters set for the can place on flag.



#### .areEnchantmentsHidden()

1.8.4


##### Returns: boolean

`true` if enchantments are hidden, `false` otherwise.



#### .areModifiersHidden()

1.8.4


##### Returns: boolean

`true` if modifiers are hidden, `false` otherwise.



#### .isUnbreakableHidden()

1.8.4


##### Returns: boolean

`true` if the unbreakable flag is hidden, `false` otherwise.



#### .isCanDestroyHidden()

1.8.4


##### Returns: boolean

`true` if the can destroy flag is hidden, `false` otherwise.



#### .isCanPlaceHidden()

1.8.4


##### Returns: boolean

`true` if the can place flag is hidden, `false` otherwise.



#### .isDyeHidden()

1.8.4


##### Returns: boolean

`true` if dye of colored leather armor is hidden, `false` otherwise.




