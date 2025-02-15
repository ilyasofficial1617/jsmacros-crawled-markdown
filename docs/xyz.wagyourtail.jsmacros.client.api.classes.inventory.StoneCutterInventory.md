

xyz.wagyourtail.jsmacros.client.api.classes.inventory.StoneCutterInventory
--------------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[StonecutterScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/StonecutterScreen)>

1.8.4

### Constructors

#### new StoneCutterInventory (inventory)

| Parameter | Type | Description |
|---|---|---|
| inventory | StonecutterScreen |  |



#### Methods

[getSelectedRecipeIndex()](#getSelectedRecipeIndex-)


[getOutput()](#getOutput-)


[selectRecipe(idx)](#selectRecipe-int-)


[getAvailableRecipeCount()](#getAvailableRecipeCount-)


[getRecipes()](#getRecipes-)


[canCraft()](#canCraft-)


[toString()](#toString-)



### Methods

#### .getSelectedRecipeIndex()

1.8.4


##### Returns: int

the selected recipe index.



#### .getOutput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the output item for the selected recipe.



#### .selectRecipe(idx)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| idx | int | the index to select |

##### Returns: [StoneCutterInventory](#)

self for chaining.



#### .getAvailableRecipeCount()

1.8.4


##### Returns: int

the amount of available recipes.



#### .getRecipes()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of all available recipe results in the form of item stacks.



#### .canCraft()

1.8.4


##### Returns: boolean

`true` if there is a selected recipe, `false` otherwise.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




