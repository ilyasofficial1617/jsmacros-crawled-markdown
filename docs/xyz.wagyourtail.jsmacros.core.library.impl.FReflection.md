

xyz.wagyourtail.jsmacros.core.library.impl.FReflection
------------------------------------------------------

#### extends [PerExecLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLibrary.html)

1.2.3

Functions for getting and using raw java classes, methods and functions.

An instance of this class is passed to scripts as the `Reflection` variable.

#### Fields

[classLoader](#classLoader)
S
F



#### Methods

[getClass(name)](#getClass-String-)


[getClass(name, name2)](#getClass-String-String-)


[getDeclaredMethod(c, name, parameterTypes)](#getDeclaredMethod-Class-String-Class[]-)


[getDeclaredMethod(c, name, name2, parameterTypes)](#getDeclaredMethod-Class-String-String-Class[]-)


[getMethod(c, name, name2, parameterTypes)](#getMethod-Class-String-String-Class[]-)


[getMethod(c, name, parameterTypes)](#getMethod-Class-String-Class[]-)


[getDeclaredField(c, name)](#getDeclaredField-Class-String-)


[getDeclaredField(c, name, name2)](#getDeclaredField-Class-String-String-)


[getField(c, name)](#getField-Class-String-)


[getField(c, name, name2)](#getField-Class-String-String-)


[invokeMethod(m, c, objects)](#invokeMethod-Method-Object-Object[]-)


[newInstance(c, objects)](#newInstance-Class-Object[]-)


[createClassProxyBuilder(clazz, interfaces)](#createClassProxyBuilder-Class-Class[]-)


[createClassBuilder(cName, clazz, interfaces)](#createClassBuilder-String-Class-Class[]-)


[getClassFromClassBuilderResult(cName)](#getClassFromClassBuilderResult-String-)


[createLibraryBuilder(name, perExec, acceptedLangs)](#createLibraryBuilder-String-boolean-String[]-)


[createLibrary(className, javaCode)](#createLibrary-String-String-)


[compileJavaClass(className, code)](#compileJavaClass-String-String-)


[getCompiledJavaClass(className)](#getCompiledJavaClass-String-)


[getAllCompiledJavaClassVersions(className)](#getAllCompiledJavaClassVersions-String-)


[getReflect(obj)](#getReflect-Object-)


[loadJarFile(file)](#loadJarFile-String-)


[loadCurrentMappingHelper()](#loadCurrentMappingHelper-)


[getClassName(o)](#getClassName-Object-)


[loadMappingHelper(urlorfile)](#loadMappingHelper-String-)


[wrapInstace(instance)](#wrapInstace-T-)


[getWrappedClass(className)](#getWrappedClass-String-)



### Fields

#### .classLoader

Static
Final

##### Type: [FReflection$CombinedVariableClassLoader](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FReflection.CombinedVariableClassLoader.html)



### Methods

#### .getClass< T >(name)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| name | String | name of class like path.to.class |

##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< T >

resolved class



#### .getClass< T >(name, name2)

1.2.3

Use this to specify a class with intermediary and yarn names of classes for cleaner code. also has support for
java primitives by using their name in lower case.

| Parameter | Type | Description |
|---|---|---|
| name | String | first try |
| name2 | String | second try |

##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< T >

a [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html) reference.



#### .getDeclaredMethod(c, name, parameterTypes)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| parameterTypes | Class<?>[] |  |

##### Returns: [Method](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Method.html)



#### .getDeclaredMethod(c, name, name2, parameterTypes)

1.2.3

Use this to specify a method with intermediary and yarn names of classes for cleaner code.

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| name2 | String |  |
| parameterTypes | Class<?>[] |  |

##### Returns: [Method](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Method.html)

a [Method](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Method.html) reference.



#### .getMethod(c, name, name2, parameterTypes)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| name2 | String |  |
| parameterTypes | Class<?>[] |  |

##### Returns: [Method](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Method.html)



#### .getMethod(c, name, parameterTypes)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| parameterTypes | Class<?>[] |  |

##### Returns: [Method](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Method.html)



#### .getDeclaredField(c, name)

1.2.3

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |

##### Returns: [Field](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Field.html)



#### .getDeclaredField(c, name, name2)

1.2.3

Use this to specify a field with intermediary and yarn names of classes for cleaner code.

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| name2 | String |  |

##### Returns: [Field](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Field.html)

a [Field](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Field.html) reference.



#### .getField(c, name)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |

##### Returns: [Field](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Field.html)



#### .getField(c, name, name2)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| c | Class<?> |  |
| name | String |  |
| name2 | String |  |

##### Returns: [Field](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Field.html)



#### .invokeMethod(m, c, objects)

1.2.3

Invoke a method on an object with auto type coercion for numbers.

| Parameter | Type | Description |
|---|---|---|
| m | Method | method |
| c | Object | object (can be null for statics) |
| objects | Object[] |  |

##### Returns: [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)



#### .newInstance< T >(c, objects)

1.2.7

Attempts to create a new instance of a class. You probably don't have to use this one and can just call `new` on a [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html) unless you're in LUA, but then you also have the (kinda poorly
documented, can someone find a better docs link for me)
[LuaJava Library](http://luaj.sourceforge.net/api/3.2/org/luaj/vm2/lib/jse/LuajavaLib.html).

| Parameter | Type | Description |
|---|---|---|
| c | Class<T> |  |
| objects | Object[] |  |

##### Returns: T



#### .createClassProxyBuilder< T >(clazz, interfaces)

1.6.0

proxy for extending java classes in the guest language with proper threading support.

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<T> |  |
| interfaces | Class<?>[] |  |

##### Returns: [ProxyBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ProxyBuilder.html)< T >



#### .createClassBuilder< T >(cName, clazz, interfaces)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| cName | String |  |
| clazz | Class<T> |  |
| interfaces | Class<?>[] |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .getClassFromClassBuilderResult(cName)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| cName | String |  |

##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >



#### .createLibraryBuilder(name, perExec, acceptedLangs)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| perExec | boolean |  |
| acceptedLangs | String[] |  |

##### Returns: [LibraryBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/LibraryBuilder.html)



#### .createLibrary(className, javaCode)

1.8.4

A library class always has a [Library](1.9.2/xyz/wagyourtail/jsmacros/core/library/Library.html) annotation containing the name of the library,
which may differ from the actual class name. A library class must also extend
[BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html) in some way, either directly or through
[PerExecLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLibrary.html),
[PerExecLanguageLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLanguageLibrary.html)
or [PerLanguageLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerLanguageLibrary.html).

| Parameter | Type | Description |
|---|---|---|
| className | String | the fully qualified name of the class, including the package |
| javaCode | String | the source code of the library |

##### Returns: void



#### .compileJavaClass(className, code)

1.8.4

A Java Development Kit (JDK) must be installed (and potentially used to start Minecraft) in
order to compile whole classes.

Compiled classes can't be accessed from any guest language, but must be either stored through
[FGlobalVars#putObject(java.lang.String,java.lang.Object)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FGlobalVars.html#putObject-String-Object-) or retrieved from this library. Unlike normal
hot swapping, already created instances of the class will not be updated. Thus, it's
important to know which version of the class you're using when instantiating it.

| Parameter | Type | Description |
|---|---|---|
| className | String | the fully qualified name of the class, including the package |
| code | String | the java code to compile |

##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >

the compiled class.



#### .getCompiledJavaClass(className)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| className | String | the fully qualified name of the class, including the package |

##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >

the latest compiled class or `null` if it doesn't exist.



#### .getAllCompiledJavaClassVersions(className)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| className | String | the fully qualified name of the class, including the package |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >>

all compiled versions of the class, in order of compilation.



#### .getReflect(obj)

1.8.4

See [jOOR Github](1.9.2/https://github.com/jOOQ/jOOR) for more information.

| Parameter | Type | Description |
|---|---|---|
| obj | Object | the object to wrap |

##### Returns: [Reflect](1.9.2/)

a wrapper for the passed object to do help with java reflection.



#### .loadJarFile(file)

1.2.6

Loads a jar file to be accessible with this library.

| Parameter | Type | Description |
|---|---|---|
| file | String | relative to the script's folder. |

##### Returns: boolean

success value



#### .loadCurrentMappingHelper()

1.3.1


##### Returns: [Mappings](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.html)

the previous mapping helper generated with [FReflection#loadMappingHelper(java.lang.String)](#loadMappingHelper-String-)



#### .getClassName(o)

1.3.1

| Parameter | Type | Description |
|---|---|---|
| o | Object | class you want the name of |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the fully qualified class name (with "."'s not "/"'s)



#### .loadMappingHelper(urlorfile)

1.3.1

| Parameter | Type | Description |
|---|---|---|
| urlorfile | String | a url or file path the the yarn mappings -v2.jar file, or .tiny file. for example https://maven.fabricmc.net/net/fabricmc/yarn/1.16.5%2Bbuild.3/yarn-1.16.5%2Bbuild.3-v2.jar, if same url/path as previous this will load from cache. |

##### Returns: [Mappings](1.9.2/xyz/wagyourtail/jsmacros/core/classes/Mappings.html)

the associated mapping helper.



#### .wrapInstace< T >(instance)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| instance | T |  |

##### Returns: [WrappedClassInstance](1.9.2/xyz/wagyourtail/jsmacros/core/classes/WrappedClassInstance.html)< T >



#### .getWrappedClass(className)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| className | String |  |

##### Returns: [WrappedClassInstance](1.9.2/xyz/wagyourtail/jsmacros/core/classes/WrappedClassInstance.html)< ? >




