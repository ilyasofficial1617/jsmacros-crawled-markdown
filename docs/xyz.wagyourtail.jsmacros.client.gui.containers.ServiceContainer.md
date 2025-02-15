

xyz.wagyourtail.jsmacros.client.gui.containers.ServiceContainer
---------------------------------------------------------------

#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[MacroScreen](1.9.2/xyz/wagyourtail/jsmacros/client/gui/screens/MacroScreen.html)>

### Constructors

#### new ServiceContainer (x, y, width, height, textRenderer, parent, service)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| parent | ServiceScreen |  |
| service | String |  |



#### Fields

[service](#service)



#### Methods

[init()](#init-)


[getEnabled()](#getEnabled-)


[getRunning()](#getRunning-)


[getTrigger()](#getTrigger-)


[setFile(file)](#setFile-File-)


[setPos(x, y, width, height)](#setPos-int-int-int-int-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .service


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .init()


##### Returns: void



#### .getEnabled()


##### Returns: boolean



#### .getRunning()


##### Returns: boolean



#### .getTrigger()


##### Returns: [ServiceTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceTrigger.html)



#### .setFile(file)

| Parameter | Type | Description |
|---|---|---|
| file | File |  |

##### Returns: void



#### .setPos(x, y, width, height)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




