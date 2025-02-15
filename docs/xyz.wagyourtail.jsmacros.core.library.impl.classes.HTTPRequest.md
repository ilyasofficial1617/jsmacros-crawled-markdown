

xyz.wagyourtail.jsmacros.core.library.impl.classes.HTTPRequest
--------------------------------------------------------------

#### 

1.1.8

### Constructors

#### new HTTPRequest (url)

| Parameter | Type | Description |
|---|---|---|
| url | String |  |



#### Fields

[headers](#headers)


[conn](#conn)


[connectTimeout](1.9.2/)


[readTimeout](1.9.2/)



#### Methods

[addHeader(key, value)](#addHeader-String-String-)


[setConnectTimeout(timeout)](#setConnectTimeout-int-)


[setReadTimeout(timeout)](#setReadTimeout-int-)


[get()](#get-)


[post(data)](#post-String-)


[post(data)](#post-byte[]-)


[put(data)](#put-String-)


[put(data)](#put-byte[]-)


[send(method)](#send-String-)


[send(method, data)](#send-String-String-)


[send(method, data)](#send-String-byte[]-)



### Fields

#### .headers


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .conn


##### Type: [URL](https://docs.oracle.com/javase/8/docs/api/index.html?java/net/URL.html)



#### .connectTimeout


##### Type: int



#### .readTimeout


##### Type: int



### Methods

#### .addHeader(key, value)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| key | String |  |
| value | String |  |

##### Returns: [HTTPRequest](#)



#### .setConnectTimeout(timeout)

1.8.6

| Parameter | Type | Description |
|---|---|---|
| timeout | int |  |

##### Returns: [HTTPRequest](#)



#### .setReadTimeout(timeout)

1.8.6

| Parameter | Type | Description |
|---|---|---|
| timeout | int |  |

##### Returns: [HTTPRequest](#)



#### .get()

1.1.8


##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .post(data)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| data | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .post(data)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| data | byte[] |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .put(data)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| data | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .put(data)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| data | byte[] |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .send(method)

1.8.6

| Parameter | Type | Description |
|---|---|---|
| method | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .send(method, data)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| method | String |  |
| data | String |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)



#### .send(method, data)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| method | String |  |
| data | byte[] |  |

##### Returns: [HTTPRequest$Response](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/HTTPRequest.Response.html)




