

xyz.wagyourtail.jsmacros.client.api.event.impl.EventKey
-------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.2.7

### Constructors

#### new EventKey (action, key, mods)

| Parameter | Type | Description |
|---|---|---|
| action | int |  |
| key | String |  |
| mods | String |  |



#### Fields

[action](1.9.2/)
F


[key](#key)
F


[mods](#mods)
F



#### Methods

[parse(key, scancode, action, mods)](#parse-int-int-int-int-)
S


[toString()](#toString-)


[getKeyModifiers(mods)](#getKeyModifiers-int-)
S


[getModInt(mods)](#getModInt-String-)
S



### Fields

#### .action

Final

##### Type: int



#### .key

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .mods

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .parse(key, scancode, action, mods)

Static
| Parameter | Type | Description |
|---|---|---|
| key | int |  |
| scancode | int |  |
| action | int |  |
| mods | int |  |

##### Returns: boolean



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getKeyModifiers(mods)

Static

turn an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html) for key modifiers into a Translation Key.

| Parameter | Type | Description |
|---|---|---|
| mods | int |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getModInt(mods)

Static

turn a Translation Key for modifiers into an [Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html).

| Parameter | Type | Description |
|---|---|---|
| mods | String |  |

##### Returns: int




