

xyz.wagyourtail.jsmacros.client.api.library.impl.FChat
------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

Functions for interacting with chat.

An instance of this class is passed to scripts as the `Chat` variable.

#### Methods

[log(message)](#log-Object-)


[log(message, await)](#log-Object-boolean-)


[logf(message, args)](#logf-String-Object[]-)


[logf(message, await, args)](#logf-String-boolean-Object[]-)


[logColor(message)](#logColor-String-)


[logColor(message, await)](#logColor-String-boolean-)


[say(message)](#say-String-)


[say(message, await)](#say-String-boolean-)


[sayf(message, args)](#sayf-String-Object[]-)


[sayf(message, await, args)](#sayf-String-boolean-Object[]-)


[open(message)](#open-String-)


[open(message, await)](#open-String-boolean-)


[title(title, subtitle, fadeIn, remain, fadeOut)](#title-Object-Object-int-int-int-)


[actionbar(text)](#actionbar-Object-)


[actionbar(text, tinted)](#actionbar-Object-boolean-)


[toast(title, desc)](#toast-Object-Object-)


[createTextHelperFromString(content)](#createTextHelperFromString-String-)


[createTextHelperFromTranslationKey(key, content)](#createTextHelperFromTranslationKey-String-Object[]-)


[getLogger()](#getLogger-)


[getLogger(name)](#getLogger-String-)


[createTextHelperFromJSON(json)](#createTextHelperFromJSON-String-)


[createTextBuilder()](#createTextBuilder-)


[createCommandBuilder(name)](#createCommandBuilder-String-)
D


[unregisterCommand(name)](#unregisterCommand-String-)
D


[reRegisterCommand(node)](#reRegisterCommand-CommandNodeHelper-)
D


[getCommandManager()](#getCommandManager-)


[getHistory()](#getHistory-)


[getTextWidth(text)](#getTextWidth-String-)


[sectionSymbolToAmpersand(string)](#sectionSymbolToAmpersand-String-)


[ampersandToSectionSymbol(string)](#ampersandToSectionSymbol-String-)


[stripFormatting(string)](#stripFormatting-String-)



### Methods

#### .log(message)

1.1.3

Log to player chat.

| Parameter | Type | Description |
|---|---|---|
| message | Object |  |

##### Returns: void



#### .log(message, await)

| Parameter | Type | Description |
|---|---|---|
| message | Object |  |
| await | boolean | should wait for message to actually be sent to chat to continue. |

##### Returns: void



#### .logf(message, args)

1.8.4

Logs the formatted message to the player's chat. The message is formatted using the default
java [String#format(java.lang.String,java.lang.Object...)](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) syntax.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to format and log |
| args | Object[] | the arguments used to format the message |

##### Returns: void



#### .logf(message, await, args)

1.8.4

Logs the formatted message to the player's chat. The message is formatted using the default
java [String#format(java.lang.String,java.lang.Object...)](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) syntax.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to format and log |
| await | boolean | whether to wait for message to be sent to chat before continuing |
| args | Object[] | the arguments used to format the message |

##### Returns: void



#### .logColor(message)

1.9.0

log with auto wrapping with [FChat#ampersandToSectionSymbol(java.lang.String)](#ampersandToSectionSymbol-String-)

| Parameter | Type | Description |
|---|---|---|
| message | String |  |

##### Returns: void



#### .logColor(message, await)

1.9.0

log with auto wrapping with [FChat#ampersandToSectionSymbol(java.lang.String)](#ampersandToSectionSymbol-String-)

| Parameter | Type | Description |
|---|---|---|
| message | String |  |
| await | boolean |  |

##### Returns: void



#### .say(message)

1.0.0

Say to server as player.

| Parameter | Type | Description |
|---|---|---|
| message | String |  |

##### Returns: void



#### .say(message, await)

1.3.1

Say to server as player.

| Parameter | Type | Description |
|---|---|---|
| message | String |  |
| await | boolean |  |

##### Returns: void



#### .sayf(message, args)

1.8.4

Sends the formatted message to the server. The message is formatted using the default java
[String#format(java.lang.String,java.lang.Object...)](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) syntax.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to format and send to the server |
| args | Object[] | the arguments used to format the message |

##### Returns: void



#### .sayf(message, await, args)

1.8.4

Sends the formatted message to the server. The message is formatted using the default java
[String#format(java.lang.String,java.lang.Object...)](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) syntax.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to format and send to the server |
| await | boolean | whether to wait for message to be sent to chat before continuing |
| args | Object[] | the arguments used to format the message |

##### Returns: void



#### .open(message)

1.6.4

open the chat input box with specific text already typed.

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to start the chat screen with |

##### Returns: void



#### .open(message, await)

1.6.4

open the chat input box with specific text already typed.
hint: you can combine with [FJsMacros#waitForEvent(java.lang.String)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.html#waitForEvent-String-) or
[FJsMacros#once(java.lang.String,xyz.wagyourtail.jsmacros.core.MethodWrapper,java.lang.Object,?>)](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.html#once-String-MethodWrapper-) to wait for the chat screen
to close and/or the to wait for the sent message

| Parameter | Type | Description |
|---|---|---|
| message | String | the message to start the chat screen with |
| await | boolean |  |

##### Returns: void



#### .title(title, subtitle, fadeIn, remain, fadeOut)

1.2.1

Display a Title to the player.

| Parameter | Type | Description |
|---|---|---|
| title | Object |  |
| subtitle | Object |  |
| fadeIn | int |  |
| remain | int |  |
| fadeOut | int |  |

##### Returns: void



#### .actionbar(text)

1.8.1

| Parameter | Type | Description |
|---|---|---|
| text | Object |  |

##### Returns: void



#### .actionbar(text, tinted)

1.2.1

Display the smaller title that's above the actionbar.

| Parameter | Type | Description |
|---|---|---|
| text | Object |  |
| tinted | boolean |  |

##### Returns: void



#### .toast(title, desc)

1.2.5

Display a toast.

| Parameter | Type | Description |
|---|---|---|
| title | Object |  |
| desc | Object |  |

##### Returns: void



#### .createTextHelperFromString(content)

1.1.3

Creates a [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html) for use where you need one and not a string.

| Parameter | Type | Description |
|---|---|---|
| content | String |  |

##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

a new [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)



#### .createTextHelperFromTranslationKey(key, content)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| key | String |  |
| content | Object[] |  |

##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

a new [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)



#### .getLogger()

1.5.2


##### Returns: [Logger](https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.30/index.html?org/slf4j/Logger.html)



#### .getLogger(name)

1.5.2

returns a log4j logger, for logging to console only.

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [Logger](https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.30/index.html?org/slf4j/Logger.html)



#### .createTextHelperFromJSON(json)

1.1.3

Create a [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html) for use where you need one and not a string.

| Parameter | Type | Description |
|---|---|---|
| json | String |  |

##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)

a new [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)



#### .createTextBuilder()

1.3.0


##### Returns: [TextBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/TextBuilder.html)

a new builder



#### .createCommandBuilder(name)

Deprecated

1.4.2

| Parameter | Type | Description |
|---|---|---|
| name | String | name of command |

##### Returns: [CommandBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/CommandBuilder.html)



#### .unregisterCommand(name)

Deprecated

1.6.5

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandNodeHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/CommandNodeHelper.html)



#### .reRegisterCommand(node)

Deprecated

1.6.5

| Parameter | Type | Description |
|---|---|---|
| node | CommandNodeHelper |  |

##### Returns: void



#### .getCommandManager()

1.7.0


##### Returns: [CommandManager](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/CommandManager.html)



#### .getHistory()

1.7.0


##### Returns: [ChatHistoryManager](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/ChatHistoryManager.html)



#### .getTextWidth(text)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| text | String | the text to get the width of |

##### Returns: int

the width of the given text in pixels.



#### .sectionSymbolToAmpersand(string)

1.6.5

escapes & to && since 1.9.0

| Parameter | Type | Description |
|---|---|---|
| string | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

§ -> &



#### .ampersandToSectionSymbol(string)

1.6.5

escapes && to & since 1.9.0

| Parameter | Type | Description |
|---|---|---|
| string | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

& -> §



#### .stripFormatting(string)

1.6.5

| Parameter | Type | Description |
|---|---|---|
| string | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




