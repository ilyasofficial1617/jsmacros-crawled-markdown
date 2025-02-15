

xyz.wagyourtail.jsmacros.core.library.LibraryRegistry
-----------------------------------------------------

#### 

### Constructors

#### new LibraryRegistry ()




#### Fields

[libraries](#libraries)
F


[perExec](#perExec)
F


[perLanguage](#perLanguage)
F


[perExecLanguage](#perExecLanguage)
F



#### Methods

[getLibraries(language, context)](#getLibraries-BaseLanguage-BaseScriptContext-)


[getOnceLibraries(language)](#getOnceLibraries-BaseLanguage-)


[getPerExecLibraries(language, context)](#getPerExecLibraries-BaseLanguage-BaseScriptContext-)


[addLibrary(clazz)](#addLibrary-Class-)



### Fields

#### .libraries

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Library](1.9.2/xyz/wagyourtail/jsmacros/core/library/Library.html), [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)>



#### .perExec

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Library](1.9.2/xyz/wagyourtail/jsmacros/core/library/Library.html), [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>



#### .perLanguage

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >, [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Library](1.9.2/xyz/wagyourtail/jsmacros/core/library/Library.html), [PerLanguageLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerLanguageLibrary.html)>>



#### .perExecLanguage

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >, [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Library](1.9.2/xyz/wagyourtail/jsmacros/core/library/Library.html), [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>>



### Methods

#### .getLibraries(language, context)

| Parameter | Type | Description |
|---|---|---|
| language | BaseLanguage<?, ?> |  |
| context | BaseScriptContext<?> |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)>



#### .getOnceLibraries(language)

| Parameter | Type | Description |
|---|---|---|
| language | BaseLanguage<?, ?> |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)>



#### .getPerExecLibraries(language, context)

| Parameter | Type | Description |
|---|---|---|
| language | BaseLanguage<?, ?> |  |
| context | BaseScriptContext<?> |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)>



#### .addLibrary(clazz)

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> |  |

##### Returns: void




