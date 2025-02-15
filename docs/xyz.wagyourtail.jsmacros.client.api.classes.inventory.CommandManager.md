

xyz.wagyourtail.jsmacros.client.api.classes.inventory.CommandManager
--------------------------------------------------------------------

Abstract
#### 

1.7.0

### Constructors

#### new CommandManager ()




#### Fields

[instance](#instance)
S



#### Methods

[getValidCommands()](#getValidCommands-)


[createCommandBuilder(name)](#createCommandBuilder-String-)
A


[unregisterCommand(command)](#unregisterCommand-String-)
A


[reRegisterCommand(node)](#reRegisterCommand-CommandNodeHelper-)
A


[getArgumentAutocompleteOptions(commandPart, callback)](#getArgumentAutocompleteOptions-String-MethodWrapper-)



### Fields

#### .instance

Static

##### Type: [CommandManager](#)



### Methods

#### .getValidCommands()

1.7.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

list of commands



#### .createCommandBuilder(name)

Abstract

1.7.0

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [CommandBuilder](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/CommandBuilder.html)



#### .unregisterCommand(command)

Abstract

1.7.0

| Parameter | Type | Description |
|---|---|---|
| command | String |  |

##### Returns: [CommandNodeHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/CommandNodeHelper.html)



#### .reRegisterCommand(node)

Abstract

1.7.0

warning: this method is hacky

| Parameter | Type | Description |
|---|---|---|
| node | CommandNodeHelper |  |

##### Returns: void



#### .getArgumentAutocompleteOptions(commandPart, callback)

1.8.2

| Parameter | Type | Description |
|---|---|---|
| commandPart | String |  |
| callback | MethodWrapper<List<String>, Object, Object, ?> |  |

##### Returns: void




