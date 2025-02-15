

xyz.wagyourtail.jsmacros.client.api.event.impl.inventory.EventSlotUpdate
------------------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.9.0

### Constructors

#### new EventSlotUpdate (screen, type, slot, oldStack, newStack)

| Parameter | Type | Description |
|---|---|---|
| screen | HandledScreen<?> |  |
| type | String |  |
| slot | int |  |
| oldStack | ItemStack |  |
| newStack | ItemStack |  |



#### Fields

[type](#type)
F


[slot](1.9.2/)
F


[oldStack](#oldStack)
F


[newStack](#newStack)
F



#### Methods

[getInventory()](#getInventory-)


[toString()](#toString-)



### Fields

#### .type

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .slot

Final

##### Type: int



#### .oldStack

Final

##### Type: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)



#### .newStack

Final

##### Type: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)



### Methods

#### .getInventory()


##### Returns: [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)< ? >

inventory associated with the event



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




