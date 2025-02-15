

xyz.wagyourtail.jsmacros.client.api.classes.FakeServerCommandSource
-------------------------------------------------------------------

#### extends [ServerCommandSource](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/server/command/ServerCommandSource)

1.8.4

### Constructors

#### new FakeServerCommandSource (source, player)

| Parameter | Type | Description |
|---|---|---|
| source | ClientCommandSource |  |
| player | ClientPlayerEntity |  |



#### Methods

[getEntitySuggestions()](#getEntitySuggestions-)


[getChatSuggestions()](#getChatSuggestions-)


[getPlayerNames()](#getPlayerNames-)


[getTeamNames()](#getTeamNames-)


[getSoundIds()](#getSoundIds-)


[getRecipeIds()](#getRecipeIds-)


[getCompletions(context)](#getCompletions-CommandContext-)


[getBlockPositionSuggestions()](#getBlockPositionSuggestions-)


[getPositionSuggestions()](#getPositionSuggestions-)


[getWorldKeys()](#getWorldKeys-)


[getRegistryManager()](#getRegistryManager-)


[sendFeedback(feedbackSupplier, broadcastToOps)](#sendFeedback-Supplier-boolean-)



### Methods

#### .getEntitySuggestions()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getChatSuggestions()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getPlayerNames()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getTeamNames()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .getSoundIds()


##### Returns: [Stream](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/stream/Stream.html)<[Identifier](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/Identifier)>



#### .getRecipeIds()


##### Returns: [Stream](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/stream/Stream.html)<[Identifier](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/Identifier)>



#### .getCompletions(context)

| Parameter | Type | Description |
|---|---|---|
| context | CommandContext<?> |  |

##### Returns: [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/concurrent/CompletableFuture.html)<[Suggestions](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=com/mojang/brigadier/suggestion/Suggestions)>



#### .getBlockPositionSuggestions()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[CommandSource$RelativePosition](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/command/CommandSource$RelativePosition)>



#### .getPositionSuggestions()


##### Returns: [Collection](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Collection.html)<[CommandSource$RelativePosition](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/command/CommandSource$RelativePosition)>



#### .getWorldKeys()


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[RegistryKey](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/registry/RegistryKey)<[World](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/world/World)>>



#### .getRegistryManager()


##### Returns: [DynamicRegistryManager](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/registry/DynamicRegistryManager)



#### .sendFeedback(feedbackSupplier, broadcastToOps)

| Parameter | Type | Description |
|---|---|---|
| feedbackSupplier | Supplier<Text> |  |
| broadcastToOps | boolean |  |

##### Returns: void




