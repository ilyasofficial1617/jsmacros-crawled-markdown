

xyz.wagyourtail.jsmacros.core.extensions.Extension
--------------------------------------------------

Interface
#### 

#### Methods

[minCoreVersion()](#minCoreVersion-)


[maxCoreVersion()](#maxCoreVersion-)


[init()](#init-)


[getPriority()](#getPriority-)


[getLanguageImplName()](#getLanguageImplName-)


[extensionMatch(file)](#extensionMatch-File-)


[defaultFileExtension()](#defaultFileExtension-)


[getLanguage(runner)](#getLanguage-Core-)


[getLibraries()](#getLibraries-)


[getDependencies()](#getDependencies-)


[getDependenciesInternal(clazz, fname)](#getDependenciesInternal-Class-String-)
S


[wrapException(t)](#wrapException-Throwable-)


[getTranslations(lang)](#getTranslations-String-)


[getTranslationsInternal(clazz, fname)](#getTranslationsInternal-Class-String-)
S


[isGuestObject(o)](#isGuestObject-Object-)



### Methods

#### .minCoreVersion()

1.9.0


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the \*minimum\* version of the jsMacros core that this extension is compatible with.



#### .maxCoreVersion()

1.9.0


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the \*maximum\* version of the jsMacros core that this extension is compatible with.



#### .init()


##### Returns: void



#### .getPriority()


##### Returns: int



#### .getLanguageImplName()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .extensionMatch(file)

| Parameter | Type | Description |
|---|---|---|
| file | File |  |

##### Returns: [Extension$ExtMatch](1.9.2/xyz/wagyourtail/jsmacros/core/extensions/Extension.ExtMatch.html)



#### .defaultFileExtension()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getLanguage(runner)

| Parameter | Type | Description |
|---|---|---|
| runner | Core<?, ?> |  |

##### Returns: [BaseLanguage](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseLanguage.html)< ? , ? >

a single static instance of the language definition



#### .getLibraries()


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>



#### .getDependencies()


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[URL](https://docs.oracle.com/javase/8/docs/api/index.html?java/net/URL.html)>



#### .getDependenciesInternal(clazz, fname)

Static
| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> |  |
| fname | String |  |

##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[URL](https://docs.oracle.com/javase/8/docs/api/index.html?java/net/URL.html)>



#### .wrapException(t)

| Parameter | Type | Description |
|---|---|---|
| t | Throwable |  |

##### Returns: [BaseWrappedException](1.9.2/xyz/wagyourtail/jsmacros/core/language/BaseWrappedException.html)< ? >



#### .getTranslations(lang)

| Parameter | Type | Description |
|---|---|---|
| lang | String |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getTranslationsInternal(clazz, fname)

Static
| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> |  |
| fname | String |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .isGuestObject(o)

| Parameter | Type | Description |
|---|---|---|
| o | Object |  |

##### Returns: boolean




