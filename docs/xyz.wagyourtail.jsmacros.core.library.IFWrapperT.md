

xyz.wagyourtail.jsmacros.core.library.IFWrapper< T >
----------------------------------------------------

Interface
#### 

1.2.5, re-named from `consumer` in 1.3.2

[FunctionalInterface](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/FunctionalInterface.html) implementation for wrapping methods to match the language spec.
  
  

An instance of this class is passed to scripts as the `consumer` variable.
  
  

Javascript:
language spec requires that only one thread can hold an instance of the language at a time,
so this implementation uses a non-preemptive priority queue for the threads that call the resulting [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html).
  
  

JEP:
language spec requires everything to be on the same thread, on the java end, so all calls to [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)
call back to JEP's starting thread and wait for the call to complete.
  
  

Jython:
no limitations
  
  

LUA:
no limitations

#### Methods

[methodToJava(c)](#methodToJava-T-)


[methodToJavaAsync(c)](#methodToJavaAsync-T-)


[methodToJavaAsync(priority, c)](#methodToJavaAsync-int-T-)


[deferCurrentTask()](#deferCurrentTask-)


[deferCurrentTask(priorityAdjust)](#deferCurrentTask-int-)


[getCurrentPriority()](#getCurrentPriority-)


[stop()](#stop-)



### Methods

#### .methodToJava< A , B , R >(c)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| c | T |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< A , B , R , ? >

a new [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)



#### .methodToJavaAsync< A , B , R >(c)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| c | T |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< A , B , R , ? >

a new [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)



#### .methodToJavaAsync< A , B , R >(priority, c)

1.8.0

JS/JEP ONLY
allows you to set the position of the thread in the queue. you can use this for return value one's too...

| Parameter | Type | Description |
|---|---|---|
| priority | int |  |
| c | T |  |

##### Returns: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)< A , B , R , ? >



#### .deferCurrentTask()

1.4.0 [citation needed]

JS/JEP only, puts current task at end of queue.
use with caution, don't accidentally cause circular waiting.


##### Returns: void



#### .deferCurrentTask(priorityAdjust)

1.8.0

JS/JEP only, puts current task at end of queue.
use with caution, don't accidentally cause circular waiting.

| Parameter | Type | Description |
|---|---|---|
| priorityAdjust | int | the amount to adjust the priority by |

##### Returns: void



#### .getCurrentPriority()

1.8.0

JS/JEP only, get priority of current task.


##### Returns: int



#### .stop()

1.2.2

Close the current context


##### Returns: void




