

xyz.wagyourtail.jsmacros.client.api.helpers.inventory.RecipeHelper
------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[RecipeEntry](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/recipe/RecipeEntry)< ? >>

1.3.1

### Constructors

#### new RecipeHelper (base, syncId)

| Parameter | Type | Description |
|---|---|---|
| base | RecipeEntry<?> |  |
| syncId | int |  |



#### Methods

[getId()](#getId-)


[getIngredients()](#getIngredients-)


[getOutput()](#getOutput-)


[craft(craftAll)](#craft-boolean-)


[getGroup()](#getGroup-)


[hasRecipeRemainders()](#hasRecipeRemainders-)


[getRecipeRemainders()](#getRecipeRemainders-)


[getType()](#getType-)


[canCraft()](#canCraft-)


[canCraft(amount)](#canCraft-int-)


[getCraftableAmount()](#getCraftableAmount-)


[toString()](#toString-)



### Methods

#### .getId()

1.3.1


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getIngredients()

1.8.3

get ingredients list


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>>



#### .getOutput()

1.3.1


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)



#### .craft(craftAll)

1.3.1

| Parameter | Type | Description |
|---|---|---|
| craftAll | boolean |  |

##### Returns: [RecipeHelper](#)



#### .getGroup()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the type of this recipe.



#### .hasRecipeRemainders()

1.8.4

This will not account for the actual items used in the recipe, but only the default recipe
itself. Items with durability or with a lot of tags will probably not work correctly.


##### Returns: boolean

will return `true` if any of the default ingredients have a recipe remainder.



#### .getRecipeRemainders()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>>

a list of all possible recipe remainders.



#### .getType()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the type of this recipe.



#### .canCraft()

1.8.4


##### Returns: boolean

`true` if the recipe can be crafted with the current inventory, `false`
otherwise.



#### .canCraft(amount)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| amount | int | the amount of items to craft |

##### Returns: boolean

`true` if the given amount of items can be crafted with the current inventory,
`false` otherwise.



#### .getCraftableAmount()

1.8.4


##### Returns: int

how often the recipe can be crafted with the current player inventory.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




