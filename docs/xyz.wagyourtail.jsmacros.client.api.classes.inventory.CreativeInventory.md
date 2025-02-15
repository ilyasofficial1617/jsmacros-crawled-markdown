

xyz.wagyourtail.jsmacros.client.api.classes.inventory.CreativeInventory
-----------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[CreativeInventoryScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/CreativeInventoryScreen)>

1.8.4

#### Methods

[scroll(amount)](#scroll-double-)


[scrollTo(position)](#scrollTo-double-)


[getShownItems()](#getShownItems-)


[search(search)](#search-String-)


[selectSearch()](#selectSearch-)


[selectInventory()](#selectInventory-)


[selectHotbar()](#selectHotbar-)


[selectTab(tabName)](#selectTab-String-)


[getTabNames()](#getTabNames-)


[getTabTexts()](#getTabTexts-)


[destroyHeldItem()](#destroyHeldItem-)


[destroyAllItems()](#destroyAllItems-)


[setCursorStack(stack)](#setCursorStack-ItemStackHelper-)


[setStack(slot, stack)](#setStack-int-ItemStackHelper-)


[saveHotbar(index)](#saveHotbar-int-)


[restoreHotbar(index)](#restoreHotbar-int-)


[getSavedHotbar(index)](#getSavedHotbar-int-)


[isInHotbar(slot)](#isInHotbar-int-)


[getOffhand()](#getOffhand-)


[getHelmet()](#getHelmet-)


[getChestplate()](#getChestplate-)


[getLeggings()](#getLeggings-)


[getBoots()](#getBoots-)


[toString()](#toString-)



### Methods

#### .scroll(amount)

1.8.4

The total scroll value is always clamp between 0 and 1.

| Parameter | Type | Description |
|---|---|---|
| amount | double | the amount to scroll by, between -1 and 1 |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .scrollTo(position)

1.8.4

The total scroll value is always clamp between 0 and 1.

| Parameter | Type | Description |
|---|---|---|
| position | double | the position to scroll to, between 0 and 1 |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .getShownItems()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of all shown items.



#### .search(search)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| search | String | the string to search for |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .selectSearch()

1.8.4

Select the search tab.


##### Returns: [CreativeInventory](#)

self for chaining.



#### .selectInventory()

1.8.4

Select the inventory tab.


##### Returns: [CreativeInventory](#)

self for chaining.



#### .selectHotbar()

1.8.4

Select the tab where the hotbars are stored.


##### Returns: [CreativeInventory](#)

self for chaining.



#### .selectTab(tabName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| tabName | String | the name of the tab to select |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .getTabNames()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getTabTexts()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)>



#### .destroyHeldItem()

1.8.4

Destroys the currently held item.


##### Returns: [CreativeInventory](#)

self for chaining.



#### .destroyAllItems()

1.8.4

Destroys all items in the player's inventory.


##### Returns: [CreativeInventory](#)

self for chaining.



#### .setCursorStack(stack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| stack | ItemStackHelper | the item stack to drag |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .setStack(slot, stack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| slot | int | the slot to insert the item into |
| stack | ItemStackHelper | the item stack to insert |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .saveHotbar(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to save the hotbar to, from 0 to 8 |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .restoreHotbar(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to save the hotbar to, from 0 to 8 |

##### Returns: [CreativeInventory](#)

self for chaining.



#### .getSavedHotbar(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to save the hotbar to, from 0 to 8 |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of all items in the saved hotbar.



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




