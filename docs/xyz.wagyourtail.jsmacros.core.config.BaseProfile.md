
[Profile](1.9.2/xyz/wagyourtail/jsmacros/client/config/Profile.html)

xyz.wagyourtail.jsmacros.core.config.BaseProfile
------------------------------------------------

Abstract
#### 

1.2.7

### Constructors

#### new BaseProfile (runner, logger)

| Parameter | Type | Description |
|---|---|---|
| runner | Core |  |
| logger | Logger |  |



#### Fields

[LOGGER](#LOGGER)
F


[joinedThreadStack](#joinedThreadStack)
F


[events](#events)
F


[profileName](#profileName)



#### Methods

[logError(ex)](#logError-Throwable-)
A


[getRegistry()](#getRegistry-)
D


[checkJoinedThreadStack()](#checkJoinedThreadStack-)
A


[loadOrCreateProfile(profileName)](#loadOrCreateProfile-String-)


[saveProfile()](#saveProfile-)


[triggerEvent(event)](#triggerEvent-BaseEvent-)


[init(defaultProfile)](#init-String-)


[getCurrentProfileName()](#getCurrentProfileName-)


[renameCurrentProfile(profile)](#renameCurrentProfile-String-)



### Fields

#### .LOGGER

Final

##### Type: [Logger](https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.30/index.html?org/slf4j/Logger.html)



#### .joinedThreadStack

Final

##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Thread.html)>



#### .events

Final

##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .profileName


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .logError(ex)

Abstract
| Parameter | Type | Description |
|---|---|---|
| ex | Throwable |  |

##### Returns: void



#### .getRegistry()

Deprecated

1.1.2 [citation needed]


##### Returns: [BaseEventRegistry](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEventRegistry.html)



#### .checkJoinedThreadStack()

Abstract

1.6.0


##### Returns: boolean



#### .loadOrCreateProfile(profileName)

1.1.2 [citation needed]

| Parameter | Type | Description |
|---|---|---|
| profileName | String |  |

##### Returns: void



#### .saveProfile()

1.0.8 [citation needed]


##### Returns: void



#### .triggerEvent(event)

1.2.7

| Parameter | Type | Description |
|---|---|---|
| event | BaseEvent |  |

##### Returns: void



#### .init(defaultProfile)

| Parameter | Type | Description |
|---|---|---|
| defaultProfile | String |  |

##### Returns: void



#### .getCurrentProfileName()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .renameCurrentProfile(profile)

| Parameter | Type | Description |
|---|---|---|
| profile | String |  |

##### Returns: void




