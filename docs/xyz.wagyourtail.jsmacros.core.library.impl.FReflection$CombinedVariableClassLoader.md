

xyz.wagyourtail.jsmacros.core.library.impl.FReflection$CombinedVariableClassLoader
----------------------------------------------------------------------------------

Static
#### extends [ClassLoader](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/ClassLoader.html)

1.2.8

I know this is probably bad practice, but lets be real, this whole library is bad practice, So I can make it
worse, right? at least this should work better than `try/catch`'ing using
[ClassLoader#loadClass(java.lang.String)](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/ClassLoader.html) to search through every [URLClassLoader](https://docs.oracle.com/javase/8/docs/api/index.html?java/net/URLClassLoader.html) that
[FReflection#loadJarFile(java.lang.String)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FReflection.html#loadJarFile-String-) would make, or how I was previously doing it by pre-loading and caching
all the classes to a [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)

This class is a modification to
[Christian d'Heureuse's JoinClassLoader](https://www.source-code.biz/snippets/java/12.htm), under the
[Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0) to change it from a Class array to a
[Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html), to allow for modifications to the [ClassLoader](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/ClassLoader.html) contained in the classLoader.

### Constructors

#### new FReflection$CombinedVariableClassLoader (parent)

| Parameter | Type | Description |
|---|---|---|
| parent | ClassLoader |  |



#### Methods

[addClassLoader(jarPath, loader)](#addClassLoader-File-ClassLoader-)


[hasJar(path)](#hasJar-File-)



### Methods

#### .addClassLoader(jarPath, loader)

| Parameter | Type | Description |
|---|---|---|
| jarPath | File |  |
| loader | ClassLoader |  |

##### Returns: boolean



#### .hasJar(path)

| Parameter | Type | Description |
|---|---|---|
| path | File |  |

##### Returns: boolean




