

xyz.wagyourtail.jsmacros.core.config.ConfigManager
--------------------------------------------------

#### 

### Constructors

#### new ConfigManager (configFolder, macroFolder, logger)

| Parameter | Type | Description |
|---|---|---|
| configFolder | File |  |
| macroFolder | File |  |
| logger | Logger |  |



#### Fields

[optionClasses](#optionClasses)
F


[options](#options)
F


[configFolder](#configFolder)
F


[macroFolder](#macroFolder)
F


[configFile](#configFile)
F


[LOGGER](#LOGGER)
F


[rawOptions](#rawOptions)



#### Methods

[reloadRawConfigFromFile()](#reloadRawConfigFromFile-)


[convertConfigFormat()](#convertConfigFormat-)


[convertConfigFormat(clazz)](#convertConfigFormat-Class-)


[getOptions(optionClass)](#getOptions-Class-)


[addOptions(key, optionClass)](#addOptions-String-Class-)


[loadConfig()](#loadConfig-)


[loadDefaults()](#loadDefaults-)


[saveConfig()](#saveConfig-)



### Fields

#### .optionClasses

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>



#### .options

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >, [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>



#### .configFolder

Final

##### Type: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .macroFolder

Final

##### Type: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .configFile

Final

##### Type: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



#### .LOGGER

Final

##### Type: [Logger](https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.30/index.html?org/slf4j/Logger.html)



#### .rawOptions


##### Type: [JsonObject](1.9.2/)



### Methods

#### .reloadRawConfigFromFile()


##### Returns: void



#### .convertConfigFormat()


##### Returns: void



#### .convertConfigFormat(clazz)

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> |  |

##### Returns: void



#### .getOptions< T >(optionClass)

| Parameter | Type | Description |
|---|---|---|
| optionClass | Class<T> |  |

##### Returns: T



#### .addOptions(key, optionClass)

| Parameter | Type | Description |
|---|---|---|
| key | String |  |
| optionClass | Class<?> |  |

##### Returns: void



#### .loadConfig()


##### Returns: void



#### .loadDefaults()


##### Returns: void



#### .saveConfig()


##### Returns: void




