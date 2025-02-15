

xyz.wagyourtail.jsmacros.core.language.BaseWrappedException< T >
----------------------------------------------------------------

#### 

### Constructors

#### new BaseWrappedException (exception, message, location, next)

| Parameter | Type | Description |
|---|---|---|
| exception | T |  |
| message | String |  |
| location | BaseWrappedException$SourceLocation |  |
| next | BaseWrappedException<?> |  |



#### Fields

[stackFrame](#stackFrame)
F


[location](#location)
F


[message](#message)
F


[next](#next)
F



#### Methods

[wrapHostElement(t, next)](#wrapHostElement-StackTraceElement-BaseWrappedException-)
S



### Fields

#### .stackFrame

Final

##### Type: T



#### .location

Final

##### Type: [BaseWrappedException$SourceLocation](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseWrappedException.SourceLocation.html)



#### .message

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .next

Final

##### Type: [BaseWrappedException](#)< ? >



### Methods

#### .wrapHostElement(t, next)

Static
| Parameter | Type | Description |
|---|---|---|
| t | StackTraceElement |  |
| next | BaseWrappedException<?> |  |

##### Returns: [BaseWrappedException](#)<[StackTraceElement](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/StackTraceElement.html)>




