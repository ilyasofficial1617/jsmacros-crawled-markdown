

xyz.wagyourtail.jsmacros.client.api.classes.inventory.HorseInventory
--------------------------------------------------------------------

#### extends [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)<[HorseScreen](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/screen/ingame/HorseScreen)>

1.8.4

#### Methods

[canBeSaddled()](#canBeSaddled-)


[isSaddled()](#isSaddled-)


[getSaddle()](#getSaddle-)


[hasArmorSlot()](#hasArmorSlot-)


[getArmor()](#getArmor-)


[hasChest()](#hasChest-)


[getInventorySize()](#getInventorySize-)


[getHorseInventory()](#getHorseInventory-)


[getHorse()](#getHorse-)


[toString()](#toString-)



### Methods

#### .canBeSaddled()

1.8.4


##### Returns: boolean

`true` if the horse can be saddled, `false` otherwise.



#### .isSaddled()

1.8.4


##### Returns: boolean

`true` if the horse is saddled, `false` otherwise.



#### .getSaddle()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the saddle item.



#### .hasArmorSlot()

1.8.4


##### Returns: boolean

`true` if the horse can equip armor, `false` otherwise.



#### .getArmor()

1.8.4


##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

the armor item.



#### .hasChest()

1.8.4


##### Returns: boolean

`true` if the horse has equipped a chest, `false` otherwise.



#### .getInventorySize()

1.8.4


##### Returns: int

the horse's inventory size.



#### .getHorseInventory()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>

a list of items in the horse's inventory.



#### .getHorse()

1.8.4


##### Returns: [AbstractHorseEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/specialized/passive/AbstractHorseEntityHelper.html)< ? >

the horse this inventory belongs to.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




