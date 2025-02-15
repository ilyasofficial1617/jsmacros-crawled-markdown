

xyz.wagyourtail.jsmacros.client.api.classes.inventory.FurnaceInventory
----------------------------------------------------------------------

#### extends [RecipeInventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/RecipeInventory.html)<[AbstractFurnaceScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/AbstractFurnaceScreen)< ? >>

1.8.4

### Constructors

#### new FurnaceInventory (inventory)

| Parameter | Type | Description |
|---|---|---|
| inventory | AbstractFurnaceScreen<?> |  |



#### Methods

[getInput(x, y)](#getInput-int-int-)


[getSmeltedItem()](#getSmeltedItem-)


[getFuel()](#getFuel-)


[canUseAsFuel(stack)](#canUseAsFuel-ItemStackHelper-)


[isSmeltable(stack)](#isSmeltable-ItemStackHelper-)


[getFuelValues()](#getFuelValues-)


[getSmeltingProgress()](#getSmeltingProgress-)


[getTotalSmeltingTime()](#getTotalSmeltingTime-)


[getRemainingSmeltingTime()](#getRemainingSmeltingTime-)


[getRemainingFuelTime()](#getRemainingFuelTime-)


[getTotalFuelTime()](#getTotalFuelTime-)


[isBurning()](#isBurning-)


[toString()](#toString-)



### Methods

#### .getInput(x, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x position of the input, will always be 0 |
| y | int | the y position of the input, will always be 0 |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the currently smelting item.



#### .getSmeltedItem()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the currently smelting item.



#### .getFuel()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the fuel item.



#### .canUseAsFuel(stack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| stack | ItemStackHelper | the item to check |

##### Returns: boolean

`true` if the item is a valid fuel, `false` otherwise.



#### .isSmeltable(stack)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| stack | ItemStackHelper | the item to check |

##### Returns: boolean

`true` if the item can be smelted, `false` otherwise.



#### .getFuelValues()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)>

a map of all valid fuels and their burn times in ticks.



#### .getSmeltingProgress()

1.8.4

If the returned value equals [FurnaceInventory#getTotalSmeltingTime()](#getTotalSmeltingTime-) then the item is done smelting.


##### Returns: int

the current Smelting progress in ticks.



#### .getTotalSmeltingTime()

1.8.4


##### Returns: int

the total smelting time of a single input item in ticks.



#### .getRemainingSmeltingTime()

1.8.4


##### Returns: int

the remaining time of the smelting progress in ticks.



#### .getRemainingFuelTime()

1.8.4


##### Returns: int

the remaining fuel time in ticks.



#### .getTotalFuelTime()

1.8.4


##### Returns: int

the total fuel time of the current fuel item in ticks.



#### .isBurning()

1.8.4


##### Returns: boolean

`true` if the furnace is currently smelting an item, `false` otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




