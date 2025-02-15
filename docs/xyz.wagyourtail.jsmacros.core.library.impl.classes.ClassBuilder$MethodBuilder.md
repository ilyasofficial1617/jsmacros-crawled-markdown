
[ClassBuilder$ConstructorBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.ConstructorBuilder.html)

xyz.wagyourtail.jsmacros.core.library.impl.classes.ClassBuilder$MethodBuilder
-----------------------------------------------------------------------------

#### 

### Constructors

#### new ClassBuilder$MethodBuilder (methodReturnType, methodName, params)

| Parameter | Type | Description |
|---|---|---|
| methodReturnType | CtClass |  |
| methodName | String |  |
| params | CtClass[] |  |



#### Methods

[compile(code)](#compile-String-)


[makePrivate()](#makePrivate-)


[makePublic()](#makePublic-)


[makeProtected()](#makeProtected-)


[makePackagePrivate()](#makePackagePrivate-)


[toggleStatic()](#toggleStatic-)


[rename(newName)](#rename-String-)


[exceptions(exceptions)](#exceptions-Class[]-)


[body(code\_src)](#body-String-)


[guestBody(methodBody)](#guestBody-MethodWrapper-)


[buildBody()](#buildBody-)


[body(buildBody)](#body-MethodWrapper-)


[endAbstract()](#endAbstract-)


[addAnnotation(type)](#addAnnotation-Class-)



### Methods

#### .compile(code)

| Parameter | Type | Description |
|---|---|---|
| code | String |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .makePrivate()


##### Returns: [ClassBuilder$MethodBuilder](#)



#### .makePublic()


##### Returns: [ClassBuilder$MethodBuilder](#)



#### .makeProtected()


##### Returns: [ClassBuilder$MethodBuilder](#)



#### .makePackagePrivate()


##### Returns: [ClassBuilder$MethodBuilder](#)



#### .toggleStatic()


##### Returns: [ClassBuilder$MethodBuilder](#)



#### .rename(newName)

| Parameter | Type | Description |
|---|---|---|
| newName | String |  |

##### Returns: [ClassBuilder$MethodBuilder](#)



#### .exceptions(exceptions)

| Parameter | Type | Description |
|---|---|---|
| exceptions | Class<?>[] |  |

##### Returns: [ClassBuilder$MethodBuilder](#)



#### .body(code\_src)

| Parameter | Type | Description |
|---|---|---|
| code_src | String |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .guestBody(methodBody)

| Parameter | Type | Description |
|---|---|---|
| methodBody | MethodWrapper<Object, Object, Object, ?> |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .buildBody()


##### Returns: [ClassBuilder$BodyBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.BodyBuilder.html)



#### .body(buildBody)

| Parameter | Type | Description |
|---|---|---|
| buildBody | MethodWrapper<CtClass, CtBehavior, Object, ?> |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .endAbstract()


##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .addAnnotation(type)

| Parameter | Type | Description |
|---|---|---|
| type | Class<?> |  |

##### Returns: [ClassBuilder$AnnotationBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.AnnotationBuilder.html)<[ClassBuilder$MethodBuilder](#)>




