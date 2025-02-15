

xyz.wagyourtail.jsmacros.client.api.library.impl.FUtils
-------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.8.4

#### Methods

[openUrl(url)](#openUrl-String-)


[openFile(path)](#openFile-String-)


[copyToClipboard(text)](#copyToClipboard-String-)


[getClipboard()](#getClipboard-)


[guessName(text)](#guessName-TextHelper-)


[guessName(text)](#guessName-String-)


[guessNameAndRoles(text)](#guessNameAndRoles-TextHelper-)


[guessNameAndRoles(text)](#guessNameAndRoles-String-)


[hashString(message)](#hashString-String-)


[hashString(message, algorithm)](#hashString-String-String-)


[hashString(message, algorithm, base64)](#hashString-String-String-Boolean-)


[encode(message)](#encode-String-)


[decode(message)](#decode-String-)


[requireNonNull(obj)](#requireNonNull-T-)


[requireNonNull(obj, message)](#requireNonNull-T-String-)



### Methods

#### .openUrl(url)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| url | String | the url to open |

##### Returns: void



#### .openFile(path)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | the path top open, relative the config folder |

##### Returns: void



#### .copyToClipboard(text)

1.8.4

Copies the text to the clipboard.

| Parameter | Type | Description |
|---|---|---|
| text | String | the text to copy |

##### Returns: void



#### .getClipboard()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the text from the clipboard.



#### .guessName(text)

1.8.4

Tries to guess the name of the sender of a given message. This is not guaranteed to work and
for specific servers it may be better to use regex instead.

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper | the text to check |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the sender or `null` if it couldn't be guessed.



#### .guessName(text)

1.8.4

Tries to guess the name of the sender of a given message. This is not guaranteed to work and
for specific servers it may be better to use regex instead.

| Parameter | Type | Description |
|---|---|---|
| text | String | the text to check |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the sender or `null` if it couldn't be guessed.



#### .guessNameAndRoles(text)

1.8.4

Tries to guess the name, as well as the titles and roles of the sender of the given message.
This is not guaranteed to work and for specific servers it may be better to use regex
instead.

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper | the text to check |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of names, titles and roles of the sender or an empty list if it couldn't be
guessed.



#### .guessNameAndRoles(text)

1.8.4

Tries to guess the name, as well as the titles and roles of the sender of the given message.
This is not guaranteed to work and for specific servers it may be better to use regex
instead.

| Parameter | Type | Description |
|---|---|---|
| text | String | the text to check |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of names, titles and roles of the sender or an empty list if it couldn't be
guessed.



#### .hashString(message)

1.8.4

Hashes the given string with sha-256.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to hash |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the hashed message.



#### .hashString(message, algorithm)

1.8.4

Hashes the given string with the selected algorithm.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to hash |
| algorithm | String | sha1 | sha256 | sha384 | sha512 | md2 | md5 |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the hashed message (Hex)



#### .hashString(message, algorithm, base64)

1.9.1

Hashes the given string with the selected algorithm.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to hash |
| algorithm | String | sha1 | sha256 | sha384 | sha512 | md2 | md5 |
| base64 | Boolean | encode the result in base64 |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the hashed message (Hex or Base64)



#### .encode(message)

1.8.4

Encodes the given string with Base64.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to encode |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the encoded message.



#### .decode(message)

1.8.4

Decodes the given string with Base64.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to decode |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the decoded message.



#### .requireNonNull< T >(obj)

1.9.1

Checks that the specified object reference is not `null`.

| Parameter | Type | Description |
|---|---|---|
| obj | T | the object reference to check for nullity |

##### Returns: T

`obj` if not `null`



#### .requireNonNull< T >(obj, message)

1.9.1

Checks that the specified object reference is not `null` and
throws a customized [NullPointerException](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/NullPointerException.html) if it is.

| Parameter | Type | Description |
|---|---|---|
| obj | T | the object reference to check for nullity |
| message | String | detail message to be used in the event that a 
                                        NullPointerException is thrown |

##### Returns: T

`obj` if not `null`




