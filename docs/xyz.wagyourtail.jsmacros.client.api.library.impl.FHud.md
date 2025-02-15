

xyz.wagyourtail.jsmacros.client.api.library.impl.FHud
-----------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

1.0.5

Functions for displaying stuff in 2 to 3 dimensions

An instance of this class is passed to scripts as the `Hud` variable.

#### Fields

[overlays](#overlays)
S
F


[renders](#renders)
S
F



#### Methods

[createScreen(title, dirtBG)](#createScreen-String-boolean-)


[openScreen(s)](#openScreen-IScreen-)


[getOpenScreen()](#getOpenScreen-)


[createTexture(width, height, name)](#createTexture-int-int-String-)


[createTexture(path, name)](#createTexture-String-String-)


[getRegisteredTextures()](#getRegisteredTextures-)


[getScaleFactor()](#getScaleFactor-)


[getOpenScreenName()](#getOpenScreenName-)


[isContainer()](#isContainer-)


[createDraw2D()](#createDraw2D-)


[registerDraw2D(overlay)](#registerDraw2D-IDraw2D-)
D


[unregisterDraw2D(overlay)](#unregisterDraw2D-IDraw2D-)
D


[listDraw2Ds()](#listDraw2Ds-)


[clearDraw2Ds()](#clearDraw2Ds-)


[createDraw3D()](#createDraw3D-)


[registerDraw3D(draw)](#registerDraw3D-Draw3D-)
D


[unregisterDraw3D(draw)](#unregisterDraw3D-Draw3D-)
D


[listDraw3Ds()](#listDraw3Ds-)


[clearDraw3Ds()](#clearDraw3Ds-)


[getMouseX()](#getMouseX-)


[getMouseY()](#getMouseY-)


[getWindowWidth()](#getWindowWidth-)


[getWindowHeight()](#getWindowHeight-)



### Fields

#### .overlays

Static
Final

Don't touch this here


##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)<[Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html)>>



#### .renders

Static
Final

Don't touch this here


##### Type: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html)>



### Methods

#### .createScreen(title, dirtBG)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| title | String |  |
| dirtBG | boolean | boolean of whether to use a dirt background or not. |

##### Returns: [ScriptScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/ScriptScreen.html)

a new [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html) Object.



#### .openScreen(s)

1.0.5

Opens a [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html) Object.

| Parameter | Type | Description |
|---|---|---|
| s | IScreen |  |

##### Returns: void



#### .getOpenScreen()

1.2.7


##### Returns: [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)

the currently open Screen as an [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)



#### .createTexture(width, height, name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| width | int | the width of the canvas |
| height | int | the height of the canvas |
| name | String |  |

##### Returns: [CustomImage](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/CustomImage.html)

a [CustomImage](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/CustomImage.html) that can be used as a texture for screen backgrounds, rendering
images, etc.



#### .createTexture(path, name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | absolute path to an image file |
| name | String |  |

##### Returns: [CustomImage](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/CustomImage.html)

a [CustomImage](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/CustomImage.html) that can be used as a texture for screen backgrounds, rendering
images, etc.



#### .getRegisteredTextures()

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [CustomImage](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/CustomImage.html)>

an immutable Map of all registered custom textures.



#### .getScaleFactor()

1.8.4


##### Returns: int

the current gui scale factor of minecraft.



#### .getOpenScreenName()

1.0.5, renamed from `getOpenScreen` in 1.2.7


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

The name of the currently open screen.



#### .isContainer()

1.1.2


##### Returns: boolean

a [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html) denoting if the currently open screen is a container.



#### .createDraw2D()

1.0.5


##### Returns: [Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html)



#### .registerDraw2D(overlay)

Deprecated

1.0.5

Registers an [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html) to be rendered.

| Parameter | Type | Description |
|---|---|---|
| overlay | IDraw2D<Draw2D> |  |

##### Returns: void



#### .unregisterDraw2D(overlay)

Deprecated

1.0.5

Unregisters an [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html) to stop it being rendered.

| Parameter | Type | Description |
|---|---|---|
| overlay | IDraw2D<Draw2D> |  |

##### Returns: void



#### .listDraw2Ds()

1.0.5


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html)<[Draw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw2D.html)>>

A list of current [IDraw2D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IDraw2D.html).



#### .clearDraw2Ds()

1.0.5

clears the Draw2D render list.


##### Returns: void



#### .createDraw3D()

1.0.6


##### Returns: [Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html)

a new [Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html).



#### .registerDraw3D(draw)

Deprecated

1.0.6

Registers an [Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html) to be rendered.

| Parameter | Type | Description |
|---|---|---|
| draw | Draw3D |  |

##### Returns: void



#### .unregisterDraw3D(draw)

Deprecated

1.0.6

Unregisters an [Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html) to stop it being rendered.

| Parameter | Type | Description |
|---|---|---|
| draw | Draw3D |  |

##### Returns: void



#### .listDraw3Ds()

1.0.6


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html)>

A list of current [Draw3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/Draw3D.html).



#### .clearDraw3Ds()

1.0.6

clears the Draw3D render list.


##### Returns: void



#### .getMouseX()

1.1.3


##### Returns: double

the current X coordinate of the mouse



#### .getMouseY()

1.1.3


##### Returns: double

the current Y coordinate of the mouse



#### .getWindowWidth()

1.8.4


##### Returns: int

the current window width.



#### .getWindowHeight()

1.8.4


##### Returns: int

the current window height.




