

xyz.wagyourtail.jsmacros.client.api.classes.inventory.EnchantInventory
----------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[EnchantmentScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/EnchantmentScreen)>

1.3.1

#### Methods

[getRequiredLevels()](#getRequiredLevels-)


[getEnchantments()](#getEnchantments-)


[getEnchantmentHelpers()](#getEnchantmentHelpers-)


[getEnchantmentIds()](#getEnchantmentIds-)


[getEnchantmentLevels()](#getEnchantmentLevels-)


[doEnchant(index)](#doEnchant-int-)


[getItemToEnchant()](#getItemToEnchant-)


[getLapis()](#getLapis-)


[toString()](#toString-)



### Methods

#### .getRequiredLevels()

1.3.1


##### Returns: int []

xp level required to do enchantments



#### .getEnchantments()

1.3.1


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)[]

list of enchantments text.



#### .getEnchantmentHelpers()

1.8.4


##### Returns: [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)[]

the visible enchantment for each level.



#### .getEnchantmentIds()

1.3.1


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

id for enchantments



#### .getEnchantmentLevels()

1.3.1


##### Returns: int []

level of enchantments



#### .doEnchant(index)

1.3.1

clicks the button to enchant.

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: boolean

success



#### .getItemToEnchant()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the item to be enchanted.



#### .getLapis()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the slot containing the lapis lazuli.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




