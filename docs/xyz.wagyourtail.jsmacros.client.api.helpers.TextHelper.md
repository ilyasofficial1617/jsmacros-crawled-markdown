

xyz.wagyourtail.jsmacros.client.api.helpers.TextHelper
------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)>

1.0.8

#### Fields

[STRIP\_FORMATTING\_PATTERN](#STRIP_FORMATTING_PATTERN)
S
F



#### Methods

[wrap(t)](#wrap-Text-)
S


[replaceFromJson(json)](#replaceFromJson-String-)
D


[replaceFromString(content)](#replaceFromString-String-)
D


[getJson()](#getJson-)


[getString()](#getString-)


[getStringStripFormatting()](#getStringStripFormatting-)


[withoutFormatting()](#withoutFormatting-)


[visit(visitor)](#visit-MethodWrapper-)


[getWidth()](#getWidth-)


[toJson()](#toJson-)
D


[toString()](#toString-)



### Fields

#### .STRIP\_FORMATTING\_PATTERN

Static
Final

##### Type: [Pattern](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/regex/Pattern.html)



### Methods

#### .wrap(t)

Static
| Parameter | Type | Description |
|---|---|---|
| t | Text |  |

##### Returns: [TextHelper](#)



#### .replaceFromJson(json)

Deprecated

1.0.8

replace the text in this class with JSON data.

| Parameter | Type | Description |
|---|---|---|
| json | String |  |

##### Returns: [TextHelper](#)



#### .replaceFromString(content)

Deprecated

1.0.8

replace the text in this class with [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) data.

| Parameter | Type | Description |
|---|---|---|
| content | String |  |

##### Returns: [TextHelper](#)



#### .getJson()

1.2.7


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

JSON data representation.



#### .getString()

1.2.7


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the text content.



#### .getStringStripFormatting()

1.6.5


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the text content. stripped formatting when servers send it the (super) old way due to shitty coders.



#### .withoutFormatting()

1.8.4


##### Returns: [TextHelper](#)

the text helper without the formatting applied.



#### .visit(visitor)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| visitor | MethodWrapper<StyleHelper, String, Object, ?> | function with 2 args, no return. |

##### Returns: [TextHelper](#)



#### .getWidth()

1.8.4


##### Returns: int

the width of this text.



#### .toJson()

Deprecated

1.0.8


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .toString()

1.0.8, this used to do the same as [TextHelper#getString()](#getString-)


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

String representation of text helper.




