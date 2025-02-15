

xyz.wagyourtail.jsmacros.client.api.helpers.InteractionManagerHelper
--------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[ClientPlayerInteractionManager](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/network/ClientPlayerInteractionManager)>

1.9.0

Helper for ClientPlayerInteractionManager
it accesses interaction manager from `mc` instead of `base`, to avoid issues

### Constructors

#### new InteractionManagerHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | ClientPlayerInteractionManager |  |



#### Fields

[autoUpdateBase](1.9.2/)



#### Methods

[checkBase(update)](#checkBase-boolean-)


[getGameMode()](#getGameMode-)


[setGameMode(gameMode)](#setGameMode-String-)


[setTarget(x, y, z)](#setTarget-int-int-int-)


[setTarget(x, y, z, direction)](#setTarget-int-int-int-String-)


[setTarget(x, y, z, direction)](#setTarget-int-int-int-int-)


[setTarget(pos)](#setTarget-BlockPosHelper-)


[setTarget(pos, direction)](#setTarget-BlockPosHelper-String-)


[setTarget(pos, direction)](#setTarget-BlockPosHelper-int-)


[setTarget(entity)](#setTarget-EntityHelper-)


[getTarget()](#getTarget-)


[getTargetedBlock()](#getTargetedBlock-)


[getTargetedEntity()](#getTargetedEntity-)


[setTargetMissed()](#setTargetMissed-)


[hasTargetOverride()](#hasTargetOverride-)


[clearTargetOverride()](#clearTargetOverride-)


[setTargetRangeCheck(enabled, autoClear)](#setTargetRangeCheck-boolean-boolean-)


[setTargetAirCheck(enabled, autoClear)](#setTargetAirCheck-boolean-boolean-)


[setTargetShapeCheck(enabled, autoClear)](#setTargetShapeCheck-boolean-boolean-)


[resetTargetChecks()](#resetTargetChecks-)


[attack()](#attack-)


[attack(await)](#attack-boolean-)


[attack(entity)](#attack-EntityHelper-)


[attack(entity, await)](#attack-EntityHelper-boolean-)


[attack(x, y, z, direction)](#attack-int-int-int-String-)


[attack(x, y, z, direction)](#attack-int-int-int-int-)


[attack(x, y, z, direction, await)](#attack-int-int-int-String-boolean-)


[attack(x, y, z, direction, await)](#attack-int-int-int-int-boolean-)


[breakBlock()](#breakBlock-)


[breakBlock(x, y, z)](#breakBlock-int-int-int-)


[breakBlock(pos)](#breakBlock-BlockPosHelper-)


[breakBlockAsync(callback)](#breakBlockAsync-MethodWrapper-)


[isBreakingBlock()](#isBreakingBlock-)


[hasBreakBlockOverride()](#hasBreakBlockOverride-)


[cancelBreakBlock()](#cancelBreakBlock-)


[interact()](#interact-)


[interact(await)](#interact-boolean-)


[interactEntity(entity, offHand)](#interactEntity-EntityHelper-boolean-)


[interactEntity(entity, offHand, await)](#interactEntity-EntityHelper-boolean-boolean-)


[interactItem(offHand)](#interactItem-boolean-)


[interactItem(offHand, await)](#interactItem-boolean-boolean-)


[interactBlock(x, y, z, direction, offHand)](#interactBlock-int-int-int-String-boolean-)


[interactBlock(x, y, z, direction, offHand)](#interactBlock-int-int-int-int-boolean-)


[interactBlock(x, y, z, direction, offHand, await)](#interactBlock-int-int-int-String-boolean-boolean-)


[interactBlock(x, y, z, direction, offHand, await)](#interactBlock-int-int-int-int-boolean-boolean-)


[holdInteract(holding)](#holdInteract-boolean-)


[holdInteract(holding, awaitFirstClick)](#holdInteract-boolean-boolean-)


[holdInteract(ticks)](#holdInteract-int-)


[holdInteract(ticks, stopOnPause)](#holdInteract-int-boolean-)


[hasInteractOverride()](#hasInteractOverride-)



### Fields

#### .autoUpdateBase

indicates if the helper should auto update the base manager, default is true  

when the base doesn't equal to the current manager,  

if this is false, raise an error;  

else if base is updated, the method works as usual;  

else if the method don't need manager or network interaction, work as usual with old manager;  

else the method does nothing


##### Type: boolean



### Methods

#### .checkBase(update)

checks if the base matches the current manager

| Parameter | Type | Description |
|---|---|---|
| update | boolean | true if the base should be updated. otherwise it'll raise an error if it's not up-to-date |

##### Returns: boolean

true if base is available



#### .getGameMode()

1.9.0


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the player's current gamemode.



#### .setGameMode(gameMode)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| gameMode | String | possible values are survival, creative, adventure, spectator (case insensitive) |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(x, y, z)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(x, y, z, direction)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | String |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(x, y, z, direction)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | int |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(pos)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(pos, direction)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |
| direction | String |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(pos, direction)

1.9.0

sets crosshair target to a block

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |
| direction | int |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTarget(entity)

1.9.0

sets crosshair target to an entity

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .getTarget()

1.9.1


##### Returns: [HitResultHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/HitResultHelper.html)< ? >

current hitResult



#### .getTargetedBlock()

1.9.0


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

targeted block pos, null if not targeting block



#### .getTargetedEntity()

1.9.0


##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

targeted entity, null if not targeting entity



#### .setTargetMissed()

1.9.0

sets crosshair target to missed (doesn't target anything)


##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .hasTargetOverride()

1.9.0


##### Returns: boolean

`true` if target have been set by `ClientPlayerEntityHelper#setTarget()` or
`ClientPlayerEntityHelper#setTargetMissed()`



#### .clearTargetOverride()

1.9.0

clears target override


##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTargetRangeCheck(enabled, autoClear)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| enabled | boolean | if target overriding should check range. default is true |
| autoClear | boolean | if override should clear when out of range.
                                          if false, target will set to missed if out of range. default is true |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTargetAirCheck(enabled, autoClear)

1.9.0

| Parameter | Type | Description |
|---|---|---|
| enabled | boolean | if target overriding should check air. default is false |
| autoClear | boolean | if override should clear when is air.
                                          if false, target will set to missed if is air. default is false |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .setTargetShapeCheck(enabled, autoClear)

1.9.0

this check ignores air. use `ClientPlayerEntityHelper#setTargetAirCheck()` to check air.

| Parameter | Type | Description |
|---|---|---|
| enabled | boolean | if target overriding should check block shape. default is true |
| autoClear | boolean | if override should clear when shape is empty.
                                          if false, target will set to missed if is empty. default is false |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .resetTargetChecks()

1.9.0

resets all range, air and shape check settings to default.


##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .attack()

1.5.0


##### Returns: [InteractionManagerHelper](#)



#### .attack(await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .attack(entity)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |

##### Returns: [InteractionManagerHelper](#)



#### .attack(entity, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .attack(x, y, z, direction)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate to attack |
| y | int | the y coordinate to attack |
| z | int | the z coordinate to attack |
| direction | String | possible values are "up", "down", "north", "south", "east", "west" |

##### Returns: [InteractionManagerHelper](#)

self for chaining.



#### .attack(x, y, z, direction)

1.5.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | int | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |

##### Returns: [InteractionManagerHelper](#)



#### .attack(x, y, z, direction, await)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate to attack |
| y | int | the y coordinate to attack |
| z | int | the z coordinate to attack |
| direction | String | possible values are "up", "down", "north", "south", "east", "west" |
| await | boolean | whether to wait for the attack to finish |

##### Returns: [InteractionManagerHelper](#)

self for chaining.



#### .attack(x, y, z, direction, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | int | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .breakBlock()

1.9.0

breaks a block, will wait till it's done  

you can use `ClientPlayerEntityHelper#setTarget()` to specify which block to break


##### Returns: [InteractionProxy$Break$BreakBlockResult](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/InteractionProxy.Break.BreakBlockResult.html)

result, or null if interaction manager is unavailable



#### .breakBlock(x, y, z)

1.9.0

breaks a block, will wait till it's done  

this is the same as:

```
                 setTarget(x, y, z);
                 let res = null;
                 if (getTargetedBlock()?.getRaw().equals(new BlockPos(x, y, z))) res = breakBlock();
                 clearTargetOverride();
                 return res;
                 
```
| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |

##### Returns: [InteractionProxy$Break$BreakBlockResult](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/InteractionProxy.Break.BreakBlockResult.html)

result



#### .breakBlock(pos)

1.9.0

breaks a block, will wait till it's done  

this is the same as:

```
                 setTarget(pos);
                 let res = null;
                 if (getTargetedBlock()?.equals(pos)) res = breakBlock();
                 clearTargetOverride();
                 return res;
                 
```
| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper |  |

##### Returns: [InteractionProxy$Break$BreakBlockResult](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/InteractionProxy.Break.BreakBlockResult.html)

result



#### .breakBlockAsync(callback)

1.9.0

starts breaking a block  

you can use `ClientPlayerEntityHelper#setTarget()` to specify which block to break

| Parameter | Type | Description |
|---|---|---|
| callback | MethodWrapper<InteractionProxy$Break$BreakBlockResult, Object, ?, ?> | this will mostly be called on main thread!
                                         Use methodToJavaAsync() instead of methodToJava() to avoid errors. |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .isBreakingBlock()

1.8.0


##### Returns: boolean



#### .hasBreakBlockOverride()

1.9.0


##### Returns: boolean

`true` if there's not finished block breaking from `ClientPlayerEntityHelper#breakBlock()`



#### .cancelBreakBlock()

1.9.0

cancels breaking block that previously started by `ClientPlayerEntityHelper#breakBlock()` or
`ClientPlayerEntityHelper#breakBlockAsync()`


##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .interact()

1.5.0


##### Returns: [InteractionManagerHelper](#)



#### .interact(await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactEntity(entity, offHand)

1.5.0, renamed from `interact` in 1.6.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| offHand | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactEntity(entity, offHand, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<?> |  |
| offHand | boolean |  |
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactItem(offHand)

1.5.0, renamed from `interact` in 1.6.0

| Parameter | Type | Description |
|---|---|---|
| offHand | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactItem(offHand, await)

1.6.0

| Parameter | Type | Description |
|---|---|---|
| offHand | boolean |  |
| await | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactBlock(x, y, z, direction, offHand)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate to interact |
| y | int | the y coordinate to interact |
| z | int | the z coordinate to interact |
| direction | String | possible values are "up", "down", "north", "south", "east", "west" |
| offHand | boolean |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining.



#### .interactBlock(x, y, z, direction, offHand)

1.5.0, renamed from `interact` in 1.6.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | int | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |
| offHand | boolean |  |

##### Returns: [InteractionManagerHelper](#)



#### .interactBlock(x, y, z, direction, offHand, await)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate to interact |
| y | int | the y coordinate to interact |
| z | int | the z coordinate to interact |
| direction | String | possible values are "up", "down", "north", "south", "east", "west" |
| offHand | boolean |  |
| await | boolean | whether to wait for the interaction to complete |

##### Returns: [InteractionManagerHelper](#)

self for chaining.



#### .interactBlock(x, y, z, direction, offHand, await)

1.5.0, renamed from `interact` in 1.6.0

| Parameter | Type | Description |
|---|---|---|
| x | int |  |
| y | int |  |
| z | int |  |
| direction | int | 0-5 in order: [DOWN, UP, NORTH, SOUTH, WEST, EAST]; |
| offHand | boolean |  |
| await | boolean | whether to wait for the interaction to complete |

##### Returns: [InteractionManagerHelper](#)



#### .holdInteract(holding)

1.9.0

starts/stops long interact

| Parameter | Type | Description |
|---|---|---|
| holding | boolean |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .holdInteract(holding, awaitFirstClick)

1.9.0

starts/stops long interact

| Parameter | Type | Description |
|---|---|---|
| holding | boolean |  |
| awaitFirstClick | boolean |  |

##### Returns: [InteractionManagerHelper](#)

self for chaining



#### .holdInteract(ticks)

1.9.0

interacts for specified number of ticks

| Parameter | Type | Description |
|---|---|---|
| ticks | int |  |

##### Returns: int

remaining ticks if the interaction was interrupted



#### .holdInteract(ticks, stopOnPause)

1.9.0

interacts for specified number of ticks

| Parameter | Type | Description |
|---|---|---|
| ticks | int |  |
| stopOnPause | boolean | if false, this interaction will not return when interrupted by pause.
                                            the timer will not decrease, meaning it'll continue right after unpause and interact exact amount of ticks. |

##### Returns: int

remaining ticks if the interaction was interrupted



#### .hasInteractOverride()

1.9.0


##### Returns: boolean

`true` if interaction from `ClientPlayerEntityHelper#holdInteract()` is active




