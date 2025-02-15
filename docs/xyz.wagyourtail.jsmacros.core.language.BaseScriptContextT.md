

xyz.wagyourtail.jsmacros.core.language.BaseScriptContext< T >
-------------------------------------------------------------

Abstract
#### 

1.4.0

### Constructors

#### new BaseScriptContext (event, file)

| Parameter | Type | Description |
|---|---|---|
| event | BaseEvent |  |
| file | File |  |



#### Fields

[startTime](1.9.2/)
F


[syncObject](#syncObject)
F


[triggeringEvent](#triggeringEvent)
F


[eventListeners](#eventListeners)
F


[hasMethodWrapperBeenInvoked](1.9.2/)



#### Methods

[getSyncObject()](#getSyncObject-)


[clearSyncObject()](#clearSyncObject-)


[shouldKeepAlive()](#shouldKeepAlive-)


[getBoundEvents()](#getBoundEvents-)


[bindEvent(th, event)](#bindEvent-Thread-EventContainer-)


[releaseBoundEventIfPresent(thread)](#releaseBoundEventIfPresent-Thread-)


[getContext()](#getContext-)


[getMainThread()](#getMainThread-)


[bindThread(t)](#bindThread-Thread-)


[unbindThread(t)](#unbindThread-Thread-)


[getBoundThreads()](#getBoundThreads-)


[setMainThread(t)](#setMainThread-Thread-)


[getTriggeringEvent()](#getTriggeringEvent-)


[setContext(context)](#setContext-T-)


[isContextClosed()](#isContextClosed-)


[closeContext()](#closeContext-)


[getFile()](#getFile-)


[getContainedFolder()](#getContainedFolder-)


[isMultiThreaded()](#isMultiThreaded-)
A


[wrapSleep(sleep)](#wrapSleep-BaseScriptContext$SleepRunnable-)



### Fields

#### .startTime

Final

##### Type: long



#### .syncObject

Final

##### Type: [WeakReference](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/ref/WeakReference.html)<[Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>



#### .triggeringEvent

Final

##### Type: [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)



#### .eventListeners

Final

##### Type: [WeakHashMap](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/WeakHashMap.html)<[IEventListener](1.9.2/xyz/wagyourtail/jsmacros/core/event/IEventListener.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .hasMethodWrapperBeenInvoked


##### Type: boolean



### Methods

#### .getSyncObject()

this object should only be weak referenced unless we want to prevent the context from closing when syncObject is cleared.


##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .clearSyncObject()


##### Returns: void



#### .shouldKeepAlive()


##### Returns: boolean



#### .getBoundEvents()

1.6.0


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html), [EventContainer](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)< ? >>



#### .bindEvent(th, event)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| th | Thread |  |
| event | EventContainer<BaseScriptContext<T>> |  |

##### Returns: void



#### .releaseBoundEventIfPresent(thread)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| thread | Thread |  |

##### Returns: boolean



#### .getContext()


##### Returns: T



#### .getMainThread()

1.5.0


##### Returns: [Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html)



#### .bindThread(t)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| t | Thread |  |

##### Returns: boolean

is a newly bound thread



#### .unbindThread(t)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| t | Thread |  |

##### Returns: void



#### .getBoundThreads()

1.6.0


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html)>



#### .setMainThread(t)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| t | Thread |  |

##### Returns: void



#### .getTriggeringEvent()

1.5.0


##### Returns: [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)



#### .setContext(context)

| Parameter | Type | Description |
|---|---|---|
| context | T |  |

##### Returns: void



#### .isContextClosed()


##### Returns: boolean



#### .closeContext()


##### Returns: void



#### .getFile()

1.6.0


##### Returns: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .getContainedFolder()

1.6.0


##### Returns: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .isMultiThreaded()

Abstract

##### Returns: boolean



#### .wrapSleep(sleep)

| Parameter | Type | Description |
|---|---|---|
| sleep | BaseScriptContext$SleepRunnable |  |

##### Returns: void




