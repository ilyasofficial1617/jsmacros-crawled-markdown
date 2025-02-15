

xyz.wagyourtail.jsmacros.client.api.library.impl.FKeyBind
---------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

Functions for getting and modifying key pressed states.

An instance of this class is passed to scripts as the `KeyBind` variable.

#### Methods

[getKeyCode(keyName)](#getKeyCode-String-)


[getKeyBindings()](#getKeyBindings-)


[setKeyBind(bind, key)](#setKeyBind-String-String-)


[key(keyName, keyState)](#key-String-boolean-)


[pressKey(keyName)](#pressKey-String-)


[releaseKey(keyName)](#releaseKey-String-)


[keyBind(keyBind, keyState)](#keyBind-String-boolean-)


[pressKeyBind(keyBind)](#pressKeyBind-String-)


[releaseKeyBind(keyBind)](#releaseKeyBind-String-)


[getPressedKeys()](#getPressedKeys-)



### Methods

#### .getKeyCode(keyName)

Dont use this one... get the raw minecraft keycode class.

| Parameter | Type | Description |
|---|---|---|
| keyName | String |  |

##### Returns: [InputUtil$Key](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/util/InputUtil$Key)

the raw minecraft keycode class



#### .getKeyBindings()

1.2.2


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

A [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html) of all the minecraft keybinds.



#### .setKeyBind(bind, key)

1.2.2

Sets a minecraft keybind to the specified key.

| Parameter | Type | Description |
|---|---|---|
| bind | String |  |
| key | String |  |

##### Returns: void



#### .key(keyName, keyState)

Set a key-state for a key.

| Parameter | Type | Description |
|---|---|---|
| keyName | String |  |
| keyState | boolean |  |

##### Returns: void



#### .pressKey(keyName)

1.8.4

Calls [FKeyBind#key(java.lang.String,boolean)](#key-String-boolean-) with keyState set to true.

| Parameter | Type | Description |
|---|---|---|
| keyName | String | the name of the key to press |

##### Returns: void



#### .releaseKey(keyName)

1.8.4

Calls [FKeyBind#key(java.lang.String,boolean)](#key-String-boolean-) with keyState set to false.

| Parameter | Type | Description |
|---|---|---|
| keyName | String | the name of the key to release |

##### Returns: void



#### .keyBind(keyBind, keyState)

1.2.2

Set a key-state using the name of the keybind rather than the name of the key.

This is probably the one you should use.

| Parameter | Type | Description |
|---|---|---|
| keyBind | String |  |
| keyState | boolean |  |

##### Returns: void



#### .pressKeyBind(keyBind)

1.8.4

Calls [FKeyBind#keyBind(java.lang.String,boolean)](#keyBind-String-boolean-) with keyState set to true.

| Parameter | Type | Description |
|---|---|---|
| keyBind | String | the name of the keybinding to press |

##### Returns: void



#### .releaseKeyBind(keyBind)

1.8.4

Calls [FKeyBind#keyBind(java.lang.String,boolean)](#keyBind-String-boolean-) with keyState set to false.

| Parameter | Type | Description |
|---|---|---|
| keyBind | String | the name of the keybinding to release |

##### Returns: void



#### .getPressedKeys()

1.2.6 (turned into set instead of list in 1.6.5)


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a set of currently pressed keys.




