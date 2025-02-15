

xyz.wagyourtail.jsmacros.client.api.classes.inventory.BrewingStandInventory
---------------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[BrewingStandScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/BrewingStandScreen)>

1.8.4

### Constructors

#### new BrewingStandInventory (inventory)

| Parameter | Type | Description |
|---|---|---|
| inventory | BrewingStandScreen |  |



#### Methods

[isBrewablePotion(potion)](#isBrewablePotion-ItemStackHelper-)


[isValidIngredient(ingredient)](#isValidIngredient-ItemStackHelper-)


[isValidRecipe(potion, ingredient)](#isValidRecipe-ItemStackHelper-ItemStackHelper-)


[getFuelCount()](#getFuelCount-)


[getMaxFuelUses()](#getMaxFuelUses-)


[canBrewCurrentInput()](#canBrewCurrentInput-)


[getBrewTime()](#getBrewTime-)


[getRemainingTicks()](#getRemainingTicks-)


[previewPotion(potion, ingredient)](#previewPotion-ItemStackHelper-ItemStackHelper-)


[previewPotions()](#previewPotions-)


[getIngredient()](#getIngredient-)


[getFuel()](#getFuel-)


[getFirstPotion()](#getFirstPotion-)


[getSecondPotion()](#getSecondPotion-)


[getThirdPotion()](#getThirdPotion-)


[getPotions()](#getPotions-)


[toString()](#toString-)



### Methods

#### .isBrewablePotion(potion)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| potion | ItemStackHelper | the potion to check |

##### Returns: boolean

`true` if the given potion is can be brewed, `false` otherwise.



#### .isValidIngredient(ingredient)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| ingredient | ItemStackHelper | the item to check |

##### Returns: boolean

`true` if the given item is a valid ingredient, `false` otherwise.



#### .isValidRecipe(potion, ingredient)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| potion | ItemStackHelper | the potion to check |
| ingredient | ItemStackHelper | the ingredient to check |

##### Returns: boolean

`true` if the given potion and ingredient can be brewed together, `false`
otherwise.



#### .getFuelCount()

1.8.4


##### Returns: int

the left fuel.



#### .getMaxFuelUses()

1.8.4

The maximum fuel count is a constant with the value 20.


##### Returns: int

the maximum fuel.



#### .canBrewCurrentInput()

1.8.4


##### Returns: boolean

`true` if the brewing stand can brew any of the held potions with the current
ingredient, `false` otherwise.



#### .getBrewTime()

1.8.4


##### Returns: int

the time the potions have been brewing.



#### .getRemainingTicks()

1.8.4


##### Returns: int

the remaining time the potions have to brew.



#### .previewPotion(potion, ingredient)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| potion | ItemStackHelper | the potion |
| ingredient | ItemStackHelper | the ingredient |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the resulting potion of the given potion and ingredient if it exists and the potion
itself otherwise.



#### .previewPotions()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of all resulting potions of the current input.



#### .getIngredient()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the ingredient.



#### .getFuel()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the fuel item.



#### .getFirstPotion()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the first potion.



#### .getSecondPotion()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the second potion.



#### .getThirdPotion()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the third potion.



#### .getPotions()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of the potions inside the brewing stand.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




