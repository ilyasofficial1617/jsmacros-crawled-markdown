

xyz.wagyourtail.jsmacros.client.gui.editor.highlighting.scriptimpl.CodeCompileEvent
-----------------------------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.3.1

"hidden" event for script based code style compiling / linting tasks.
remember to `consumer.autoWrap()` everything.

### Constructors

#### new CodeCompileEvent (code, language, screen)

| Parameter | Type | Description |
|---|---|---|
| code | String |  |
| language | String |  |
| screen | EditorScreen |  |



#### Fields

[cursor](#cursor)
F


[code](#code)
F


[language](#language)
F


[screen](#screen)
F


[textLines](#textLines)
F


[autoCompleteSuggestions](#autoCompleteSuggestions)
F


[rightClickActions](#rightClickActions)



#### Methods

[genPrismNodes()](#genPrismNodes-)


[createMap()](#createMap-)


[createTextBuilder()](#createTextBuilder-)


[createSuggestion(startIndex, suggestion)](#createSuggestion-int-String-)


[createSuggestion(startIndex, suggestion, displayText)](#createSuggestion-int-String-TextHelper-)


[createPrefixTree()](#createPrefixTree-)


[getThemeData()](#getThemeData-)



### Fields

#### .cursor

Final

##### Type: [SelectCursor](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/SelectCursor.html)



#### .code

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .language

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .screen

Final

##### Type: [EditorScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/EditorScreen.html)



#### .textLines

Final

you are expected to fill this in with text styling, if not filled, nothing will render
if the code is an empty string, you are still expected to put an empty string as the first line here


##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)>



#### .autoCompleteSuggestions

Final

you are expected to fill this with suggestions for autocomplete created using
[CodeCompileEvent#createSuggestion(int,java.lang.String)](#createSuggestion-int-String-)


##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[AutoCompleteSuggestion](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/AutoCompleteSuggestion.html)>



#### .rightClickActions

you are expected to fill this with a method to create right click actions.
method should be `(index:number) => Map<string,() => void>`,
meaning it accepts a character index and returns a map of names to actions.


##### Type: [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [MethodWrapper](1.9.2/xyz/wagyourtail/jsmacros/core/MethodWrapper.html)<[Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html), ? >>, ? >



### Methods

#### .genPrismNodes()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Prism4j$Node](1.9.2/)>

[Prism4j's
node list](https://github.com/noties/Prism4j/blob/75ac3dae6f8eff5b1b0396df3b806f44ce86c484/prism4j/src/main/java/io/noties/prism4j/Prism4j.java#L54) you don't have to use it but if you're not compiling your own...
peek at the code of [TextStyleCompiler](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/impl/TextStyleCompiler.html) for the default impl for walking the node tree.



#### .createMap()

Easy access to the [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html) object for use with [CodeCompileEvent#rightClickActions](#rightClickActions)


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)< ? , ? >

specifically a [LinkedHashMap](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/LinkedHashMap.html)



#### .createTextBuilder()

more convenient access to TextBuilder


##### Returns: [TextBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/TextBuilder.html)

new instance for use with [CodeCompileEvent#textLines](#textLines)



#### .createSuggestion(startIndex, suggestion)

| Parameter | Type | Description |
|---|---|---|
| startIndex | int |  |
| suggestion | String |  |

##### Returns: [AutoCompleteSuggestion](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/AutoCompleteSuggestion.html)



#### .createSuggestion(startIndex, suggestion, displayText)

| Parameter | Type | Description |
|---|---|---|
| startIndex | int | index that is where the suggestion starts from before the already typed part |
| suggestion | String | complete suggestion including the already typed part |
| displayText | TextHelper | how the text should be displayed in the dropdown, default is suggestion text |

##### Returns: [AutoCompleteSuggestion](1.9.2/xyz/wagyourtail/jsmacros/client/gui/editor/highlighting/AutoCompleteSuggestion.html)

a new suggestion object



#### .createPrefixTree()

prefix tree data structure written for you, it's a bit intensive to add things to, especially how I wrote it, but
lookup times are much better at least on larger data sets,
so create a single copy of this for your static autocompletes and don't be re-creating this every time, store it
in `globalvars`, probably per language

or just don't use it, I'm not forcing you to.


##### Returns: [StringHashTrie](1.9.2/xyz/wagyourtail/StringHashTrie.html)

a new [StringHashTrie](1.9.2/xyz/wagyourtail/StringHashTrie.html)



#### .getThemeData()


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), short []>

`key -> hex integer` values for theme data points, this can be used with the prism data for
coloring, just have to use [TextBuilder#withColor(int,int,int)](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/TextBuilder.html#withColor-int-int-int-)
on 1.15 and older versions the integer values with be the default color's index so you can directly pass it
to [TextBuilder#withColor(int)](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/TextBuilder.html#withColor-int-)




