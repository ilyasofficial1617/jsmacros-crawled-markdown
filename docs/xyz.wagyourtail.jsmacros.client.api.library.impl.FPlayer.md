

xyz.wagyourtail.jsmacros.client.api.library.impl.FPlayer
--------------------------------------------------------

#### extends [BaseLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/BaseLibrary.html)

Functions for getting and modifying the player's state.

An instance of this class is passed to scripts as the `Player` variable.

#### Methods

[openInventory()](#openInventory-)


[getPlayer()](#getPlayer-)


[getInteractionManager()](#getInteractionManager-)


[interactions()](#interactions-)


[getGameMode()](#getGameMode-)


[setGameMode(gameMode)](#setGameMode-String-)


[rayTraceBlock(distance, fluid)](#rayTraceBlock-double-boolean-)


[detailedRayTraceBlock(distance, fluid)](#detailedRayTraceBlock-double-boolean-)


[rayTraceEntity()](#rayTraceEntity-)
D


[rayTraceEntity(distance)](#rayTraceEntity-int-)


[writeSign(l1, l2, l3, l4)](#writeSign-String-String-String-String-)


[takeScreenshot(folder, callback)](#takeScreenshot-String-MethodWrapper-)


[takeScreenshot(folder, file, callback)](#takeScreenshot-String-String-MethodWrapper-)


[takePanorama(folder, width, height, callback)](#takePanorama-String-int-int-MethodWrapper-)


[getStatistics()](#getStatistics-)


[getReach()](#getReach-)


[createPlayerInput()](#createPlayerInput-)


[createPlayerInput(movementForward, movementSideways, yaw)](#createPlayerInput-double-double-double-)


[createPlayerInput(movementForward, yaw, jumping, sprinting)](#createPlayerInput-double-double-boolean-boolean-)


[createPlayerInput(movementForward, movementSideways, yaw, pitch, jumping, sneaking, sprinting)](#createPlayerInput-double-double-double-double-boolean-boolean-boolean-)


[createPlayerInputsFromCsv(csv)](#createPlayerInputsFromCsv-String-)


[createPlayerInputsFromJson(json)](#createPlayerInputsFromJson-String-)


[getCurrentPlayerInput()](#getCurrentPlayerInput-)


[addInput(input)](#addInput-PlayerInput-)


[addInputs(inputs)](#addInputs-PlayerInput[]-)


[clearInputs()](#clearInputs-)


[setDrawPredictions(val)](#setDrawPredictions-boolean-)


[predictInput(input)](#predictInput-PlayerInput-)


[predictInput(input, draw)](#predictInput-PlayerInput-boolean-)


[predictInputs(inputs)](#predictInputs-PlayerInput[]-)


[isBreakingBlock()](#isBreakingBlock-)
D


[predictInputs(inputs, draw)](#predictInputs-PlayerInput[]-boolean-)


[moveForward(yaw)](#moveForward-double-)


[moveBackward(yaw)](#moveBackward-double-)


[moveStrafeLeft(yaw)](#moveStrafeLeft-double-)


[moveStrafeRight(yaw)](#moveStrafeRight-double-)



### Methods

#### .openInventory()


##### Returns: [Inventory](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/inventory/Inventory.html)< ? >

the Inventory handler



#### .getPlayer()

1.0.3


##### Returns: [ClientPlayerEntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/ClientPlayerEntityHelper.html)<[ClientPlayerEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/client/network/ClientPlayerEntity)>

the player entity wrapper.



#### .getInteractionManager()

1.9.0


##### Returns: [InteractionManagerHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/InteractionManagerHelper.html)



#### .interactions()

1.9.0

alias for [FPlayer#getInteractionManager()](#getInteractionManager-)


##### Returns: [InteractionManagerHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/InteractionManagerHelper.html)



#### .getGameMode()

1.0.9


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the player's current gamemode.



#### .setGameMode(gameMode)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| gameMode | String | possible values are survival, creative, adventure, spectator (case insensitive) |

##### Returns: void



#### .rayTraceBlock(distance, fluid)

1.0.5

| Parameter | Type | Description |
|---|---|---|
| distance | double |  |
| fluid | boolean |  |

##### Returns: [BlockDataHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockDataHelper.html)

the block/liquid the player is currently looking at.



#### .detailedRayTraceBlock(distance, fluid)

1.9.1

| Parameter | Type | Description |
|---|---|---|
| distance | double |  |
| fluid | boolean |  |

##### Returns: [HitResultHelper$Block](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/HitResultHelper.Block.html)

the raycast result.



#### .rayTraceEntity()

Deprecated

1.0.5


##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

the entity the camera is currently looking at. can be affected by [InteractionManagerHelper#setTarget(xyz.wagyourtail.jsmacros.client.api.helpers.world.entity.EntityHelper)](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/InteractionManagerHelper.html#setTarget-EntityHelper-)



#### .rayTraceEntity(distance)

1.8.3

| Parameter | Type | Description |
|---|---|---|
| distance | int |  |

##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

entity the player entity is currently looking at (if any).



#### .writeSign(l1, l2, l3, l4)

1.2.2

Write to a sign screen if a sign screen is currently open.

| Parameter | Type | Description |
|---|---|---|
| l1 | String |  |
| l2 | String |  |
| l3 | String |  |
| l4 | String |  |

##### Returns: boolean

of success.



#### .takeScreenshot(folder, callback)

1.2.6

| Parameter | Type | Description |
|---|---|---|
| folder | String |  |
| callback | MethodWrapper<TextHelper, Object, Object, ?> | calls your method as a Consumer<TextHelper> |

##### Returns: void



#### .takeScreenshot(folder, file, callback)

1.2.6

Take a screenshot and save to a file.

`file` is the optional one, typescript doesn't like it not being the last one that's optional

| Parameter | Type | Description |
|---|---|---|
| folder | String |  |
| file | String |  |
| callback | MethodWrapper<TextHelper, Object, Object, ?> | calls your method as a Consumer<TextHelper> |

##### Returns: void



#### .takePanorama(folder, width, height, callback)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| folder | String | the folder to save the screenshot to, relative to the macro folder |
| width | int | the width of the panorama |
| height | int | the height of the panorama |
| callback | MethodWrapper<TextHelper, Object, Object, ?> | calls your method as a Consumer<TextHelper> |

##### Returns: void



#### .getStatistics()


##### Returns: [StatsHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatsHelper.html)



#### .getReach()

1.8.4


##### Returns: double

the current reach distance of the player.



#### .createPlayerInput()

1.4.0

Creates a new PlayerInput object.


##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)



#### .createPlayerInput(movementForward, movementSideways, yaw)

1.4.0

Creates a new PlayerInput object.

| Parameter | Type | Description |
|---|---|---|
| movementForward | double |  |
| movementSideways | double |  |
| yaw | double |  |

##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)



#### .createPlayerInput(movementForward, yaw, jumping, sprinting)

1.4.0

Creates a new PlayerInput object.

| Parameter | Type | Description |
|---|---|---|
| movementForward | double |  |
| yaw | double |  |
| jumping | boolean |  |
| sprinting | boolean |  |

##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)



#### .createPlayerInput(movementForward, movementSideways, yaw, pitch, jumping, sneaking, sprinting)

1.4.0

Creates a new PlayerInput object.

| Parameter | Type | Description |
|---|---|---|
| movementForward | double | 1 = forward input (W); 0 = no input; -1 = backward input (S) |
| movementSideways | double | 1 = left input (A); 0 = no input; -1 = right input (D) |
| yaw | double | yaw of the player |
| pitch | double | pitch of the player |
| jumping | boolean | jump input |
| sneaking | boolean | sneak input |
| sprinting | boolean | sprint input |

##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)



#### .createPlayerInputsFromCsv(csv)

1.4.0

Parses each row of CSV string into a `PlayerInput`.
The capitalization of the header matters.  

About the columns:

* `movementForward` and `movementSideways` as a number
* `yaw` and `pitch` as an absolute number
* `jumping`, `sneaking` and `sprinting` have to be boolean

The separation must be a "," it's a csv...(but spaces don't matter)  

Quoted values don't work

| Parameter | Type | Description |
|---|---|---|
| csv | String | CSV string to be parsed |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)>



#### .createPlayerInputsFromJson(json)

1.4.0

Parses a JSON string into a `PlayerInput` Object.
For details see `PlayerInput.fromCsv()`, on what has to be present.  

Capitalization of the keys matters.

| Parameter | Type | Description |
|---|---|---|
| json | String | JSON string to be parsed |

##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)

The JSON parsed into a `PlayerInput`



#### .getCurrentPlayerInput()

1.4.0

Creates a new `PlayerInput` object with the current inputs of the player.


##### Returns: [PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)



#### .addInput(input)

1.4.0

Adds a new `PlayerInput` to `MovementQueue` to be executed

| Parameter | Type | Description |
|---|---|---|
| input | PlayerInput | the PlayerInput to be executed |

##### Returns: void



#### .addInputs(inputs)

1.4.0

Adds multiple new `PlayerInput` to `MovementQueue` to be executed

| Parameter | Type | Description |
|---|---|---|
| inputs | PlayerInput[] | the PlayerInputs to be executed |

##### Returns: void



#### .clearInputs()

1.4.0

Clears all inputs in the `MovementQueue`


##### Returns: void



#### .setDrawPredictions(val)

| Parameter | Type | Description |
|---|---|---|
| val | boolean |  |

##### Returns: void



#### .predictInput(input)

1.4.0

Predicts where one tick with a `PlayerInput` as input would lead to.

| Parameter | Type | Description |
|---|---|---|
| input | PlayerInput | the PlayerInput for the prediction |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the position after the input



#### .predictInput(input, draw)

1.4.0

Predicts where one tick with a `PlayerInput` as input would lead to.

| Parameter | Type | Description |
|---|---|---|
| input | PlayerInput | the PlayerInput for the prediction |
| draw | boolean | whether to visualize the result or not |

##### Returns: [Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)

the position after the input



#### .predictInputs(inputs)

1.4.0

Predicts where each `PlayerInput` executed in a row would lead
without drawing it.

| Parameter | Type | Description |
|---|---|---|
| inputs | PlayerInput[] | the PlayerInputs for each tick for the prediction |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>

the position after each input



#### .isBreakingBlock()

Deprecated

1.8.0


##### Returns: boolean



#### .predictInputs(inputs, draw)

1.4.0

Predicts where each `PlayerInput` executed in a row would lead

| Parameter | Type | Description |
|---|---|---|
| inputs | PlayerInput[] | the PlayerInputs for each tick for the prediction |
| draw | boolean | whether to visualize the result or not |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Pos3D](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/math/Pos3D.html)>

the position after each input



#### .moveForward(yaw)

1.4.0

Adds a forward movement with a relative yaw value to the MovementQueue.

| Parameter | Type | Description |
|---|---|---|
| yaw | double | the relative yaw for the player |

##### Returns: void



#### .moveBackward(yaw)

1.4.0

Adds a backward movement with a relative yaw value to the MovementQueue.

| Parameter | Type | Description |
|---|---|---|
| yaw | double | the relative yaw for the player |

##### Returns: void



#### .moveStrafeLeft(yaw)

1.4.2

Adds sideways movement with a relative yaw value to the MovementQueue.

| Parameter | Type | Description |
|---|---|---|
| yaw | double | the relative yaw for the player |

##### Returns: void



#### .moveStrafeRight(yaw)

1.4.2

Adds sideways movement with a relative yaw value to the MovementQueue.

| Parameter | Type | Description |
|---|---|---|
| yaw | double | the relative yaw for the player |

##### Returns: void




