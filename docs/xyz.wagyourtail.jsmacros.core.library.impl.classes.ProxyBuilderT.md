

xyz.wagyourtail.jsmacros.core.library.impl.classes.ProxyBuilder< T >
--------------------------------------------------------------------

#### 

1.6.0

### Constructors

#### new ProxyBuilder (clazz, interfaces)

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<T> |  |
| interfaces | Class<?>[] |  |



#### Fields

[factory](#factory)
F


[proxiedMethods](#proxiedMethods)
F


[proxiedMethodDefaults](#proxiedMethodDefaults)
F



#### Methods

[addMethod(methodNameOrSig, proxyMethod)](#addMethod-String-MethodWrapper-)


[buildInstance(constructorArgs)](#buildInstance-Object[]-)


[buildInstance(constructorSig, constructorArgs)](#buildInstance-String-Object[]-)


[buildInstance(constructorSig, constructorArgs)](#buildInstance-Class[]-Object[]-)



### Fields

#### .factory

Final

##### Type: [ProxyFactory](1.9.2/)



#### .proxiedMethods

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[ProxyBuilder$MethodSigParts](1.9.2/), [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[ProxyBuilder$ProxyReference](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ProxyBuilder.ProxyReference.html)< T >, [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)[], ? , ? >>



#### .proxiedMethodDefaults

Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[ProxyBuilder$ProxyReference](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ProxyBuilder.ProxyReference.html)< T >, [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)[], ? , ? >>



### Methods

#### .addMethod(methodNameOrSig, proxyMethod)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| methodNameOrSig | String | name of method or sig (the usual format) |
| proxyMethod | MethodWrapper<ProxyBuilder$ProxyReference<T>, Object[], ?, ?> |  |

##### Returns: [ProxyBuilder](#)< T >

self for chaining



#### .buildInstance(constructorArgs)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| constructorArgs | Object[] | args for the super constructor |

##### Returns: T

new instance of the constructor



#### .buildInstance(constructorSig, constructorArgs)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| constructorSig | String | string signature (you can skip the <init> part) |
| constructorArgs | Object[] | args for the super constructor |

##### Returns: T

new instance of the constructor



#### .buildInstance(constructorSig, constructorArgs)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| constructorSig | Class<?>[] | string signature (you can skip the <init> part) |
| constructorArgs | Object[] | args for the super constructor |

##### Returns: T

new instance of the constructor




