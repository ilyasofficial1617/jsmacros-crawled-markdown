

xyz.wagyourtail.jsmacros.client.api.classes.RegistryHelper
----------------------------------------------------------

#### 

1.8.4

### Constructors

#### new RegistryHelper ()




#### Methods

[getItem(id)](#getItem-String-)


[getItemStack(id)](#getItemStack-String-)


[getItemStack(id, nbt)](#getItemStack-String-String-)


[getItemIds()](#getItemIds-)


[getItems()](#getItems-)


[getBlock(id)](#getBlock-String-)


[getBlockState(id)](#getBlockState-String-)


[getStatusEffect(id)](#getStatusEffect-String-)


[getStatusEffects()](#getStatusEffects-)


[getBlockState(id, nbt)](#getBlockState-String-String-)


[getBlockIds()](#getBlockIds-)


[getBlocks()](#getBlocks-)


[getEnchantment(id)](#getEnchantment-String-)


[getEnchantment(id, level)](#getEnchantment-String-int-)


[getEnchantmentIds()](#getEnchantmentIds-)


[getEnchantments()](#getEnchantments-)


[getEntity(type)](#getEntity-String-)


[getRawEntityType(type)](#getRawEntityType-String-)


[getEntityTypeIds()](#getEntityTypeIds-)


[getFluidState(id)](#getFluidState-String-)


[getFeatureIds()](#getFeatureIds-)


[getStructureFeatureIds()](#getStructureFeatureIds-)


[getPaintingIds()](#getPaintingIds-)


[getParticleTypeIds()](#getParticleTypeIds-)


[getGameEventNames()](#getGameEventNames-)


[getStatusEffectIds()](#getStatusEffectIds-)


[getBlockEntityTypeIds()](#getBlockEntityTypeIds-)


[getScreenHandlerIds()](#getScreenHandlerIds-)


[getRecipeTypeIds()](#getRecipeTypeIds-)


[getVillagerTypeIds()](#getVillagerTypeIds-)


[getVillagerProfessionIds()](#getVillagerProfessionIds-)


[getPointOfInterestTypeIds()](#getPointOfInterestTypeIds-)


[getMemoryModuleTypeIds()](#getMemoryModuleTypeIds-)


[getSensorTypeIds()](#getSensorTypeIds-)


[getActivityTypeIds()](#getActivityTypeIds-)


[getStatTypeIds()](#getStatTypeIds-)


[getEntityAttributeIds()](#getEntityAttributeIds-)


[getPotionTypeIds()](#getPotionTypeIds-)


[getIdentifier(identifier)](#getIdentifier-String-)


[parseIdentifier(id)](#parseIdentifier-String-)
S


[parseNameSpace(id)](#parseNameSpace-String-)
S



### Methods

#### .getItem(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the item's id |

##### Returns: [ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html)

an [ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html) for the given item.



#### .getItemStack(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the item's id |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

an [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html) for the given item.



#### .getItemStack(id, nbt)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the item's id |
| nbt | String | the item's nbt |

##### Returns: [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html)

an [ItemStackHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemStackHelper.html) for the given item and nbt data.



#### .getItemIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all registered item ids.



#### .getItems()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[ItemHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/ItemHelper.html)>

a list of all registered items.



#### .getBlock(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the block's id |

##### Returns: [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)

an [BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html) for the given block.



#### .getBlockState(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the block's id |

##### Returns: [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html)

an [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html) for the given block.



#### .getStatusEffect(id)

| Parameter | Type | Description |
|---|---|---|
| id | String | the status effect's id |

##### Returns: [StatusEffectHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatusEffectHelper.html)

an [StatusEffectHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatusEffectHelper.html) for the given status effect with 0 ticks duration.



#### .getStatusEffects()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[StatusEffectHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatusEffectHelper.html)>

a list of all registered status effects as [StatusEffectHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/StatusEffectHelper.html)s with 0 ticks duration.



#### .getBlockState(id, nbt)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the block's id |
| nbt | String | the block's nbt |

##### Returns: [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html)

an [BlockStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockStateHelper.html) for the given block with the specified nbt.



#### .getBlockIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all registered block ids.



#### .getBlocks()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[BlockHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockHelper.html)>

a list of all registered blocks.



#### .getEnchantment(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the enchantment's id |

##### Returns: [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)

an [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html) for the given enchantment.



#### .getEnchantment(id, level)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the enchantment's id |
| level | int | the level of the enchantment |

##### Returns: [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)

an [EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html) for the given enchantment with the specified level.



#### .getEnchantmentIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all registered enchantment ids.



#### .getEnchantments()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[EnchantmentHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/inventory/EnchantmentHelper.html)>

a list of all registered enchantments.



#### .getEntity(type)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| type | String | the id of the entity's type |

##### Returns: [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html)< ? >

an [EntityHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/entity/EntityHelper.html) for the given entity.



#### .getRawEntityType(type)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| type | String | the id of the entity's type |

##### Returns: [EntityType](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/EntityType)< ? >

an [EntityType](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/entity/EntityType) for the given entity.



#### .getEntityTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all entity type ids.



#### .getFluidState(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the fluid's id |

##### Returns: [FluidStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/FluidStateHelper.html)

an [FluidStateHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/FluidStateHelper.html) for the given fluid.



#### .getFeatureIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all feature ids.



#### .getStructureFeatureIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all structure feature ids.



#### .getPaintingIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all painting motive ids.



#### .getParticleTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all particle type ids.



#### .getGameEventNames()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all game event names.



#### .getStatusEffectIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all status effect ids.



#### .getBlockEntityTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all block entity type ids.



#### .getScreenHandlerIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all screen handler ids.



#### .getRecipeTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all recipe type ids.



#### .getVillagerTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all villager type ids.



#### .getVillagerProfessionIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all villager profession ids.



#### .getPointOfInterestTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all point of interest type ids.



#### .getMemoryModuleTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all memory module type ids.



#### .getSensorTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all villager sensor type ids.



#### .getActivityTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all villager activity type ids.



#### .getStatTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all stat type ids.



#### .getEntityAttributeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all entity attribute ids.



#### .getPotionTypeIds()

1.8.4


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all potion type ids.



#### .getIdentifier(identifier)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| identifier | String | the String representation of the identifier, with the namespace and path |

##### Returns: [Identifier](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/Identifier)

the raw minecraft Identifier.



#### .parseIdentifier(id)

Static
| Parameter | Type | Description |
|---|---|---|
| id | String |  |

##### Returns: [Identifier](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/Identifier)



#### .parseNameSpace(id)

Static
| Parameter | Type | Description |
|---|---|---|
| id | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




