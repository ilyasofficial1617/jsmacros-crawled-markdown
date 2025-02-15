
[KeyListener](1.9.2/xyz/wagyourtail/jsmacros/client/listeners/KeyListener.html) [EventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/EventListener.html)

xyz.wagyourtail.jsmacros.core.event.BaseListener
------------------------------------------------

Abstract
#### implements [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)

This is for java-sided listeners, for creating listeners script sided directly use [IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html)

### Constructors

#### new BaseListener (trigger, runner)

| Parameter | Type | Description |
|---|---|---|
| trigger | ScriptTrigger |  |
| runner | Core |  |



#### Methods

[getRawTrigger()](#getRawTrigger-)


[runScript(event)](#runScript-BaseEvent-)


[joined()](#joined-)


[equals(o)](#equals-Object-)


[off()](#off-)


[toString()](#toString-)



### Methods

#### .getRawTrigger()


##### Returns: [ScriptTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/config/ScriptTrigger.html)



#### .runScript(event)

| Parameter | Type | Description |
|---|---|---|
| event | BaseEvent |  |

##### Returns: [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >



#### .joined()


##### Returns: boolean



#### .equals(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean



#### .off()


##### Returns: void



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




