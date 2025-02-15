

xyz.wagyourtail.jsmacros.client.api.classes.inventory.ChatHistoryManager
------------------------------------------------------------------------

#### 

1.6.0

### Constructors

#### new ChatHistoryManager (hud)

| Parameter | Type | Description |
|---|---|---|
| hud | ChatHud |  |



#### Methods

[getRecvLine(index)](#getRecvLine-int-)


[getRecvCount()](#getRecvCount-)


[getRecvLines()](#getRecvLines-)


[insertRecvText(index, line)](#insertRecvText-int-TextHelper-)


[insertRecvText(index, line, timeTicks)](#insertRecvText-int-TextHelper-int-)


[insertRecvText(index, line, timeTicks, await)](#insertRecvText-int-TextHelper-int-boolean-)


[removeRecvText(index)](#removeRecvText-int-)


[removeRecvText(index, await)](#removeRecvText-int-boolean-)


[removeRecvTextMatching(text)](#removeRecvTextMatching-TextHelper-)


[removeRecvTextMatching(text, await)](#removeRecvTextMatching-TextHelper-boolean-)


[removeRecvTextMatchingFilter(filter)](#removeRecvTextMatchingFilter-MethodWrapper-)


[removeRecvTextMatchingFilter(filter, await)](#removeRecvTextMatchingFilter-MethodWrapper-boolean-)


[refreshVisible()](#refreshVisible-)


[refreshVisible(await)](#refreshVisible-boolean-)


[clearRecv()](#clearRecv-)


[clearRecv(await)](#clearRecv-boolean-)


[getSent()](#getSent-)


[clearSent()](#clearSent-)


[clearSent(await)](#clearSent-boolean-)



### Methods

#### .getRecvLine(index)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: [ChatHudLineHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ChatHudLineHelper.html)



#### .getRecvCount()

1.8.4


##### Returns: int

the amount of messages in the chat history.



#### .getRecvLines()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ChatHudLineHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ChatHudLineHelper.html)>

all received messages in the chat history.



#### .insertRecvText(index, line)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| index | int |  |
| line | TextHelper |  |

##### Returns: void



#### .insertRecvText(index, line, timeTicks)

1.6.0

you should probably run [ChatHistoryManager#refreshVisible()](#refreshVisible-) after...

| Parameter | Type | Description |
|---|---|---|
| index | int |  |
| line | TextHelper |  |
| timeTicks | int |  |

##### Returns: void



#### .insertRecvText(index, line, timeTicks, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| index | int |  |
| line | TextHelper |  |
| timeTicks | int |  |
| await | boolean |  |

##### Returns: void



#### .removeRecvText(index)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: void



#### .removeRecvText(index, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| index | int |  |
| await | boolean |  |

##### Returns: void



#### .removeRecvTextMatching(text)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |

##### Returns: void



#### .removeRecvTextMatching(text, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |
| await | boolean |  |

##### Returns: void



#### .removeRecvTextMatchingFilter(filter)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| filter | MethodWrapper<ChatHudLineHelper, Object, Boolean, ?> |  |

##### Returns: void



#### .removeRecvTextMatchingFilter(filter, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| filter | MethodWrapper<ChatHudLineHelper, Object, Boolean, ?> |  |
| await | boolean |  |

##### Returns: void



#### .refreshVisible()

1.6.0

this will reset the view of visible messages


##### Returns: void



#### .refreshVisible(await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| await | boolean |  |

##### Returns: void



#### .clearRecv()

1.6.0


##### Returns: void



#### .clearRecv(await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| await | boolean |  |

##### Returns: void



#### .getSent()

1.6.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

direct reference to sent message history list. modifications will affect the list.



#### .clearSent()

1.6.0


##### Returns: void



#### .clearSent(await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| await | boolean |  |

##### Returns: void




