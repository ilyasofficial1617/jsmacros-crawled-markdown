

xyz.wagyourtail.jsmacros.client.gui.overlays.FileChooser
--------------------------------------------------------

#### extends [OverlayContainer](1.9.2/xyz/wagyourtail/wagyourgui/overlays/OverlayContainer.html)

### Constructors

#### new FileChooser (x, y, width, height, textRenderer, directory, selected, parent, setFile, editFile)

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| width | int |  |
| height | int |  |
| textRenderer | TextRenderer |  |
| directory | File |  |
| selected | File |  |
| parent | IOverlayParent |  |
| setFile | Consumer<File> |  |
| editFile | Consumer<File> |  |



#### Fields

[root](#root)



#### Methods

[setDir(dir)](#setDir-File-)


[selectFile(f)](#selectFile-File-)


[init()](#init-)


[addFile(f)](#addFile-File-)


[addFile(f, btnText)](#addFile-File-String-)


[updateFilePos()](#updateFilePos-)


[confirmDelete(f)](#confirmDelete-FileChooser$fileObj-)


[delete(f)](#delete-FileChooser$fileObj-)


[onScrollbar(page)](#onScrollbar-double-)


[render(drawContext, mouseX, mouseY, delta)](#render-DrawContext-int-int-float-)



### Fields

#### .root


##### Type: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)



### Methods

#### .setDir(dir)

| Parameter | Type | Description |
|---|---|---|
| dir | File |  |

##### Returns: void



#### .selectFile(f)

| Parameter | Type | Description |
|---|---|---|
| f | File |  |

##### Returns: void



#### .init()


##### Returns: void



#### .addFile(f)

| Parameter | Type | Description |
|---|---|---|
| f | File |  |

##### Returns: void



#### .addFile(f, btnText)

| Parameter | Type | Description |
|---|---|---|
| f | File |  |
| btnText | String |  |

##### Returns: void



#### .updateFilePos()


##### Returns: void



#### .confirmDelete(f)

| Parameter | Type | Description |
|---|---|---|
| f | FileChooser$fileObj |  |

##### Returns: void



#### .delete(f)

| Parameter | Type | Description |
|---|---|---|
| f | FileChooser$fileObj |  |

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




