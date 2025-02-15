

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.TradeOfferHelper
-------------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[TradeOffer](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/village/TradeOffer)>

### Constructors

#### new TradeOfferHelper (base, index, inv)

| Parameter | Type | Description |
|---|---|---|
| base | TradeOffer |  |
| index | int |  |
| inv | VillagerInventory |  |



#### Methods

[getInput()](#getInput-)


[getLeftInput()](#getLeftInput-)


[getRightInput()](#getRightInput-)


[getOutput()](#getOutput-)


[getIndex()](#getIndex-)


[select()](#select-)


[isAvailable()](#isAvailable-)


[getNBT()](#getNBT-)


[getUses()](#getUses-)


[getMaxUses()](#getMaxUses-)


[shouldRewardPlayerExperience()](#shouldRewardPlayerExperience-)


[getExperience()](#getExperience-)


[getCurrentPriceAdjustment()](#getCurrentPriceAdjustment-)


[getOriginalFirstInput()](#getOriginalFirstInput-)


[getOriginalPrice()](#getOriginalPrice-)


[getAdjustedPrice()](#getAdjustedPrice-)


[getSpecialPrice()](#getSpecialPrice-)


[getPriceMultiplier()](#getPriceMultiplier-)


[getDemandBonus()](#getDemandBonus-)


[toString()](#toString-)



### Methods

#### .getInput()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

list of input items required



#### .getLeftInput()

1.8.4

The returned item uses the adjusted price, in form of its stack size and will be empty
[ItemStackHelper#isEmpty()](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html#isEmpty-) if the first input doesn't exist.


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the first input item.



#### .getRightInput()

1.8.4

The returned item uses the adjusted price, in form of its stack size and will be empty
[ItemStackHelper#isEmpty()](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html#isEmpty-) if the first input doesn't exist.


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the second input item.



#### .getOutput()


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

output item that will be received



#### .getIndex()

1.8.4


##### Returns: int

the index if this trade in the given villager inventory.



#### .select()

select trade offer on screen


##### Returns: [TradeOfferHelper](#)



#### .isAvailable()


##### Returns: boolean



#### .getNBT()


##### Returns: [NBTElementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/NBTElementHelper.html)< ? >

trade offer as nbt tag



#### .getUses()


##### Returns: int

current number of uses



#### .getMaxUses()


##### Returns: int

max uses before it locks



#### .shouldRewardPlayerExperience()

1.8.4


##### Returns: boolean

`true` if after a successful trade xp will be summoned, `false`
otherwise.



#### .getExperience()


##### Returns: int

experience gained for trade



#### .getCurrentPriceAdjustment()


##### Returns: int

current price adjustment, negative is discount.



#### .getOriginalFirstInput()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the original priced item without any adjustments due to rewards or demand.



#### .getOriginalPrice()

1.8.4


##### Returns: int

the original price of the item without any adjustments due to rewards or demand.



#### .getAdjustedPrice()

1.8.4


##### Returns: int

the adjusted price of the item.



#### .getSpecialPrice()

1.8.4

A negative value is a discount and means that the player has a good reputation with the
villager, while a positive value is a premium. Hero of the village will always affect and
reduce this value.


##### Returns: int

the special price multiplier, which affects the price of the item depending on the
player's reputation with the villager.



#### .getPriceMultiplier()

1.8.4

A higher price multiplier means that the price of these trades can vary much more than normal
ones. The default value is 0.05 and 0.2 for armor and tools.


##### Returns: float

the price multiplier, which is only depended on the type of trade.



#### .getDemandBonus()

1.8.4

The demand bonus is globally applied to all trades of this type for all villagers and
players. It is used to increase the price of trades that are in high demand. The demand is
only calculated and updated on restock. Note that a villager can always restock, even if no
items were traded with him. Updating the demand is done with the following formula:

```
 demand = demand + 2 * uses - maxUses 
```

Thus trading only half of the max uses will not increase the demand.
The demand is also capped at 0, so it can not decrease the price.


##### Returns: int

the demand bonus for this trade.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




