
[MixinChatHud](1.9.2/xyz/wagyourtail/jsmacros/client/mixins/access/MixinChatHud.html)

xyz.wagyourtail.jsmacros.client.access.IChatHud
-----------------------------------------------

Interface
#### 

#### Methods

[jsmacros\_addMessageBypass(message)](#jsmacros_addMessageBypass-Text-)


[jsmacros\_getMessages()](#jsmacros_getMessages-)


[jsmacros\_removeMessageById(messageId)](#jsmacros_removeMessageById-int-)


[jsmacros\_addMessageAtIndexBypass(message, index, time)](#jsmacros_addMessageAtIndexBypass-Text-int-int-)


[jsmacros\_removeMessage(index)](#jsmacros_removeMessage-int-)


[jsmacros\_removeMessageByText(text)](#jsmacros_removeMessageByText-Text-)


[jsmacros\_removeMessagePredicate(textfilter)](#jsmacros_removeMessagePredicate-Predicate-)



### Methods

#### .jsmacros\_addMessageBypass(message)

| Parameter | Type | Description |
|---|---|---|
| message | Text |  |

##### Returns: void



#### .jsmacros\_getMessages()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ChatHudLine](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/hud/ChatHudLine)>



#### .jsmacros\_removeMessageById(messageId)

| Parameter | Type | Description |
|---|---|---|
| messageId | int |  |

##### Returns: void



#### .jsmacros\_addMessageAtIndexBypass(message, index, time)

| Parameter | Type | Description |
|---|---|---|
| message | Text |  |
| index | int |  |
| time | int |  |

##### Returns: void



#### .jsmacros\_removeMessage(index)

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: void



#### .jsmacros\_removeMessageByText(text)

| Parameter | Type | Description |
|---|---|---|
| text | Text |  |

##### Returns: void



#### .jsmacros\_removeMessagePredicate(textfilter)

| Parameter | Type | Description |
|---|---|---|
| textfilter | Predicate<ChatHudLine> |  |

##### Returns: void




