

xyz.wagyourtail.jsmacros.core.event.impl.FiltererComposed
---------------------------------------------------------

#### implements [EventFilterer$Compound](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.Compound.html)

1.9.1

### Constructors

#### new FiltererComposed (initial)

| Parameter | Type | Description |
|---|---|---|
| initial | EventFilterer |  |



#### Methods

[canFilter(event)](#canFilter-String-)


[test(event)](#test-BaseEvent-)


[and(filterer)](#and-EventFilterer-)


[or(filterer)](#or-EventFilterer-)


[checkCyclicRef(base)](#checkCyclicRef-EventFilterer$Compound-)



### Methods

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



#### .and(filterer)

| Parameter | Type | Description |
|---|---|---|
| filterer | EventFilterer | the filterer to compose |

##### Returns: [FiltererComposed](#)

self for chaining



#### .or(filterer)

| Parameter | Type | Description |
|---|---|---|
| filterer | EventFilterer | the filterer to compose |

##### Returns: [FiltererComposed](#)

self for chaining



#### .checkCyclicRef(base)

| Parameter | Type | Description |
|---|---|---|
| base | EventFilterer$Compound |  |

##### Returns: void




