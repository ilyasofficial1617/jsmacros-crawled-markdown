
[ScriptCodeCompiler](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/scriptimpl/ScriptCodeCompiler.html) [NoStyleCodeCompiler](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/impl/NoStyleCodeCompiler.html) [DefaultCodeCompiler](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/impl/DefaultCodeCompiler.html)

xyz.wagyourtail.jsmacros.client.gui.editor.highlighting.AbstractRenderCodeCompiler
----------------------------------------------------------------------------------

Abstract
#### 

### Constructors

#### new AbstractRenderCodeCompiler (language, screen)

| Parameter | Type | Description |
|---|---|---|
| language | String |  |
| screen | EditorScreen |  |



#### Methods

[recompileRenderedText(text)](#recompileRenderedText-String-)
A


[getRightClickOptions(index)](#getRightClickOptions-int-)
A


[getRenderedText()](#getRenderedText-)
A


[getSuggestions()](#getSuggestions-)
A



### Methods

#### .recompileRenderedText(text)

Abstract
| Parameter | Type | Description |
|---|---|---|
| text | String |  |

##### Returns: void



#### .getRightClickOptions(index)

Abstract
| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Runnable](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Runnable.html)>



#### .getRenderedText()

Abstract

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)[]



#### .getSuggestions()

Abstract

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AutoCompleteSuggestion](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/AutoCompleteSuggestion.html)>




