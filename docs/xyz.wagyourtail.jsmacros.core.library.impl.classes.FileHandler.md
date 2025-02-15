

xyz.wagyourtail.jsmacros.core.library.impl.classes.FileHandler
--------------------------------------------------------------

#### 

1.1.8

### Constructors

#### new FileHandler (path)

| Parameter | Type | Description |
|---|---|---|
| path | String |  |


#### new FileHandler (path, charset)

| Parameter | Type | Description |
|---|---|---|
| path | String |  |
| charset | String |  |


#### new FileHandler (path, charset)

| Parameter | Type | Description |
|---|---|---|
| path | File |  |
| charset | String |  |


#### new FileHandler (path, charset)

| Parameter | Type | Description |
|---|---|---|
| path | String |  |
| charset | Charset |  |


#### new FileHandler (path)

| Parameter | Type | Description |
|---|---|---|
| path | File |  |


#### new FileHandler (path, charset)

| Parameter | Type | Description |
|---|---|---|
| path | File |  |
| charset | Charset |  |



#### Methods

[write(s)](#write-String-)


[write(b)](#write-byte[]-)


[read()](#read-)


[readBytes()](#readBytes-)


[readLines()](#readLines-)


[streamBytes()](#streamBytes-)


[append(s)](#append-String-)


[append(b)](#append-byte[]-)


[getFile()](#getFile-)


[toString()](#toString-)



### Methods

#### .write(s)

1.1.8

writes a string to the file. this is a destructive operation that replaces the file contents.

| Parameter | Type | Description |
|---|---|---|
| s | String |  |

##### Returns: [FileHandler](#)

self



#### .write(b)

1.1.8

writes a byte array to the file. this is a destructive operation that replaces the file contents.

| Parameter | Type | Description |
|---|---|---|
| b | byte[] |  |

##### Returns: [FileHandler](#)

self



#### .read()

1.1.8


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .readBytes()

1.2.6


##### Returns: byte []



#### .readLines()

1.8.4

get an iterator for the lines in the file.
please call [FileHandler$FileLineIterator#close()](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.FileLineIterator.html#close-) when you are done with the iterator to not leak resources.


##### Returns: [FileHandler$FileLineIterator](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.FileLineIterator.html)



#### .streamBytes()

1.8.4

get an input stream for the file.
please call [BufferedInputStream#close()](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/BufferedInputStream.html) when you are done with the stream to not leak resources.


##### Returns: [BufferedInputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/BufferedInputStream.html)



#### .append(s)

1.1.8

| Parameter | Type | Description |
|---|---|---|
| s | String |  |

##### Returns: [FileHandler](#)

self



#### .append(b)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| b | byte[] |  |

##### Returns: [FileHandler](#)

self



#### .getFile()


##### Returns: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




