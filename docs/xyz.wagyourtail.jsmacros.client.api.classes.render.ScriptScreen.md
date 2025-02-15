

xyz.wagyourtail.jsmacros.client.api.classes.render.ScriptScreen
---------------------------------------------------------------

#### extends [BaseScreen](1.9.2/xyz/wagyourtail/wagyourgui/BaseScreen.html)

1.0.5

just go look at [IScreen](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/IScreen.html)
since all the methods are done through a mixin...

### Constructors

#### new ScriptScreen (title, dirt)

| Parameter | Type | Description |
|---|---|---|
| title | String |  |
| dirt | boolean |  |



#### Fields

[drawTitle](1.9.2/)


[shouldCloseOnEsc](1.9.2/)


[shouldPause](1.9.2/)



#### Methods

[setParent(parent)](#setParent-IScreen-)


[setOnRender(onRender)](#setOnRender-MethodWrapper-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)


[close()](#close-)


[shouldPause()](#shouldPause-)


[shouldCloseOnEsc()](#shouldCloseOnEsc-)



### Fields

#### .drawTitle


##### Type: boolean



#### .shouldCloseOnEsc

1.8.4
WARNING: this can break the game if you set it false and don't have a way to close the screen.


##### Type: boolean



#### .shouldPause

1.8.4


##### Type: boolean



### Methods

#### .setParent(parent)

1.4.0

| Parameter | Type | Description |
|---|---|---|
| parent | IScreen | parent screen to go to when this one exits. |

##### Returns: void



#### .setOnRender(onRender)

1.4.0

add custom stuff to the render function on the main thread.

| Parameter | Type | Description |
|---|---|---|
| onRender | MethodWrapper<Pos3D, DrawContext, Object, ?> | pos3d elements are mousex, mousey, tickDelta |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .close()


##### Returns: void



#### .shouldPause()


##### Returns: boolean



#### .shouldCloseOnEsc()


##### Returns: boolean




