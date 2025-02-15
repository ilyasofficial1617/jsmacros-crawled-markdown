

xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.specialized.passive.SheepEntityHelper
----------------------------------------------------------------------------------------------

#### extends [AnimalEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/specialized/passive/AnimalEntityHelper.html)<[SheepEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/passive/SheepEntity)>

1.8.4

### Constructors

#### new SheepEntityHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | SheepEntity |  |



#### Methods

[isSheared()](#isSheared-)


[isShearable()](#isShearable-)


[getColor()](#getColor-)


[isJeb()](#isJeb-)



### Methods

#### .isSheared()

1.8.4


##### Returns: boolean

`true` if this sheep is sheared, `false` otherwise.



#### .isShearable()

1.8.4


##### Returns: boolean

`true` if this sheep can be sheared, `false` otherwise.



#### .getColor()

1.8.4


##### Returns: [DyeColorHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/DyeColorHelper.html)

the color of this sheep.



#### .isJeb()

1.8.4

Sheep named `jeb_` will cycle through all colors when rendered. If sheared, they will
drop their original colored wool.


##### Returns: boolean

`true` if the sheep has a rainbow overlay, `false` otherwise.




