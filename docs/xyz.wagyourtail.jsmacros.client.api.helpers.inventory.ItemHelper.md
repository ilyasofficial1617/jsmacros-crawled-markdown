

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.ItemHelper
----------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Item](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/Item)>

1.8.4

### Constructors

#### new ItemHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | Item |  |



#### Methods

[getCreativeTab()](#getCreativeTab-)


[getGroupIcon()](#getGroupIcon-)


[canBeRepairedWith(stack)](#canBeRepairedWith-ItemStackHelper-)


[isSuitableFor(block)](#isSuitableFor-BlockHelper-)


[isSuitableFor(block)](#isSuitableFor-BlockStateHelper-)


[isBlockItem()](#isBlockItem-)


[getBlock()](#getBlock-)


[getMiningSpeedMultiplier(state)](#getMiningSpeedMultiplier-BlockStateHelper-)


[isDamageable()](#isDamageable-)


[hasRecipeRemainder()](#hasRecipeRemainder-)


[getRecipeRemainder()](#getRecipeRemainder-)


[getEnchantability()](#getEnchantability-)


[getName()](#getName-)


[getId()](#getId-)


[getMaxCount()](#getMaxCount-)


[getMaxDurability()](#getMaxDurability-)


[isFireproof()](#isFireproof-)


[isTool()](#isTool-)


[isWearable()](#isWearable-)


[isFood()](#isFood-)


[getFood()](#getFood-)


[canBeNested()](#canBeNested-)


[getDefaultStack()](#getDefaultStack-)


[getStackWithNbt(nbt)](#getStackWithNbt-String-)


[toString()](#toString-)



### Methods

#### .getCreativeTab()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)>

the name of this item's group or `"UNKNOWN"` if this item is not in a group.



#### .getGroupIcon()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

the item stack representing the group of this item or `null` if this item is
not in a group.



#### .canBeRepairedWith(stack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| stack | ItemStackHelper | the possible repair material |

##### Returns: boolean

`true` if the given item stack can be used to repair item stacks of this item,
`false` otherwise.



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



#### .isBlockItem()

1.8.4


##### Returns: boolean

`true` if the item has a block representation, `false` otherwise.



#### .getBlock()

1.8.4


##### Returns: [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)

the block representation of this item or `null` if this item has no
corresponding block.



#### .getMiningSpeedMultiplier(state)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| state | BlockStateHelper | the block state to check |

##### Returns: float

the mining speed of this item against the given block state, returns `1` by
default.



#### .isDamageable()

1.8.4


##### Returns: boolean

`true` if the item has durability, `false` otherwise.



#### .hasRecipeRemainder()

1.8.4


##### Returns: boolean

`true` if when crafter the item stack has a remainder, `false`
otherwise.



#### .getRecipeRemainder()

1.8.4


##### Returns: [ItemHelper](#)

the recipe remainder if it exists and `null` otherwise.



#### .getEnchantability()

1.8.4

With increased enchantability the change to get more and better enchantments increases.


##### Returns: int

the enchantability of this item, returns `0` by default.



#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of this item, translated to the current language.



#### .getId()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the identifier of this item.



#### .getMaxCount()

1.8.4


##### Returns: int

the maximum amount of items in a stack of this item.



#### .getMaxDurability()

1.8.4

The damage an item has taken is the opposite of the durability still left.


##### Returns: int

the maximum amount of damage this item can take.



#### .isFireproof()

1.8.4


##### Returns: boolean

`true` if this item is fireproof, `false` otherwise.



#### .isTool()

1.8.4


##### Returns: boolean

`true` if this item is a tool, `false` otherwise.



#### .isWearable()

1.8.4


##### Returns: boolean

`true` if this item can be worn in the armor slot, `false` otherwise.



#### .isFood()

1.8.4


##### Returns: boolean

`true` if this item is food, `false` otherwise.



#### .getFood()

1.8.4


##### Returns: [FoodComponentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/FoodComponentHelper.html)

the food component of this item or `null` if this item is not food.



#### .canBeNested()

1.8.4


##### Returns: boolean

`true` if this item can be nested, i.e. put into a bundle or shulker box,
`false` otherwise.



#### .getDefaultStack()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the default item stack of this item with a stack size of `1`.



#### .getStackWithNbt(nbt)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| nbt | String | the nbt data of the item stack |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the item stack of this item with a stack size of `1` and the given nbt.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




