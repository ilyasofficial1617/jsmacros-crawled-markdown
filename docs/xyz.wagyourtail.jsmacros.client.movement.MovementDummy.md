

xyz.wagyourtail.jsmacros.client.movement.MovementDummy
------------------------------------------------------

#### extends [LivingEntity](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/LivingEntity)

### Constructors

#### new MovementDummy (player)

| Parameter | Type | Description |
|---|---|---|
| player | MovementDummy |  |


#### new MovementDummy (player)

| Parameter | Type | Description |
|---|---|---|
| player | ClientPlayerEntity |  |


#### new MovementDummy (world, pos, velocity, hitBox, onGround, isSprinting, isSneaking)

| Parameter | Type | Description |
|---|---|---|
| world | World |  |
| pos | Vec3d |  |
| velocity | Vec3d |  |
| hitBox | Box |  |
| onGround | boolean |  |
| isSprinting | boolean |  |
| isSneaking | boolean |  |



#### Methods

[getCoordsHistory()](#getCoordsHistory-)


[getInputs()](#getInputs-)


[applyInput(input)](#applyInput-PlayerInput-)


[applyMovementInput(movementInput, f)](#applyMovementInput-Vec3d-float-)


[canMoveVoluntarily()](#canMoveVoluntarily-)


[setSprinting(sprinting)](#setSprinting-boolean-)


[getMainHandStack()](#getMainHandStack-)


[getArmorItems()](#getArmorItems-)


[getEquippedStack(slot)](#getEquippedStack-EquipmentSlot-)


[equipStack(slot, stack)](#equipStack-EquipmentSlot-ItemStack-)


[getMainArm()](#getMainArm-)


[clone()](#clone-)



### Methods

#### .getCoordsHistory()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[Vec3d](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/Vec3d)>



#### .getInputs()


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[PlayerInput](1.9.2/xyz/wagyourtail/jsmacros/client/api/classes/PlayerInput.html)>



#### .applyInput(input)

| Parameter | Type | Description |
|---|---|---|
| input | PlayerInput |  |

##### Returns: [Vec3d](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/Vec3d)



#### .applyMovementInput(movementInput, f)

We have to do this "inject" since the the applyClimbingSpeed() method
in LivingEntity is checking if we are a PlayerEntity, we want to apply the outcome of this check,
so this is why we need to set the y-velocity to 0.

| Parameter | Type | Description |
|---|---|---|
| movementInput | Vec3d |  |
| f | float |  |

##### Returns: [Vec3d](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/math/Vec3d)



#### .canMoveVoluntarily()


##### Returns: boolean



#### .setSprinting(sprinting)

| Parameter | Type | Description |
|---|---|---|
| sprinting | boolean |  |

##### Returns: void



#### .getMainHandStack()


##### Returns: [ItemStack](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/ItemStack)



#### .getArmorItems()


##### Returns: [Iterable](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Iterable.html)<[ItemStack](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/ItemStack)>



#### .getEquippedStack(slot)

| Parameter | Type | Description |
|---|---|---|
| slot | EquipmentSlot |  |

##### Returns: [ItemStack](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/item/ItemStack)



#### .equipStack(slot, stack)

| Parameter | Type | Description |
|---|---|---|
| slot | EquipmentSlot |  |
| stack | ItemStack |  |

##### Returns: void



#### .getMainArm()


##### Returns: [Arm](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/Arm)



#### .clone()


##### Returns: [MovementDummy](#)




