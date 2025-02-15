

xyz.wagyourtail.jsmacros.core.library.impl.FJsMacros
----------------------------------------------------

#### extends [PerExecLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLibrary.html)

Functions that interact directly with JsMacros or Events.

An instance of this class is passed to scripts as the `JsMacros` variable.

#### Methods

[getProfile()](#getProfile-)


[getConfig()](#getConfig-)


[getServiceManager()](#getServiceManager-)


[getOpenContexts()](#getOpenContexts-)


[runScript(file)](#runScript-String-)


[runScript(file, fakeEvent)](#runScript-String-BaseEvent-)


[runScript(file, fakeEvent, callback)](#runScript-String-BaseEvent-MethodWrapper-)


[runScript(language, script)](#runScript-String-String-)


[runScript(language, script, callback)](#runScript-String-String-MethodWrapper-)


[runScript(language, script, file, callback)](#runScript-String-String-String-MethodWrapper-)


[runScript(language, script, file, event, callback)](#runScript-String-String-String-BaseEvent-MethodWrapper-)


[wrapScriptRun(file)](#wrapScriptRun-String-)


[wrapScriptRun(language, script)](#wrapScriptRun-String-String-)


[wrapScriptRun(language, script, file)](#wrapScriptRun-String-String-String-)


[wrapScriptRunAsync(file)](#wrapScriptRunAsync-String-)


[wrapScriptRunAsync(language, script)](#wrapScriptRunAsync-String-String-)


[wrapScriptRunAsync(language, script, file)](#wrapScriptRunAsync-String-String-String-)


[open(path)](#open-String-)
D


[openUrl(url)](#openUrl-String-)
D


[on(event, callback)](#on-String-MethodWrapper-)


[on(event, joined, callback)](#on-String-boolean-MethodWrapper-)


[on(event, filterer, callback)](#on-String-EventFilterer-MethodWrapper-)


[on(event, filterer, joined, callback)](#on-String-EventFilterer-boolean-MethodWrapper-)


[once(event, callback)](#once-String-MethodWrapper-)


[once(event, joined, callback)](#once-String-boolean-MethodWrapper-)


[off(listener)](#off-IEventListener-)


[off(event, listener)](#off-String-IEventListener-)


[disableAllListeners(event)](#disableAllListeners-String-)


[disableAllListeners()](#disableAllListeners-)


[disableScriptListeners(event)](#disableScriptListeners-String-)


[disableScriptListeners()](#disableScriptListeners-)


[waitForEvent(event)](#waitForEvent-String-)


[waitForEvent(event, join)](#waitForEvent-String-boolean-)


[waitForEvent(event, filter)](#waitForEvent-String-MethodWrapper-)


[waitForEvent(event, join, filter)](#waitForEvent-String-boolean-MethodWrapper-)


[waitForEvent(event, filter, runBeforeWaiting)](#waitForEvent-String-MethodWrapper-MethodWrapper-)


[waitForEvent(event, join, filter, runBeforeWaiting)](#waitForEvent-String-boolean-MethodWrapper-MethodWrapper-)


[listeners(event)](#listeners-String-)


[createEventFilterer(event)](#createEventFilterer-String-)


[createComposedEventFilterer(initial)](#createComposedEventFilterer-EventFilterer-)


[createModulusEventFilterer(quotient)](#createModulusEventFilterer-int-)


[invertEventFilterer(base)](#invertEventFilterer-EventFilterer-)


[createCustomEvent(eventName)](#createCustomEvent-String-)


[assertEvent(event, type)](#assertEvent-BaseEvent-String-)



### Methods

#### .getProfile()


##### Returns: [BaseProfile](1.9.2/xyz/wagyourtail/jsmacros/core/config/BaseProfile.html)

the JsMacros profile class.



#### .getConfig()


##### Returns: [ConfigManager](1.9.2/xyz/wagyourtail/jsmacros/core/config/ConfigManager.html)

the JsMacros config management class.



#### .getServiceManager()

1.6.3

services are background scripts designed to run full time and are mainly noticed by their side effects.


##### Returns: [ServiceManager](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.html)

for managing services.



#### .getOpenContexts()

1.4.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BaseScriptContext](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseScriptContext.html)< ? >>

list of non-garbage-collected ScriptContext's



#### .runScript(file)

1.1.5

| Parameter | Type | Description |
|---|---|---|
| file | String |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .runScript(file, fakeEvent)

1.6.3

| Parameter | Type | Description |
|---|---|---|
| file | String |  |
| fakeEvent | BaseEvent | you probably actually want to pass an instance created by FJsMacros#createCustomEvent(java.lang.String) |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .runScript(file, fakeEvent, callback)

1.6.3 (1.1.5 - 1.6.3 didn't have fakeEvent)

runs a script with a eventCustom to be able to pass args

| Parameter | Type | Description |
|---|---|---|
| file | String |  |
| fakeEvent | BaseEvent |  |
| callback | MethodWrapper<Throwable, Object, Object, ?> |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >

container the script is running on.



#### .runScript(language, script)

1.2.4

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .runScript(language, script, callback)

1.2.4

Runs a string as a script.

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |
| callback | MethodWrapper<Throwable, Object, Object, ?> | calls your method as a Consumer<String> |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >

the [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html) the script is running on.



#### .runScript(language, script, file, callback)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |
| file | String |  |
| callback | MethodWrapper<Throwable, Object, Object, ?> |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .runScript(language, script, file, event, callback)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |
| file | String |  |
| event | BaseEvent |  |
| callback | MethodWrapper<Throwable, Object, Object, ?> |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .wrapScriptRun< T , U , R >(file)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| file | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .wrapScriptRun< T , U , R >(language, script)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .wrapScriptRun< T , U , R >(language, script, file)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |
| file | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .wrapScriptRunAsync< T , U , R >(file)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| file | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .wrapScriptRunAsync< T , U , R >(language, script)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .wrapScriptRunAsync< T , U , R >(language, script, file)

1.7.0

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| script | String |  |
| file | String |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< T , U , R , ? >



#### .open(path)

Deprecated

1.1.8

Opens a file with the default system program.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: void



#### .openUrl(url)

Deprecated

1.6.0

| Parameter | Type | Description |
|---|---|---|
| url | String |  |

##### Returns: void



#### .on(event, callback)

1.2.7

Creates a listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)



#### .on(event, joined, callback)

1.9.0

Creates a listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| joined | boolean |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)



#### .on(event, filterer, callback)

1.9.1

Creates a listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| filterer | EventFilterer |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)



#### .on(event, filterer, joined, callback)

1.9.1

Creates a listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| filterer | EventFilterer |  |
| joined | boolean |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)



#### .once(event, callback)

1.2.7

Creates a single-run listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)

the listener.



#### .once(event, joined, callback)

1.9.0

Creates a single-run listener for an event, this function can be more efficient that running a script file when used properly.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| joined | boolean |  |
| callback | MethodWrapper<BaseEvent, EventContainer<?>, Object, ?> | calls your method as a BiConsumer<BaseEvent, EventContainer> |

##### Returns: [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)

the listener.



#### .off(listener)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| listener | IEventListener |  |

##### Returns: boolean



#### .off(event, listener)

1.2.3

Removes a [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html) from an event.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| listener | IEventListener |  |

##### Returns: boolean



#### .disableAllListeners(event)

1.8.4

Will also disable all listeners for the given event, including JsMacros own event listeners.

| Parameter | Type | Description |
|---|---|---|
| event | String | the event to remove all listeners from |

##### Returns: void



#### .disableAllListeners()

1.8.4

Will also disable all listeners, including JsMacros own event listeners.


##### Returns: void



#### .disableScriptListeners(event)

1.8.4

Will only disable user created event listeners for the given event. This includes listeners
created from [FJsMacros#on(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,java.lang.Object,?>)](#on-String-MethodWrapper-), [FJsMacros#once(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,java.lang.Object,?>)](#once-String-MethodWrapper-),
[FJsMacros#waitForEvent(java.lang.String)](#waitForEvent-String-), [FJsMacros#waitForEvent(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper)](#waitForEvent-String-MethodWrapper-) and
[FJsMacros#waitForEvent(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,xyz.wagyourtail.jsmacros.core.MethodWrapper)](#waitForEvent-String-MethodWrapper-MethodWrapper-).

| Parameter | Type | Description |
|---|---|---|
| event | String | the event to remove all listeners from |

##### Returns: void



#### .disableScriptListeners()

1.8.4

Will only disable user created event listeners. This includes listeners created from
[FJsMacros#on(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,java.lang.Object,?>)](#on-String-MethodWrapper-), [FJsMacros#once(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,java.lang.Object,?>)](#once-String-MethodWrapper-),
[FJsMacros#waitForEvent(java.lang.String)](#waitForEvent-String-), [FJsMacros#waitForEvent(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper)](#waitForEvent-String-MethodWrapper-) and
[FJsMacros#waitForEvent(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,xyz.wagyourtail.jsmacros.core.MethodWrapper)](#waitForEvent-String-MethodWrapper-MethodWrapper-).


##### Returns: void



#### .waitForEvent(event)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| event | String | event to wait for |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >

a event and a new context if the event you're waiting for was joined, to leave it early.



#### .waitForEvent(event, join)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| event | String | event to wait for |
| join | boolean |  |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >

a event and a new context if the event you're waiting for was joined, to leave it early.



#### .waitForEvent(event, filter)

1.5.0 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| filter | MethodWrapper<BaseEvent, Object, Boolean, ?> |  |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >



#### .waitForEvent(event, join, filter)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| event | String |  |
| join | boolean |  |
| filter | MethodWrapper<BaseEvent, Object, Boolean, ?> |  |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >



#### .waitForEvent(event, filter, runBeforeWaiting)

1.5.0

waits for an event. if this thread is bound to an event already, this will release current lock.

| Parameter | Type | Description |
|---|---|---|
| event | String | event to wait for |
| filter | MethodWrapper<BaseEvent, Object, Boolean, ?> | filter the event until it has the proper values or whatever. |
| runBeforeWaiting | MethodWrapper<Object, Object, Object, ?> | runs as a Runnable, run before waiting, this is a thread-safety thing to prevent "interrupts" from going in between this and things like deferCurrentTask |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >

a event and a new context if the event you're waiting for was joined, to leave it early.



#### .waitForEvent(event, join, filter, runBeforeWaiting)

1.9.0

waits for an event. if this thread is bound to an event already, this will release current lock.

| Parameter | Type | Description |
|---|---|---|
| event | String | event to wait for |
| join | boolean |  |
| filter | MethodWrapper<BaseEvent, Object, Boolean, ?> | filter the event until it has the proper values or whatever. |
| runBeforeWaiting | MethodWrapper<Object, Object, Object, ?> | runs as a Runnable, run before waiting, this is a thread-safety thing to prevent "interrupts" from going in between this and things like deferCurrentTask |

##### Returns: [FJsMacros$EventAndContext](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.EventAndContext.html)< ? >

a event and a new context if the event you're waiting for was joined, to leave it early.



#### .listeners(event)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| event | String |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)>

a list of script-added listeners.



#### .createEventFilterer(event)

1.9.1

create an event filterer.  

this exists to reduce lag when listening to frequently triggered events.

| Parameter | Type | Description |
|---|---|---|
| event | String |  |

##### Returns: [EventFilterer](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.html)



#### .createComposedEventFilterer(initial)

1.9.1

create a composed event filterer.  

this filterer combines multiple filterers together with and/or logic.

| Parameter | Type | Description |
|---|---|---|
| initial | EventFilterer |  |

##### Returns: [FiltererComposed](1.9.2/xyz/wagyourtail/jsmacros/core/event/impl/FiltererComposed.html)



#### .createModulusEventFilterer(quotient)

1.9.1

create a modulus event filterer.  

this filterer only let every nth event pass through.

| Parameter | Type | Description |
|---|---|---|
| quotient | int |  |

##### Returns: [FiltererModulus](1.9.2/xyz/wagyourtail/jsmacros/core/event/impl/FiltererModulus.html)



#### .invertEventFilterer(base)

1.9.1

inverts the base filterer's result.  

this checks if the base is already inverted.  

e.g. `filterer == invert(invert(filterer))` would be `true`.

| Parameter | Type | Description |
|---|---|---|
| base | EventFilterer |  |

##### Returns: [EventFilterer](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventFilterer.html)



#### .createCustomEvent(eventName)

1.2.8

create a custom event object that can trigger a event. It's recommended to use
[EventCustom#registerEvent()](1.9.2/xyz/wagyourtail/jsmacros/core/event/impl/EventCustom.html#registerEvent-) to set up the event to be visible in the GUI.

| Parameter | Type | Description |
|---|---|---|
| eventName | String | name of the event. please don't use an existing one... your scripts might not like that. |

##### Returns: [EventCustom](1.9.2/xyz/wagyourtail/jsmacros/core/event/impl/EventCustom.html)



#### .assertEvent(event, type)

1.9.0

asserts if `event` is the correct type of event  

and convert `event` type to target type in ts  

example:

```
                 JsMacros.assertEvent(event, 'Service')
                 
```
| Parameter | Type | Description |
|---|---|---|
| event | BaseEvent | the event to assert |
| type | String | string of the event type |

##### Returns: void




