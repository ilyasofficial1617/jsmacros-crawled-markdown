

xyz.wagyourtail.jsmacros.client.api.event.impl.inventory.EventClickSlot
-----------------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.6.4

event triggered when the user "clicks" a slot in an inventory

### Constructors

#### new EventClickSlot (screen, mode, button, slot)

| Parameter | Type | Description |
|---|---|---|
| screen | HandledScreen<?> |  |
| mode | int |  |
| button | int |  |
| slot | int |  |



#### Fields

[mode](1.9.2/)
F


[button](1.9.2/)
F


[slot](1.9.2/)
F



#### Methods

[getInventory()](#getInventory-)


[toString()](#toString-)



### Fields

#### .mode

Final

<https://wiki.vg/Protocol#Click_Window>


##### Type: int



#### .button

Final

##### Type: int



#### .slot

Final

##### Type: int



### Methods

#### .getInventory()


##### Returns: [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)< ? >

inventory associated with the event



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




