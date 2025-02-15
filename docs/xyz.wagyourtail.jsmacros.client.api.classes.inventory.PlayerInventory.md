

xyz.wagyourtail.jsmacros.client.api.classes.inventory.PlayerInventory
---------------------------------------------------------------------

#### extends [RecipeInventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/RecipeInventory.html)<[InventoryScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/InventoryScreen)>

1.8.4

#### Methods

[getInput(x, y)](#getInput-int-int-)


[isInHotbar(slot)](#isInHotbar-int-)


[getOffhand()](#getOffhand-)


[getHelmet()](#getHelmet-)


[getChestplate()](#getChestplate-)


[getLeggings()](#getLeggings-)


[getBoots()](#getBoots-)


[toString()](#toString-)



### Methods

#### .getInput(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the input from 0 to 1, going left to right |
| y | int | the y position of the input from 0 to 1, going top to bottom |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the input item at the given position of the crafting grid.



#### .isInHotbar(slot)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| slot | int | the slot to check |

##### Returns: boolean

`true` if the slot is in the hotbar or the offhand slot, `false`
otherwise.



#### .getOffhand()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the item in the offhand.



#### .getHelmet()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the equipped helmet item.



#### .getChestplate()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the equipped chestplate item.



#### .getLeggings()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the equipped leggings item.



#### .getBoots()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the equipped boots item.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




