

xyz.wagyourtail.jsmacros.core.library.impl.classes.Websocket
------------------------------------------------------------

#### 

### Constructors

#### new Websocket (address)

| Parameter | Type | Description |
|---|---|---|
| address | String |  |


#### new Websocket (address)

| Parameter | Type | Description |
|---|---|---|
| address | URL |  |



#### Fields

[onConnect](#onConnect)


[onTextMessage](#onTextMessage)


[onDisconnect](#onDisconnect)


[onError](#onError)


[onFrame](#onFrame)



#### Methods

[connect()](#connect-)


[getWs()](#getWs-)


[sendText(text)](#sendText-String-)


[close()](#close-)


[close(closeCode)](#close-int-)



### Fields

#### .onConnect

calls your method as a [Consumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Consumer.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>, [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .onTextMessage

calls your method as a [BiConsumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/BiConsumer.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .onDisconnect

calls your method as a [BiConsumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/BiConsumer.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [Websocket$Disconnected](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/Websocket.Disconnected.html)>


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [Websocket$Disconnected](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/Websocket.Disconnected.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .onError

calls your method as a [BiConsumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/BiConsumer.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [WebSocketException](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocketException.html)>


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [WebSocketException](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocketException.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



#### .onFrame

calls your method as a [BiConsumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/BiConsumer.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [WebSocketFrame](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocketFrame.html)>


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html), [WebSocketFrame](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocketFrame.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >



### Methods

#### .connect()

1.1.9


##### Returns: [Websocket](#)

self



#### .getWs()

1.1.9


##### Returns: [WebSocket](https://javadoc.io/doc/com.neovisionaries/nv-websocket-client/latest/index.html?com/neovisionaries/ws/client/WebSocket.html)



#### .sendText(text)

1.1.9

| Parameter | Type | Description |
|---|---|---|
| text | String |  |

##### Returns: [Websocket](#)

self



#### .close()

1.1.9


##### Returns: [Websocket](#)

self



#### .close(closeCode)

1.1.9

| Parameter | Type | Description |
|---|---|---|
| closeCode | int |  |

##### Returns: [Websocket](#)

self




