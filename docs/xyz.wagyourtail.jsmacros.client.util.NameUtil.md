

xyz.wagyourtail.jsmacros.client.util.NameUtil
---------------------------------------------

Final
#### 

1.8.4

#### Methods

[guessNameAndRoles(text)](#guessNameAndRoles-String-)
S



### Methods

#### .guessNameAndRoles(text)

Static

An approach to retrieve the name of a player from a chat message.

Iterate until <. If found, get the next valid name

Iterate until :. If found, get the last valid name

Iterate until >>. If found get the last valid name

Iterate until ->. If found get the last valid name (continue if empty)

The potential last name is the last value between [] or before >. It's used when the
sentence just continues.

There are some edge cases like "name > ", because it could also be "Guild >
name :". Since the last one is much more common, I will stay with this approach.

| Parameter | Type | Description |
|---|---|---|
| text | String |  |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of the name at index 0 and any potential roles as subsequent elements or an
empty list if the name could not be identified.




