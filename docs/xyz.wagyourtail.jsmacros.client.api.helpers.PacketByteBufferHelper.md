

xyz.wagyourtail.jsmacros.client.api.helpers.PacketByteBufferHelper
------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[PacketByteBuf](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/PacketByteBuf)>

1.8.4

### Constructors

#### new PacketByteBufferHelper ()



#### new PacketByteBufferHelper (base)

| Parameter | Type | Description |
|---|---|---|
| base | PacketByteBuf |  |


#### new PacketByteBufferHelper (packet)

| Parameter | Type | Description |
|---|---|---|
| packet | Packet<?> |  |



#### Fields

[BUFFER\_TO\_PACKET](#BUFFER_TO_PACKET)
S
F



#### Methods

[toPacket()](#toPacket-)


[toPacket(packetName)](#toPacket-String-)


[toPacket(clazz)](#toPacket-Class-)


[getPacketId(packetClass)](#getPacketId-Class-)


[getNetworkStateId(packetClass)](#getNetworkStateId-Class-)


[isClientbound(packetClass)](#isClientbound-Class-)


[isServerbound(packetClass)](#isServerbound-Class-)


[sendPacket()](#sendPacket-)


[sendPacket(packetName)](#sendPacket-String-)


[sendPacket(clazz)](#sendPacket-Class-)


[receivePacket()](#receivePacket-)


[receivePacket(packetName)](#receivePacket-String-)


[receivePacket(clazz)](#receivePacket-Class-)


[getPacketNames()](#getPacketNames-)


[reset()](#reset-)


[writeRegistryKey(key)](#writeRegistryKey-RegistryKey-)


[readRegistryKey(registry)](#readRegistryKey-RegistryKey-)


[writeCollection(collection, writer)](#writeCollection-Collection-MethodWrapper-)


[readList(reader)](#readList-MethodWrapper-)


[writeIntList(list)](#writeIntList-Collection-)


[readIntList()](#readIntList-)


[writeMap(map, keyWriter, valueWriter)](#writeMap-Map-MethodWrapper-MethodWrapper-)


[readMap(keyReader, valueReader)](#readMap-MethodWrapper-MethodWrapper-)


[forEachInCollection(reader)](#forEachInCollection-MethodWrapper-)


[writeOptional(value, writer)](#writeOptional-T-MethodWrapper-)


[readOptional(reader)](#readOptional-MethodWrapper-)


[writeNullable(value, writer)](#writeNullable-Object-MethodWrapper-)


[readNullable(reader)](#readNullable-MethodWrapper-)


[writeByteArray(bytes)](#writeByteArray-byte[]-)


[readByteArray()](#readByteArray-)


[readByteArray(maxSize)](#readByteArray-int-)


[writeIntArray(ints)](#writeIntArray-int[]-)


[readIntArray()](#readIntArray-)


[readIntArray(maxSize)](#readIntArray-int-)


[writeLongArray(longs)](#writeLongArray-long[]-)


[readLongArray()](#readLongArray-)


[readLongArray(maxSize)](#readLongArray-int-)


[writeBlockPos(pos)](#writeBlockPos-BlockPosHelper-)


[writeBlockPos(x, y, z)](#writeBlockPos-int-int-int-)


[readBlockPos()](#readBlockPos-)


[writeChunkPos(x, z)](#writeChunkPos-int-int-)


[writeChunkPos(chunk)](#writeChunkPos-ChunkHelper-)


[readChunkPos()](#readChunkPos-)


[readChunkHelper()](#readChunkHelper-)


[writeChunkSectionPos(chunkX, y, chunkZ)](#writeChunkSectionPos-int-int-int-)


[writeChunkSectionPos(chunk, y)](#writeChunkSectionPos-ChunkHelper-int-)


[readChunkSectionPos()](#readChunkSectionPos-)


[writeGlobalPos(dimension, pos)](#writeGlobalPos-String-BlockPosHelper-)


[writeGlobalPos(dimension, x, y, z)](#writeGlobalPos-String-int-int-int-)


[writeEnumConstant(constant)](#writeEnumConstant-Enum-)


[readEnumConstant(enumClass)](#readEnumConstant-Class-)


[writeVarInt(i)](#writeVarInt-int-)


[readVarInt()](#readVarInt-)


[writeVarLong(l)](#writeVarLong-long-)


[readVarLong()](#readVarLong-)


[writeUuid(uuid)](#writeUuid-String-)


[readUuid()](#readUuid-)


[writeNbt(nbt)](#writeNbt-NBTElementHelper$NBTCompoundHelper-)


[readNbt()](#readNbt-)


[writeString(string)](#writeString-String-)


[writeString(string, maxLength)](#writeString-String-int-)


[readString()](#readString-)


[readString(maxLength)](#readString-int-)


[writeIdentifier(id)](#writeIdentifier-String-)


[readIdentifier()](#readIdentifier-)


[writeDate(date)](#writeDate-Date-)


[readDate()](#readDate-)


[writeInstant(instant)](#writeInstant-Instant-)


[readInstant()](#readInstant-)


[writePublicKey(key)](#writePublicKey-PublicKey-)


[readPublicKey()](#readPublicKey-)


[writeBlockHitResult(hitResult)](#writeBlockHitResult-BlockHitResult-)
D


[writeBlockHitResult(hitResult)](#writeBlockHitResult-HitResultHelper$Block-)


[writeBlockHitResult(pos, direction, blockPos, missed, insideBlock)](#writeBlockHitResult-Pos3D-String-BlockPosHelper-boolean-boolean-)


[readBlockHitResult()](#readBlockHitResult-)
D


[readBlockHitResultMap()](#readBlockHitResultMap-)
D


[readBlockHitResultHelper()](#readBlockHitResultHelper-)


[writeBitSet(bitSet)](#writeBitSet-BitSet-)


[readBitSet()](#readBitSet-)


[readerIndex()](#readerIndex-)


[setReaderIndex(index)](#setReaderIndex-int-)


[writerIndex()](#writerIndex-)


[setWriterIndex(index)](#setWriterIndex-int-)


[setIndices(readerIndex, writerIndex)](#setIndices-int-int-)


[resetIndices()](#resetIndices-)


[markReaderIndex()](#markReaderIndex-)


[resetReaderIndex()](#resetReaderIndex-)


[markWriterIndex()](#markWriterIndex-)


[resetWriterIndex()](#resetWriterIndex-)


[clear()](#clear-)


[writeBoolean(value)](#writeBoolean-boolean-)


[setBoolean(index, value)](#setBoolean-int-boolean-)


[readBoolean()](#readBoolean-)


[getBoolean(index)](#getBoolean-int-)


[writeChar(value)](#writeChar-int-)


[setChar(index, value)](#setChar-int-char-)


[readChar()](#readChar-)


[getChar(index)](#getChar-int-)


[writeByte(value)](#writeByte-int-)


[setByte(index, value)](#setByte-int-int-)


[readByte()](#readByte-)


[readUnsignedByte()](#readUnsignedByte-)


[getByte(index)](#getByte-int-)


[getUnsignedByte(index)](#getUnsignedByte-int-)


[writeShort(value)](#writeShort-int-)


[setShort(index, value)](#setShort-int-int-)


[readShort()](#readShort-)


[readUnsignedShort()](#readUnsignedShort-)


[getShort(index)](#getShort-int-)


[getUnsignedShort(index)](#getUnsignedShort-int-)


[writeMedium(value)](#writeMedium-int-)


[setMedium(index, value)](#setMedium-int-int-)


[readMedium()](#readMedium-)


[readUnsignedMedium()](#readUnsignedMedium-)


[getMedium(index)](#getMedium-int-)


[getUnsignedMedium(index)](#getUnsignedMedium-int-)


[writeInt(value)](#writeInt-int-)


[setInt(index, value)](#setInt-int-int-)


[readInt()](#readInt-)


[readUnsignedInt()](#readUnsignedInt-)


[getInt(index)](#getInt-int-)


[getUnsignedInt(index)](#getUnsignedInt-int-)


[writeLong(value)](#writeLong-long-)


[setLong(index, value)](#setLong-int-long-)


[readLong()](#readLong-)


[getLong(index)](#getLong-int-)


[writeFloat(value)](#writeFloat-double-)


[setFloat(index, value)](#setFloat-int-double-)


[readFloat()](#readFloat-)


[getFloat(index)](#getFloat-int-)


[writeDouble(value)](#writeDouble-double-)


[setDouble(index, value)](#setDouble-int-double-)


[readDouble()](#readDouble-)


[getDouble(index)](#getDouble-int-)


[writeZero(length)](#writeZero-int-)


[setZero(index, length)](#setZero-int-int-)


[writeBytes(bytes)](#writeBytes-byte[]-)


[setBytes(index, bytes)](#setBytes-int-byte[]-)


[readBytes(length)](#readBytes-int-)


[getBytes(index, length)](#getBytes-int-int-)


[skipBytes(length)](#skipBytes-int-)


[toString()](#toString-)


[getPacketName(packet)](#getPacketName-Packet-)
S


[init()](#init-)
S


[main(args)](#main-String[]-)
S



### Fields

#### .BUFFER\_TO\_PACKET

Static
Final

Don't touch this here!


##### Type: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[Class](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Class.html)< ? >, [Function](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Function.html)<[PacketByteBuf](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/PacketByteBuf), ? >>



### Methods

#### .toPacket()

1.8.4


##### Returns: [Packet](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/Packet)< ? >

the packet for this buffer or `null` if no packet was used to create this
helper.



#### .toPacket(packetName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetName | String | the name of the packet's class that should be returned |

##### Returns: [Packet](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/Packet)< ? >

the packet for this buffer.



#### .toPacket(clazz)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> | the class of the packet to return |

##### Returns: [Packet](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/Packet)< ? >

the packet for this buffer.



#### .getPacketId(packetClass)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetClass | Class<?> | the class of the packet to get the id for |

##### Returns: int

the id of the packet.



#### .getNetworkStateId(packetClass)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetClass | Class<?> | the class of the packet to get the id for |

##### Returns: int

the id of the network state the packet belongs to.



#### .isClientbound(packetClass)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetClass | Class<?> | the class to get the side for |

##### Returns: boolean

`true` if the packet is clientbound, `false` if it is serverbound.



#### .isServerbound(packetClass)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetClass | Class<?> | the class to get the id for |

##### Returns: boolean

`true` if the packet is serverbound, `false` if it is clientbound.



#### .sendPacket()

1.8.4

Send a packet of the given type, created from this buffer, to the server.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .sendPacket(packetName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetName | String | the name of the packet's class that should be sent |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .sendPacket(clazz)

1.8.4

Send a packet of the given type, created from this buffer, to the server.

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> | the class of the packet to send |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .receivePacket()

1.8.4


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .receivePacket(packetName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| packetName | String | the name of the packet's class that should be received |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .receivePacket(clazz)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| clazz | Class<?> | the class of the packet to receive |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .getPacketNames()

1.8.4

These names are subject to change and are only for an easier access. They will probably not
change in the future, but it is not guaranteed.


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

a list of all packet names.



#### .reset()

1.8.4

Resets the buffer to the state it was in when this helper was created.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeRegistryKey(key)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| key | RegistryKey<?> | the registry key to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readRegistryKey< T >(registry)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| registry | RegistryKey<?> | the registry the read key is from |

##### Returns: [RegistryKey](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/registry/RegistryKey)< T >

the registry key.



#### .writeCollection< T >(collection, writer)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| collection | Collection<T> | the collection to store |
| writer | MethodWrapper<PacketByteBuf, T, ?, ?> | the function that writes the collection's elements to the buffer |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readList< T >(reader)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| reader | MethodWrapper<PacketByteBuf, ?, T, ?> | the function that reads the collection's elements from the buffer |

##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)< T >

the read list.



#### .writeIntList(list)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| list | Collection<Integer> | the integer list to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readIntList()

1.8.4


##### Returns: [IntList](1.9.2/)

the read integer list.



#### .writeMap< K , V >(map, keyWriter, valueWriter)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| map | Map<K, V> | the map to store |
| keyWriter | MethodWrapper<PacketByteBuf, K, ?, ?> | the function to write the map's keys to the buffer |
| valueWriter | MethodWrapper<PacketByteBuf, V, ?, ?> | the function to write the map's values to the buffer |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readMap< K , V >(keyReader, valueReader)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| keyReader | MethodWrapper<PacketByteBuf, ?, K, ?> | the function to read the map's keys from the buffer |
| valueReader | MethodWrapper<PacketByteBuf, ?, V, ?> | the function to read the map's values from the buffer |

##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)< K , V >

the read map.



#### .forEachInCollection(reader)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| reader | MethodWrapper<PacketByteBuf, ?, Object, ?> | the function to read the collection's elements from the buffer |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeOptional< T >(value, writer)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | T | the optional value to store |
| writer | MethodWrapper<PacketByteBuf, T, ?, ?> | the function to write the optional value if present to the buffer |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readOptional< T >(reader)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| reader | MethodWrapper<PacketByteBuf, ?, T, ?> | the function to read the optional value from the buffer if present |

##### Returns: [Optional](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Optional.html)< T >

the optional value.



#### .writeNullable(value, writer)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | Object | the optional value to store |
| writer | MethodWrapper<PacketByteBuf, Object, ?, ?> | the function to write the optional value if it's not null to the buffer |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readNullable< T >(reader)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| reader | MethodWrapper<PacketByteBuf, ?, T, ?> | the function to read the value from the buffer if it's not null |

##### Returns: T

the read value or `null` if it was null.



#### .writeByteArray(bytes)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| bytes | byte[] | the bytes to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readByteArray()

1.8.4


##### Returns: byte []

the read byte array.



#### .readByteArray(maxSize)

1.8.4

Will throw an exception if the byte array is bigger than the given maximum size.

| Parameter | Type | Description |
|---|---|---|
| maxSize | int | the maximum size of the byte array to read |

##### Returns: byte []

the read byte array.



#### .writeIntArray(ints)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| ints | int[] | the int array to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readIntArray()

1.8.4


##### Returns: int []

the read int array.



#### .readIntArray(maxSize)

1.8.4

Will throw an exception if the int array is bigger than the given maximum size.

| Parameter | Type | Description |
|---|---|---|
| maxSize | int | the maximum size of the int array to read |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeLongArray(longs)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| longs | long[] | the long array to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readLongArray()

1.8.4


##### Returns: long []

the read long array.



#### .readLongArray(maxSize)

1.8.4

Will throw an exception if the long array is bigger than the given maximum size.

| Parameter | Type | Description |
|---|---|---|
| maxSize | int | the maximum size of the long array to read |

##### Returns: long []

the read long array.



#### .writeBlockPos(pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | BlockPosHelper | the block position to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeBlockPos(x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the block position to store |
| y | int | the y coordinate of the block position to store |
| z | int | the z coordinate of the block position to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readBlockPos()

1.8.4


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the read block position.



#### .writeChunkPos(x, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| x | int | the x coordinate of the chunk to store |
| z | int | the z coordinate of the chunk to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeChunkPos(chunk)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| chunk | ChunkHelper | the chunk to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readChunkPos()

1.8.4


##### Returns: int []

the position of the read chunk, x at index 0, z at index 1.



#### .readChunkHelper()

1.8.4


##### Returns: [ChunkHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ChunkHelper.html)

a [ChunkHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/ChunkHelper.html) for the read chunk position.



#### .writeChunkSectionPos(chunkX, y, chunkZ)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| chunkX | int | the x coordinate of the chunk to store |
| y | int | the y coordinate to store |
| chunkZ | int | the z coordinate of the chunk to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeChunkSectionPos(chunk, y)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| chunk | ChunkHelper | the chunk whose position should be stored |
| y | int | the y to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readChunkSectionPos()

1.8.4


##### Returns: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)

the read chunk section pos, as a [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html).



#### .writeGlobalPos(dimension, pos)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| dimension | String | the dimension, vanilla default are overworld, the_nether,
                                          the_end |
| pos | BlockPosHelper | the position to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeGlobalPos(dimension, x, y, z)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| dimension | String | the dimension, vanilla default are overworld, the_nether,
                                          the_end |
| x | int | the x coordinate of the position to store |
| y | int | the y coordinate of the position to store |
| z | int | the z coordinate of the position to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeEnumConstant(constant)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| constant | Enum<?> | the enum constant to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readEnumConstant< T **extends** [Enum](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Enum.html)< T > >(enumClass)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| enumClass | Class<T
                             extends Enum<T>> | the class of the enum to read from |

##### Returns: T **extends** [Enum](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Enum.html)< T >

the read enum constant.



#### .writeVarInt(i)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| i | int | the int to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readVarInt()

1.8.4


##### Returns: int

the read int.



#### .writeVarLong(l)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| l | long | the long to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readVarLong()

1.8.4


##### Returns: long

the read long.



#### .writeUuid(uuid)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| uuid | String | the UUID to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readUuid()

1.8.4


##### Returns: [UUID](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/UUID.html)

the read UUID.



#### .writeNbt(nbt)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| nbt | NBTElementHelper$NBTCompoundHelper | the nbt |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readNbt()

1.8.4


##### Returns: [NBTElementHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/NBTElementHelper.html)< ? >

the read nbt data.



#### .writeString(string)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| string | String | the string to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeString(string, maxLength)

1.8.4

Throws an exception if the string is longer than the given length.

| Parameter | Type | Description |
|---|---|---|
| string | String | the string to store |
| maxLength | int | the maximum length of the string |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readString()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the read string.



#### .readString(maxLength)

1.8.4

Throws an exception if the read string is longer than the given length.

| Parameter | Type | Description |
|---|---|---|
| maxLength | int | the maximum length of the string to read |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the read string.



#### .writeIdentifier(id)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| id | String | the identifier to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readIdentifier()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the read identifier.



#### .writeDate(date)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| date | Date | the date to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readDate()

1.8.4


##### Returns: [Date](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Date.html)

the read date.



#### .writeInstant(instant)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| instant | Instant | the instant to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readInstant()

1.8.4


##### Returns: [Instant](https://docs.oracle.com/javase/8/docs/api/index.html?java/time/Instant.html)

the read instant.



#### .writePublicKey(key)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| key | PublicKey | the public key to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readPublicKey()

1.8.4


##### Returns: [PublicKey](https://docs.oracle.com/javase/8/docs/api/index.html?java/security/PublicKey.html)

the read public key.



#### .writeBlockHitResult(hitResult)

Deprecated

1.8.4

| Parameter | Type | Description |
|---|---|---|
| hitResult | BlockHitResult | the hit result to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeBlockHitResult(hitResult)

1.9.1

| Parameter | Type | Description |
|---|---|---|
| hitResult | HitResultHelper$Block | the hit result to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeBlockHitResult(pos, direction, blockPos, missed, insideBlock)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| pos | Pos3D | the position of the BlockHitResult |
| direction | String | the direction of the BlockHitResult |
| blockPos | BlockPosHelper | the block pos of the BlockHitResult |
| missed | boolean | whether the BlockHitResult missed |
| insideBlock | boolean | whether the BlockHitResult is inside a block |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readBlockHitResult()

Deprecated

1.8.4


##### Returns: [BlockHitResult](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/util/hit/BlockHitResult)

the read block hit result.



#### .readBlockHitResultMap()

Deprecated

1.8.4


##### Returns: [Map](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html), [Object](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Object.html)>

a map of the block hit result's data and their values.



#### .readBlockHitResultHelper()

1.9.1


##### Returns: [HitResultHelper$Block](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/HitResultHelper.Block.html)

the read block hit result as a helper.



#### .writeBitSet(bitSet)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| bitSet | BitSet | the bit set to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readBitSet()

1.8.4


##### Returns: [BitSet](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/BitSet.html)

the read bit set.



#### .readerIndex()

1.8.4


##### Returns: int

the readers current position.



#### .setReaderIndex(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the readers new index |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writerIndex()

1.8.4


##### Returns: int

the writers current position.



#### .setWriterIndex(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the writers new index |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setIndices(readerIndex, writerIndex)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| readerIndex | int | the readers new index |
| writerIndex | int | the writers new index |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .resetIndices()

1.8.4

Resets the readers and writers index to their respective last marked indices.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .markReaderIndex()

1.8.4

Marks the readers current index for later use.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .resetReaderIndex()

1.8.4

Resets the readers index to the last marked index.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .markWriterIndex()

1.8.4

Marks the writers current index for later use.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .resetWriterIndex()

1.8.4

Resets the writers index to the last marked index.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .clear()

1.8.4

Resets the writers and readers index to 0. This technically doesn't clear the buffer, but
rather makes it so that new operations will overwrite the old data.


##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeBoolean(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | boolean | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setBoolean(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | boolean | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readBoolean()

1.8.4


##### Returns: boolean

the read boolean value.



#### .getBoolean(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: boolean

the boolean value at the given index.



#### .writeChar(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setChar(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | char | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readChar()

1.8.4


##### Returns: char

the read char value.



#### .getChar(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: char

the char at the given index.



#### .writeByte(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setByte(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readByte()

1.8.4


##### Returns: byte

the read byte value.



#### .readUnsignedByte()

1.8.4


##### Returns: short

the read unsigned byte value, represented as a short.



#### .getByte(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: byte

the byte at the given index.



#### .getUnsignedByte(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: short

the unsigned byte at the given index, represented as a short.



#### .writeShort(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setShort(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readShort()

1.8.4


##### Returns: short

the read short value.



#### .readUnsignedShort()

1.8.4


##### Returns: int

the read unsigned short value, represented as an int.



#### .getShort(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: short

the short at the given index.



#### .getUnsignedShort(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: int

the unsigned short at the given index, represented as an int.



#### .writeMedium(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setMedium(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readMedium()

1.8.4


##### Returns: int

the read medium value.



#### .readUnsignedMedium()

1.8.4


##### Returns: int

the read unsigned medium value.



#### .getMedium(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: int

the medium at the given index.



#### .getUnsignedMedium(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: int

the unsigned medium at the given index.



#### .writeInt(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setInt(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | int | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readInt()

1.8.4


##### Returns: int

the read int value.



#### .readUnsignedInt()

1.8.4


##### Returns: long

the read unsigned int value, represented as a long.



#### .getInt(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: int

the int at the given index.



#### .getUnsignedInt(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: long

the unsigned int at the given index, represented as a long.



#### .writeLong(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | long | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setLong(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | long | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readLong()

1.8.4


##### Returns: long

the read long value.



#### .getLong(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: long

the long at the given index.



#### .writeFloat(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | double | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setFloat(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | double | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readFloat()

1.8.4


##### Returns: float

the read float value.



#### .getFloat(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: float

the float at the given index.



#### .writeDouble(value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| value | double | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setDouble(index, value)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| value | double | the value to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readDouble()

1.8.4


##### Returns: double

the read double value.



#### .getDouble(index)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to read from |

##### Returns: double

the double at the given index.



#### .writeZero(length)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| length | int | the amount of zeros to write |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setZero(index, length)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| length | int | the amount of zeros to write |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .writeBytes(bytes)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| bytes | byte[] | the bytes to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .setBytes(index, bytes)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to write to |
| bytes | byte[] | the bytes to store |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .readBytes(length)

1.8.4

Starts reading from this buffer's readerIndex.

| Parameter | Type | Description |
|---|---|---|
| length | int | the length of the array to read |

##### Returns: byte []

the read byte array.



#### .getBytes(index, length)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| index | int | the index to start reading from |
| length | int | the length of the array to read |

##### Returns: byte []

the read byte array .



#### .skipBytes(length)

1.8.4

Moves the readerIndex of this buffer by the specified amount.

| Parameter | Type | Description |
|---|---|---|
| length | int | the amount of bytes to skip |

##### Returns: [PacketByteBufferHelper](#)

self for chaining.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .getPacketName(packet)

Static
| Parameter | Type | Description |
|---|---|---|
| packet | Packet<?> |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .init()

Static

##### Returns: void



#### .main(args)

Static
| Parameter | Type | Description |
|---|---|---|
| args | String[] |  |

##### Returns: void




