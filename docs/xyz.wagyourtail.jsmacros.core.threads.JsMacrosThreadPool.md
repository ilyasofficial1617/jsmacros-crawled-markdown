

xyz.wagyourtail.jsmacros.core.threads.JsMacrosThreadPool
--------------------------------------------------------

#### 

### Constructors

#### new JsMacrosThreadPool ()



#### new JsMacrosThreadPool (maxFreeThreads)

| Parameter | Type | Description |
|---|---|---|
| maxFreeThreads | int |  |



#### Fields

[maxFreeThreads](1.9.2/)
F



#### Methods

[runTask(task)](#runTask-Runnable-)


[runTask(task, beforeRunTask)](#runTask-Runnable-Consumer-)



### Fields

#### .maxFreeThreads

Final

##### Type: int



### Methods

#### .runTask(task)

| Parameter | Type | Description |
|---|---|---|
| task | Runnable |  |

##### Returns: [Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html)



#### .runTask(task, beforeRunTask)

| Parameter | Type | Description |
|---|---|---|
| task | Runnable |  |
| beforeRunTask | Consumer<Thread> |  |

##### Returns: [Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html)




