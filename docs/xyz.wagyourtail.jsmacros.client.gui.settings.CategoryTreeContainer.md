

xyz.wagyourtail.jsmacros.client.gui.settings.CategoryTreeContainer
------------------------------------------------------------------

#### extends [MultiElementContainer](1.9.2/xyz/wagyourtail/wagyourgui/containers/MultiElementContainer.html)<[ICategoryTreeParent](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/ICategoryTreeParent.html)> implements [ICategoryTreeParent](1.9.2/xyz/wagyourtail/jsmacros/client/gui/settings/ICategoryTreeParent.html)

### Constructors

#### new CategoryTreeContainer (x, y, width, height, textRenderer, parent)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| parent | ICategoryTreeParent |  |



#### Fields

[category](#category)
F


[scroll](#scroll)


[children](#children)


[expandBtn](#expandBtn)


[showBtn](#showBtn)


[isHead](1.9.2/)


[topScroll](1.9.2/)


[btnHeight](1.9.2/)



#### Methods

[addCategory(category)](#addCategory-String[]-)


[selectCategory(category)](#selectCategory-String[]-)


[updateOffsets()](#updateOffsets-)


[init()](#init-)


[onScrollbar(page)](#onScrollbar-double-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .category

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .scroll


##### Type: [Scrollbar](1.9.2/xyz/wagyourtail/wagyourgui/elements/Scrollbar.html)



#### .children


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [CategoryTreeContainer](#)>



#### .expandBtn


##### Type: [Button](1.9.2/xyz/wagyourtail/wagyourgui/elements/Button.html)



#### .showBtn


##### Type: [Button](1.9.2/xyz/wagyourtail/wagyourgui/elements/Button.html)



#### .isHead


##### Type: boolean



#### .topScroll


##### Type: int



#### .btnHeight


##### Type: int



### Methods

#### .addCategory(category)

| Parameter | Type | Description |
|---|---|---|
| category | String[] |  |

##### Returns: [CategoryTreeContainer](#)



#### .selectCategory(category)

| Parameter | Type | Description |
|---|---|---|
| category | String[] |  |

##### Returns: void



#### .updateOffsets()


##### Returns: void



#### .init()


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




