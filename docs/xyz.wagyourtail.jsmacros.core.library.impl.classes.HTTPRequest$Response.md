

xyz.wagyourtail.jsmacros.core.library.impl.classes.HTTPRequest$Response
-----------------------------------------------------------------------

Static
#### 

1.1.8

### Constructors

#### new HTTPRequest$Response (inputStream, responseCode, headers)

| Parameter | Type | Description |
|---|---|---|
| inputStream | InputStream |  |
| responseCode | int |  |
| headers | Map<String, List<String>> |  |



#### Fields

[headers](#headers)


[responseCode](1.9.2/)



#### Methods

[text()](#text-)


[json()](#json-)
D


[byteArray()](#byteArray-)



### Fields

#### .headers


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>>



#### .responseCode


##### Type: int



### Methods

#### .text()

1.1.8


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .json()

Deprecated

1.1.8

Don't use this. Parse [HTTPRequest$Response#text()](#text-) in the guest language


##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .byteArray()

1.2.2


##### Returns: byte []




