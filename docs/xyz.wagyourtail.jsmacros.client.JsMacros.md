

xyz.wagyourtail.jsmacros.client.JsMacros
----------------------------------------

#### 

### Constructors

#### new JsMacros ()




#### Fields

[MOD\_ID](#MOD_ID)
S
F


[LOGGER](#LOGGER)
S
F


[keyBinding](#keyBinding)
S


[prevScreen](#prevScreen)
S


[core](#core)
S
F



#### Methods

[onInitialize()](#onInitialize-)
S


[onInitializeClient()](#onInitializeClient-)
S


[getKeyText(translationKey)](#getKeyText-String-)
S


[getScreenName(s)](#getScreenName-Screen-)
S


[getLocalizedName(keyCode)](#getLocalizedName-InputUtil$Key-)
S
D


[getMinecraft()](#getMinecraft-)
S
D


[range(end)](#range-int-)
S


[range(start, end)](#range-int-int-)
S


[range(start, end, iter)](#range-int-int-int-)
S


[getModLoader()](#getModLoader-)
S



### Fields

#### .MOD\_ID

Static
Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .LOGGER

Static
Final

##### Type: [Logger](https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.30/index.html?org/slf4j/Logger.html)



#### .keyBinding

Static

##### Type: [KeyBinding](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/option/KeyBinding)



#### .prevScreen

Static

##### Type: [BaseScreen](1.9.2/xyz/wagyourtail/wagyourgui/BaseScreen.html)



#### .core

Static
Final

##### Type: [Core](1.9.2/xyz/wagyourtail/jsmacros/core/Core.html)<[Profile](1.9.2/xyz/wagyourtail/jsmacros/client/config/Profile.html), [EventRegistry](1.9.2/xyz/wagyourtail/jsmacros/client/event/EventRegistry.html)>



### Methods

#### .onInitialize()

Static

##### Returns: void



#### .onInitializeClient()

Static

##### Returns: void



#### .getKeyText(translationKey)

Static
| Parameter | Type | Description |
|---|---|---|
| translationKey | String |  |

##### Returns: [Text](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/text/Text)



#### .getScreenName(s)

Static
| Parameter | Type | Description |
|---|---|---|
| s | Screen |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getLocalizedName(keyCode)

Static
Deprecated
| Parameter | Type | Description |
|---|---|---|
| keyCode | InputUtil$Key |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getMinecraft()

Static
Deprecated

##### Returns: [MinecraftClient](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/MinecraftClient)



#### .range(end)

Static
| Parameter | Type | Description |
|---|---|---|
| end | int |  |

##### Returns: int []



#### .range(start, end)

Static
| Parameter | Type | Description |
|---|---|---|
| start | int |  |
| end | int |  |

##### Returns: int []



#### .range(start, end, iter)

Static
| Parameter | Type | Description |
|---|---|---|
| start | int |  |
| end | int |  |
| iter | int |  |

##### Returns: int []



#### .getModLoader()

Static

##### Returns: [ModLoader](1.9.2/xyz/wagyourtail/jsmacros/client/ModLoader.html)




