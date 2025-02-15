

xyz.wagyourtail.wagyourgui.containers.ListContainer
---------------------------------------------------

#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[IContainerParent](1.9.2/xyz/wagyourtail/wagyourgui/containers/IContainerParent.html)>

### Constructors

#### new ListContainer (x, y, width, height, textRenderer, list, parent, onSelect)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| list | List<Text> |  |
| parent | IOverlayParent |  |
| onSelect | Consumer<Integer> |  |



#### Fields

[onSelect](#onSelect)



#### Methods

[init()](#init-)


[addItem(name)](#addItem-Text-)


[setSelected(index)](#setSelected-int-)


[onScrollbar(page)](#onScrollbar-double-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .onSelect


##### Type: [Consumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Consumer.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Integer.html)>



### Methods

#### .init()


##### Returns: void



#### .addItem(name)

| Parameter | Type | Description |
|---|---|---|
| name | Text |  |

##### Returns: void



#### .setSelected(index)

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: void



#### .onScrollbar(page)

| Parameter | Type | Description |
|---|---|---|
| page | double |  |

##### Returns: void



#### .render(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void




