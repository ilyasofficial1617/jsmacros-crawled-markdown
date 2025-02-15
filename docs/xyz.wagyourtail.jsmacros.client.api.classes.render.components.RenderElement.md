
[Surface](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components3d/Surface.html) [Draw2DElement](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Draw2DElement.html) [Rect](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Rect.html) [Line](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Line.html) [Item](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Item.html) [Image](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Image.html) [Text](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/render/components/Text.html) [ButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ButtonWidgetHelper.html)<

T

 **extends** 

[ButtonWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ButtonWidget)> [CyclingButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CyclingButtonWidgetHelper.html)<

T

> [SliderWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/SliderWidgetHelper.html) [CheckBoxWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/CheckBoxWidgetHelper.html) [TextFieldWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/TextFieldWidgetHelper.html) [LockButtonWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/LockButtonWidgetHelper.html) [ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)<

B

 **extends** 

[ClickableWidgetHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ClickableWidgetHelper.html)<

B

, 

T

 **extends** 

[ClickableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ClickableWidget)>, 

T

 **extends** 

[ClickableWidget](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/widget/ClickableWidget)>

xyz.wagyourtail.jsmacros.client.api.classes.render.components.RenderElement
---------------------------------------------------------------------------

Interface
#### implements [Drawable](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/gui/Drawable)

#### Fields

[mc](#mc)
S
F



#### Methods

[getZIndex()](#getZIndex-)


[render3D(drawContext, mouseX, mouseY, delta)](#render3D-DrawContext-int-int-float-)


[setupMatrix(matrices, x, y, scale, rotation)](#setupMatrix-MatrixStack-double-double-float-float-)


[setupMatrix(matrices, x, y, scale, rotation, width, height, rotateAroundCenter)](#setupMatrix-MatrixStack-double-double-float-float-double-double-boolean-)



### Fields

#### .mc

Static
Final

##### Type: [MinecraftClient](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/MinecraftClient)



### Methods

#### .getZIndex()


##### Returns: int



#### .render3D(drawContext, mouseX, mouseY, delta)

| Parameter | Type | Description |
|---|---|---|
| drawContext | DrawContext |  |
| mouseX | int |  |
| mouseY | int |  |
| delta | float |  |

##### Returns: void



#### .setupMatrix(matrices, x, y, scale, rotation)

| Parameter | Type | Description |
|---|---|---|
| matrices | MatrixStack |  |
| x | double |  |
| y | double |  |
| scale | float |  |
| rotation | float |  |

##### Returns: void



#### .setupMatrix(matrices, x, y, scale, rotation, width, height, rotateAroundCenter)

| Parameter | Type | Description |
|---|---|---|
| matrices | MatrixStack |  |
| x | double |  |
| y | double |  |
| scale | float |  |
| rotation | float |  |
| width | double |  |
| height | double |  |
| rotateAroundCenter | boolean |  |

##### Returns: void




