

xyz.wagyourtail.jsmacros.client.api.event.impl.player.EventDeath
----------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.2.7

### Constructors

#### new EventDeath ()




#### Fields

[deathPos](#deathPos)
F


[inventory](#inventory)
F



#### Methods

[respawn()](#respawn-)


[toString()](#toString-)



### Fields

#### .deathPos

Final

##### Type: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)



#### .inventory

Final

##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)>



### Methods

#### .respawn()

1.8.4

Respawns the player. Should be used with some delay, one tick should be enough.


##### Returns: void



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




