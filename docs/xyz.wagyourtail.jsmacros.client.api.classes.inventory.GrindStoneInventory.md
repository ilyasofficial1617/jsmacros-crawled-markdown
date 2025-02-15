

xyz.wagyourtail.jsmacros.client.api.classes.inventory.GrindStoneInventory
-------------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[GrindstoneScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/GrindstoneScreen)>

1.8.4

### Constructors

#### new GrindStoneInventory (inventory)

| Parameter | Type | Description |
|---|---|---|
| inventory | GrindstoneScreen |  |



#### Methods

[getTopInput()](#getTopInput-)


[getBottomInput()](#getBottomInput-)


[getOutput()](#getOutput-)


[simulateXp()](#simulateXp-)


[toString()](#toString-)



### Methods

#### .getTopInput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the upper item to disenchant.



#### .getBottomInput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the bottom item to disenchant.



#### .getOutput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the expected output item.



#### .simulateXp()

1.8.4

Returns the minimum amount of xp dropped when disenchanting the input items. To calculate the
maximum amount of xp, just multiply the return value by 2.


##### Returns: int

the minimum amount of xp the grindstone should return.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




