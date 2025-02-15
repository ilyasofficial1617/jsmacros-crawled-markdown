

xyz.wagyourtail.jsmacros.client.mixins.events.MixinClientPlayerInteractionManager
---------------------------------------------------------------------------------

#### 

### Constructors

#### new MixinClientPlayerInteractionManager ()




#### Methods

[onInteractBlock(player, hand, hitResult, cir)](#onInteractBlock-ClientPlayerEntity-Hand-BlockHitResult-CallbackInfoReturnable-)


[onAttackBlock(pos, direction, cir)](#onAttackBlock-BlockPos-Direction-CallbackInfoReturnable-)


[onAttackEntity(player, target, ci)](#onAttackEntity-PlayerEntity-Entity-CallbackInfo-)


[onInteractEntity(player, entity, hand, cir)](#onInteractEntity-PlayerEntity-Entity-Hand-CallbackInfoReturnable-)



### Methods

#### .onInteractBlock(player, hand, hitResult, cir)

| Parameter | Type | Description |
|---|---|---|
| player | ClientPlayerEntity |  |
| hand | Hand |  |
| hitResult | BlockHitResult |  |
| cir | CallbackInfoReturnable<ActionResult> |  |

##### Returns: void



#### .onAttackBlock(pos, direction, cir)

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPos |  |
| direction | Direction |  |
| cir | CallbackInfoReturnable<Boolean> |  |

##### Returns: void



#### .onAttackEntity(player, target, ci)

| Parameter | Type | Description |
|---|---|---|
| player | PlayerEntity |  |
| target | Entity |  |
| ci | CallbackInfo |  |

##### Returns: void



#### .onInteractEntity(player, entity, hand, cir)

| Parameter | Type | Description |
|---|---|---|
| player | PlayerEntity |  |
| entity | Entity |  |
| hand | Hand |  |
| cir | CallbackInfoReturnable<ActionResult> |  |

##### Returns: void




