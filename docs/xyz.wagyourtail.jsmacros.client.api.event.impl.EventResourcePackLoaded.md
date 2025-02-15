

xyz.wagyourtail.jsmacros.client.api.event.impl.EventResourcePackLoaded
----------------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.5.1

This event is fired after resources have been reloaded, i.e. after the splash screen has finished.
This includes when the game is finished loading and the title screen becomes visible, which you can check using
[EventResourcePackLoaded#isGameStart](1.9.2/).

### Constructors

#### new EventResourcePackLoaded (isGameStart)

| Parameter | Type | Description |
|---|---|---|
| isGameStart | boolean |  |



#### Fields

[isGameStart](1.9.2/)
F


[loadedPacks](#loadedPacks)
F



#### Methods

[toString()](#toString-)



### Fields

#### .isGameStart

Final

##### Type: boolean



#### .loadedPacks

Final

##### Type: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



### Methods

#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




