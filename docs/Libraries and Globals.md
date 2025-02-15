

Libraries and Globals
---------------------

Instances of libraries are passed into the global context of the guest language as variables.
  

Here is a list:

### Libraries

* [**Chat**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FChat.html) - for all the chat based functions.
* [**Client**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FClient.html) - for all the client based functions.
* [**FS**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FFS.html) - for all the filesystem stuff.
* [**GlobalVars**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FGlobalVars.html) - for passing variables between script contexts.
* [**Hud**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FHud.html) - for all the 2d/3d render stuff.
* [**JavaWrapper**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FWrapper.html) - for wrapping your functions to native code.
* [**JsMacros**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FJsMacros.html) - for functions that deal with events and other jsmacros stuff. also all the stuff I couldn't find another lib for.
* [**KeyBind**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FKeyBind.html) - for all the key based functions, like forcing a key down or getting pressed keys.
* [**Player**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FPlayer.html) - for all the player based functions.
* [**Reflection**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FReflection.html) - for all the java native access functions.
* [**Request**](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FRequest.html) - for all the HTTP(s) based functions.
* [**Time**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FTime.html) - for all the time based functions.
* [**World**](1.9.2/xyz/wagyourtail/jsmacros/client/api/library/impl/FWorld.html) - for all the world based functions.

There are 3 other globally context'd variables passed to scripts.

* [**event**](#classLists)
* [**file**](https://docs.oracle.com/javase/8/docs/api/java/io/File.html)
* [**context**](1.9.2/xyz/wagyourtail/jsmacros/core/language/EventContainer.html)

