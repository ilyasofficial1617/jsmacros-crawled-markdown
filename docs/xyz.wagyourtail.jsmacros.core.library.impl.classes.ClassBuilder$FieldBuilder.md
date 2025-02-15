

xyz.wagyourtail.jsmacros.core.library.impl.classes.ClassBuilder$FieldBuilder
----------------------------------------------------------------------------

#### 

### Constructors

#### new ClassBuilder$FieldBuilder (fieldType, name)

| Parameter | Type | Description |
|---|---|---|
| fieldType | CtClass |  |
| name | String |  |



#### Fields

[fieldInitializer](#fieldInitializer)



#### Methods

[compile(code)](#compile-String-)


[rename(name)](#rename-String-)


[makePrivate()](#makePrivate-)


[makePublic()](#makePublic-)


[makeProtected()](#makeProtected-)


[makePackagePrivate()](#makePackagePrivate-)


[toggleStatic()](#toggleStatic-)


[toggleFinal()](#toggleFinal-)


[getMods()](#getMods-)


[getModString()](#getModString-)


[addAnnotation(type)](#addAnnotation-Class-)


[initializer()](#initializer-)


[end()](#end-)



### Fields

#### .fieldInitializer


##### Type: [CtField$Initializer](1.9.2/)



### Methods

#### .compile(code)

| Parameter | Type | Description |
|---|---|---|
| code | String |  |

##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >



#### .rename(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [ClassBuilder$FieldBuilder](#)



#### .makePrivate()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .makePublic()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .makeProtected()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .makePackagePrivate()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .toggleStatic()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .toggleFinal()


##### Returns: [ClassBuilder$FieldBuilder](#)



#### .getMods()


##### Returns: int



#### .getModString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .addAnnotation(type)

| Parameter | Type | Description |
|---|---|---|
| type | Class<?> |  |

##### Returns: [ClassBuilder$AnnotationBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.AnnotationBuilder.html)<[ClassBuilder$FieldBuilder](#)>



#### .initializer()


##### Returns: [ClassBuilder$FieldBuilder$FieldInitializerBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.FieldBuilder.FieldInitializerBuilder.html)



#### .end()


##### Returns: [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)< T >




