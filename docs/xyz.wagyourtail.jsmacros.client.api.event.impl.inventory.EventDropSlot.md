

xyz.wagyourtail.jsmacros.client.api.event.impl.inventory.EventDropSlot
----------------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.6.4

event triggered when an item is dropped

### Constructors

#### new EventDropSlot (screen, slot, all)

| Parameter | Type | Description |
|---|---|---|
| screen | HandledScreen<?> |  |
| slot | int |  |
| all | boolean |  |



#### Fields

[slot](1.9.2/)
F


[all](1.9.2/)
F



#### Methods

[getInventory()](#getInventory-)


[toString()](#toString-)



### Fields

#### .slot

Final

##### Type: int



#### .all

Final

whether it's all or a single item being dropped


##### Type: boolean



### Methods

#### .getInventory()


##### Returns: [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)< ? >

inventory associated with the event



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




