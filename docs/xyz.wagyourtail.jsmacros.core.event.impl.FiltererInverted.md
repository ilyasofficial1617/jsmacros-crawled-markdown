

xyz.wagyourtail.jsmacros.core.event.impl.FiltererInverted
---------------------------------------------------------

#### implements [EventFilterer$Compound](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.Compound.html)

1.9.1

#### Fields

[base](#base)
F



#### Methods

[invert(base)](#invert-EventFilterer-)
S


[canFilter(event)](#canFilter-String-)


[test(event)](#test-BaseEvent-)


[checkCyclicRef(base)](#checkCyclicRef-EventFilterer$Compound-)



### Fields

#### .base

Final

##### Type: [EventFilterer](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.html)



### Methods

#### .invert(base)

Static
| Parameter | Type | Description |
|---|---|---|
| base | EventFilterer |  |

##### Returns: [EventFilterer](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.html)



#### .canFilter(event)

| Parameter | Type | Description |
|---|---|---|
| event | String |  |

##### Returns: boolean



#### .test(event)

| Parameter | Type | Description |
|---|---|---|
| event | BaseEvent |  |

##### Returns: boolean



#### .checkCyclicRef(base)

| Parameter | Type | Description |
|---|---|---|
| base | EventFilterer$Compound |  |

##### Returns: void




