

xyz.wagyourtail.jsmacros.client.api.classes.inventory.AnvilInventory
--------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[AnvilScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/AnvilScreen)>

1.8.4

### Constructors

#### new AnvilInventory (inventory)

| Parameter | Type | Description |
|---|---|---|
| inventory | AnvilScreen |  |



#### Methods

[getName()](#getName-)


[setName(name)](#setName-String-)


[getLevelCost()](#getLevelCost-)


[getItemRepairCost()](#getItemRepairCost-)


[getMaximumLevelCost()](#getMaximumLevelCost-)


[getLeftInput()](#getLeftInput-)


[getRightInput()](#getRightInput-)


[getOutput()](#getOutput-)


[toString()](#toString-)



### Methods

#### .getName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the currently set name to be applied.



#### .setName(name)

1.8.4

The change will be applied once the item is taken out of the anvil.

| Parameter | Type | Description |
|---|---|---|
| name | String | the new item name |

##### Returns: [AnvilInventory](#)

self for chaining.



#### .getLevelCost()

1.8.4


##### Returns: int

the level cost to apply the changes.



#### .getItemRepairCost()

1.8.4


##### Returns: int

the amount of item needed to fully repair the item.



#### .getMaximumLevelCost()

1.8.4


##### Returns: int

the maximum default level cost.



#### .getLeftInput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the first input item.



#### .getRightInput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the second input item.



#### .getOutput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the expected output item.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




