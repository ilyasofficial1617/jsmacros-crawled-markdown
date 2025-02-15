

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.CreativeItemStackHelper
-----------------------------------------------------------------------------

#### extends [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

1.8.4

### Constructors

#### new CreativeItemStackHelper (itemStack)

| Parameter | Type | Description |
|---|---|---|
| itemStack | ItemStack |  |



#### Methods

[setDamage(damage)](#setDamage-int-)


[setDurability(durability)](#setDurability-int-)


[setCount(count)](#setCount-int-)


[setName(name)](#setName-String-)


[setName(name)](#setName-TextHelper-)


[addEnchantment(id, level)](#addEnchantment-String-int-)


[addEnchantment(enchantment)](#addEnchantment-EnchantmentHelper-)


[clearEnchantments()](#clearEnchantments-)


[removeEnchantment(enchantment)](#removeEnchantment-EnchantmentHelper-)


[removeEnchantment(id)](#removeEnchantment-String-)


[clearLore()](#clearLore-)


[setLore(lore)](#setLore-Object[]-)


[addLore(lore)](#addLore-Object[]-)


[setUnbreakable(unbreakable)](#setUnbreakable-boolean-)


[hideEnchantments(hide)](#hideEnchantments-boolean-)


[hideModifiers(hide)](#hideModifiers-boolean-)


[hideUnbreakable(hide)](#hideUnbreakable-boolean-)


[hideCanDestroy(hide)](#hideCanDestroy-boolean-)


[hideCanPlace(hide)](#hideCanPlace-boolean-)


[hideDye(hide)](#hideDye-boolean-)



### Methods

#### .setDamage(damage)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| damage | int | the damage the item should take |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setDurability(durability)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| durability | int | the new durability of this item |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setCount(count)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| count | int | the new count of the item |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setName(name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| name | String | the new name of the item |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setName(name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| name | TextHelper | the new name of the item |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .addEnchantment(id, level)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the enchantment |
| level | int | the level of the enchantment |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .addEnchantment(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to add |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .clearEnchantments()

1.8.4


##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .removeEnchantment(enchantment)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enchantment | EnchantmentHelper | the enchantment to remove |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .removeEnchantment(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the id of the enchantment to remove |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .clearLore()

1.8.4


##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setLore(lore)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| lore | Object[] | the new lore |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .addLore(lore)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| lore | Object[] | the lore to add |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .setUnbreakable(unbreakable)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| unbreakable | boolean | whether the item should be unbreakable or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideEnchantments(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide the enchantments or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideModifiers(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide attributes and modifiers or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideUnbreakable(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide the unbreakable flag or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideCanDestroy(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide the blocks this item can destroy or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideCanPlace(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide the blocks this item can be placed on or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.



#### .hideDye(hide)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hide | boolean | whether to hide the color of colored leather armor or not |

##### Returns: [CreativeItemStackHelper](#)

self for chaining.




