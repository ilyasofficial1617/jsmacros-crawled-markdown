

xyz.wagyourtail.jsmacros.client.api.classes.PlayerInput
-------------------------------------------------------

#### 

1.4.0

An object, that combines all possible player inputs

### Constructors

#### new PlayerInput ()

1.4.0

Creates a new `PlayerInput` Object with all values set either to 0 or false



#### new PlayerInput (movementForward, movementSideways, yaw)

1.4.0

Creates a new `PlayerInput` Object with all other values set either to 0 or false

| Parameter | Type | Description |
|---|---|---|
| movementForward | float | 1 = forward input (W); 0 = no input; -1 = backward input (S) |
| movementSideways | float | 1 = left input (A); 0 = no input; -1 = right input (D) |
| yaw | float | yaw of the player |


#### new PlayerInput (movementForward, yaw, jumping, sprinting)

1.4.0

Creates a new `PlayerInput` Object with all other values set either to 0 or false

| Parameter | Type | Description |
|---|---|---|
| movementForward | float | 1 = forward input (W); 0 = no input; -1 = backward input (S) |
| yaw | float | yaw of the player |
| jumping | boolean | jump input |
| sprinting | boolean | sprint input |


#### new PlayerInput (input, yaw, pitch, sprinting)

1.4.0

Creates a new `PlayerInput` Object from a minecraft input with the missing values extra

| Parameter | Type | Description |
|---|---|---|
| input | Input | Minecraft Input to be converted. |
| yaw | float | yaw of the player |
| pitch | float | pitch of the player |
| sprinting | boolean | sprint input |


#### new PlayerInput (movementForward, movementSideways, yaw, pitch, jumping, sneaking, sprinting)

1.4.0

Creates a new `PlayerInput` Object with all double values converted to floats

| Parameter | Type | Description |
|---|---|---|
| movementForward | double | 1 = forward input (W); 0 = no input; -1 = backward input (S) |
| movementSideways | double | 1 = left input (A); 0 = no input; -1 = right input (D) |
| yaw | double | yaw of the player |
| pitch | double | pitch of the player |
| jumping | boolean | jump input |
| sneaking | boolean | sneak input |
| sprinting | boolean | sprint input |


#### new PlayerInput (movementForward, movementSideways, yaw, pitch, jumping, sneaking, sprinting)

1.4.0

Creates a new `PlayerInput` Object

| Parameter | Type | Description |
|---|---|---|
| movementForward | float | 1 = forward input (W); 0 = no input; -1 = backward input (S) |
| movementSideways | float | 1 = left input (A); 0 = no input; -1 = right input (D) |
| yaw | float | yaw of the player |
| pitch | float | pitch of the player |
| jumping | boolean | jump input |
| sneaking | boolean | sneak input |
| sprinting | boolean | sprint input |


#### new PlayerInput (input)

1.4.0

Creates a clone `PlayerInput` Object

| Parameter | Type | Description |
|---|---|---|
| input | PlayerInput | the PlayerInput object to be cloned |



#### Fields

[movementForward](1.9.2/)


[movementSideways](1.9.2/)


[yaw](1.9.2/)


[pitch](1.9.2/)


[jumping](1.9.2/)


[sneaking](1.9.2/)


[sprinting](1.9.2/)



#### Methods

[fromCsv(csv)](#fromCsv-String-)
S


[fromJson(json)](#fromJson-String-)
S


[toString(varNames)](#toString-boolean-)


[toString()](#toString-)


[clone()](#clone-)



### Fields

#### .movementForward


##### Type: float



#### .movementSideways


##### Type: float



#### .yaw


##### Type: float



#### .pitch


##### Type: float



#### .jumping


##### Type: boolean



#### .sneaking


##### Type: boolean



#### .sprinting


##### Type: boolean



### Methods

#### .fromCsv(csv)

Static

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

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[PlayerInput](#)>

`List` Each row parsed as a `PlayerInput`



#### .fromJson(json)

Static

1.4.0

Parses a JSON string into a `PlayerInput` Object  

Capitalization of the keys matters.

| Parameter | Type | Description |
|---|---|---|
| json | String | JSON string to be parsed |

##### Returns: [PlayerInput](#)

The JSON parsed into a `PlayerInput`



#### .toString(varNames)

1.4.0

Converts the current object into a string.
This can be used to convert current inputs created using `Player.getCurrentPlayerInput()`
to either JSON or CSV.

The output can be converted into a PlayerInput object again by using either
`fromCsv(String, String)` or `fromJson(String)`.

| Parameter | Type | Description |
|---|---|---|
| varNames | boolean | whether to include variable Names(=JSON) or not(=CSV) |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

The `PlayerInput` object as a string



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .clone()


##### Returns: [PlayerInput](#)




