

xyz.wagyourtail.jsmacros.core.library.impl.FRequest
---------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.1.8

Functions for getting and using raw java classes, methods and functions.

An instance of this class is passed to scripts as the `Request` variable.

#### Methods

[create(url)](#create-String-)


[get(url)](#get-String-)


[get(url, headers)](#get-String-Map-)


[post(url, data)](#post-String-String-)


[post(url, data, headers)](#post-String-String-Map-)


[createWS(url)](#createWS-String-)


[createWS2(url)](#createWS2-String-)
D



### Methods

#### .create(url)

1.1.8

create a HTTPRequest handler to the specified URL

| Parameter | Type | Description |
|---|---|---|
| url | String |  |

##### Returns: [HTTPRequest](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.html)

Request Wrapper



#### .get(url)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| url | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .get(url, headers)

1.1.8

send a GET request to the specified URL.

| Parameter | Type | Description |
|---|---|---|
| url | String |  |
| headers | Map<String, String> |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)

Response Data



#### .post(url, data)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| url | String |  |
| data | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .post(url, data, headers)

1.1.8

send a POST request to the specified URL.

| Parameter | Type | Description |
|---|---|---|
| url | String |  |
| data | String |  |
| headers | Map<String, String> |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)

Response Data



#### .createWS(url)

1.2.7

Create a Websocket handler.

| Parameter | Type | Description |
|---|---|---|
| url | String |  |

##### Returns: [Websocket](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/Websocket.html)



#### .createWS2(url)

Deprecated

1.1.9

Create a Websocket handler.

| Parameter | Type | Description |
|---|---|---|
| url | String |  |

##### Returns: [Websocket](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/Websocket.html)




