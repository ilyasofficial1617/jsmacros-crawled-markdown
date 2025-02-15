

xyz.wagyourtail.jsmacros.core.config.CoreConfigV2
-------------------------------------------------

#### 

### Constructors

#### new CoreConfigV2 ()




#### Fields

[maxLockTime](1.9.2/)


[defaultProfile](#defaultProfile)


[anythingIgnored](#anythingIgnored)


[profiles](#profiles)


[services](#services)



#### Methods

[getCurrentProfile()](#getCurrentProfile-)


[setCurrentProfile(pname)](#setCurrentProfile-String-)


[profileOptions()](#profileOptions-)


[getEvents()](#getEvents-)


[fromV1(v1)](#fromV1-JsonObject-)
D



### Fields

#### .maxLockTime


##### Type: long



#### .defaultProfile


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .anythingIgnored


##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .profiles


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ScriptTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/config/ScriptTrigger.html)>>



#### .services


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [ServiceTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceTrigger.html)>



### Methods

#### .getCurrentProfile()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .setCurrentProfile(pname)

| Parameter | Type | Description |
|---|---|---|
| pname | String |  |

##### Returns: void



#### .profileOptions()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getEvents()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .fromV1(v1)

Deprecated
| Parameter | Type | Description |
|---|---|---|
| v1 | JsonObject |  |

##### Returns: void




