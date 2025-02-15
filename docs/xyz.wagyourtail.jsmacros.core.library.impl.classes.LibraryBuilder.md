

xyz.wagyourtail.jsmacros.core.library.impl.classes.LibraryBuilder
-----------------------------------------------------------------

#### extends [ClassBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.html)<[BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)>

1.6.5

### Constructors

#### new LibraryBuilder (name, perExec, allowedLangs)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| perExec | boolean |  |
| allowedLangs | String[] |  |



#### Methods

[addConstructor()](#addConstructor-)


[finishBuildAndFreeze()](#finishBuildAndFreeze-)



### Methods

#### .addConstructor()

constructor, if perExec run every context, if per language run once for each lang;
params are context and language class.
if not per exec, param will be skipped.
ie:
BaseLibrary: no params
PerExecLibrary: context
PerExecLanguageLibrary: context, language
PerLanguageLibrary: language

Don't do other constructors...


##### Returns: [ClassBuilder$ConstructorBuilder](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/ClassBuilder.ConstructorBuilder.html)



#### .finishBuildAndFreeze()


##### Returns: [Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >




