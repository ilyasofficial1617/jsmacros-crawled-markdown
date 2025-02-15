
[LibraryBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/LibraryBuilder.html)

xyz.wagyourtail.jsmacros.core.library.impl.classes.ClassBuilder< T >
--------------------------------------------------------------------

#### 

1.6.5

### Constructors

#### new ClassBuilder (name, parent, interfaces)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| parent | Class<T> |  |
| interfaces | Class<?>[] |  |



#### Fields

[methodWrappers](#methodWrappers)
S
F


[ctClass](#ctClass)
F



#### Methods

[addField(fieldType, name)](#addField-Class-String-)


[addField(code)](#addField-String-)


[addMethod(returnType, name, params)](#addMethod-Class-String-Class[]-)


[addMethod(code)](#addMethod-String-)


[addConstructor(params)](#addConstructor-Class[]-)


[addConstructor(code)](#addConstructor-String-)


[addClinit()](#addClinit-)


[addAnnotation(type)](#addAnnotation-Class-)


[finishBuildAndFreeze()](#finishBuildAndFreeze-)



### Fields

#### .methodWrappers

Static
Final

##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >>



#### .ctClass

Final

##### Type: [CtClass](1.9.2/)



### Methods

#### .addField(fieldType, name)

| Parameter | Type | Description |
|---|---|---|
| fieldType | Class<?> |  |
| name | String |  |

##### Returns: [ClassBuilder$FieldBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.FieldBuilder.html)



#### .addField(code)

1.8.4

The code must define the full field, including visibility, type, name and an optional value.
Generic types are not supported and must be explicitly cast in the source code when used.
Annotations are also not supported.
Just like in java, classes from the `java.lang` package don't need a fully qualified name.
Examples are:

```
                 private String name;
                 private java.lang.String name;
                 public java.util.List list = new java.util.ArrayList();
                 static int value = 10;
                 
```
| Parameter | Type | Description |
|---|---|---|
| code | String | the code for the field |

##### Returns: [ClassBuilder](#)< T >

self for chaining.



#### .addMethod(returnType, name, params)

| Parameter | Type | Description |
|---|---|---|
| returnType | Class<?> |  |
| name | String |  |
| params | Class<?>[] |  |

##### Returns: [ClassBuilder$MethodBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.MethodBuilder.html)



#### .addMethod(code)

1.8.4

The code must define the full method, including visibility, return type, name and parameters.
Generic types are not supported as return values or arguments, neither can varargs be used.
Annotations are also not supported.
Just like in java, classes from the `java.lang` package don't need a fully qualified name.
Examples are:

```
                 public Object id(Object obj) { return obj; }
                 private void print(String text) { System.out.println(text); }
                 private static java.util.Map toMap(Object[] keys, Object[] values) {
                      java.util.Map map = new java.util.HashMap();
                      for (int i = 0; i < keys.length; i++) {
                          map.put(keys[i], values[i]);
                      }
                      return map;
                  }
                 public String toString() {
                      System.out.println(super.toString());
                      return "Hello World!";
                  }
                 
```
| Parameter | Type | Description |
|---|---|---|
| code | String | the code for the method |

##### Returns: [ClassBuilder](#)< T >

self for chaining.



#### .addConstructor(params)

| Parameter | Type | Description |
|---|---|---|
| params | Class<?>[] |  |

##### Returns: [ClassBuilder$ConstructorBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.ConstructorBuilder.html)



#### .addConstructor(code)

1.8.4

The code must define the full constructor, including visibility and parameters.
Generic types are not supported as arguments, neither can varargs be used.
Annotations are also not supported.
Just like in java, classes from the `java.lang` package don't need a fully qualified name.
To make sure the class can be easily instantiated, the visibility of the constructor should be public.
Examples are:

```
                 public MyClass() { }
                 public MyClass(String text) { System.out.println(text); }
                 protected MyClass(String text, int number) { super(text, number, ""); }
                 public MyClass(String text, int number, String other) {
                      this(text, number);
                      this.other = other;
                 }
                 
```
| Parameter | Type | Description |
|---|---|---|
| code | String | the code for the constructor |

##### Returns: [ClassBuilder](#)< T >

self for chaining.



#### .addClinit()


##### Returns: [ClassBuilder$ConstructorBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.ConstructorBuilder.html)



#### .addAnnotation(type)

| Parameter | Type | Description |
|---|---|---|
| type | Class<?> |  |

##### Returns: [ClassBuilder$AnnotationBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.AnnotationBuilder.html)<[ClassBuilder](#)< T >>



#### .finishBuildAndFreeze()


##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >




