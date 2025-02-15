

xyz.wagyourtail.jsmacros.core.library.impl.classes.WrappedScript< T ,  U ,  V >
-------------------------------------------------------------------------------

#### extends [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , V , [BaseScriptContext](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseScriptContext.html)< ? >>

### Constructors

#### new WrappedScript (f, \_async)

| Parameter | Type | Description |
|---|---|---|
| f | Function<BaseEvent, EventContainer<BaseScriptContext<?>>> |  |
| _async | boolean |  |



#### Fields

[f](#f)
F


[\_async](1.9.2/)
F



#### Methods

[accept(t)](#accept-T-)


[accept(t, u)](#accept-T-U-)


[apply(t)](#apply-T-)


[apply(t, u)](#apply-T-U-)


[test(t)](#test-T-)


[test(t, u)](#test-T-U-)


[run()](#run-)


[compare(o1, o2)](#compare-T-T-)


[get()](#get-)



### Fields

#### .f

Final

##### Type: [Function](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Function.html)<[BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html), [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)<[BaseScriptContext](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseScriptContext.html)< ? >>>



#### .\_async

Final

##### Type: boolean



### Methods

#### .accept(t)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |

##### Returns: void



#### .accept(t, u)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |
| u | U |  |

##### Returns: void



#### .apply(t)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |

##### Returns: V



#### .apply(t, u)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |
| u | U |  |

##### Returns: V



#### .test(t)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |

##### Returns: boolean



#### .test(t, u)

| Parameter | Type | Description |
|---|---|---|
| t | T |  |
| u | U |  |

##### Returns: boolean



#### .run()


##### Returns: void



#### .compare(o1, o2)

| Parameter | Type | Description |
|---|---|---|
| o1 | T |  |
| o2 | T |  |

##### Returns: int



#### .get()


##### Returns: V




