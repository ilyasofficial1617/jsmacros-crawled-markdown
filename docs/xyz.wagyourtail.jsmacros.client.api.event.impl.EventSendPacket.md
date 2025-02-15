

xyz.wagyourtail.jsmacros.client.api.event.impl.EventSendPacket
--------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.8.4

### Constructors

#### new EventSendPacket (packet)

| Parameter | Type | Description |
|---|---|---|
| packet | Packet<?> |  |



#### Fields

[packet](#packet)


[type](#type)
F



#### Methods

[replacePacket(args)](#replacePacket-Object[]-)


[getPacketBuffer()](#getPacketBuffer-)


[toString()](#toString-)



### Fields

#### .packet


##### Type: [Packet](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/Packet)< ? >



#### .type

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .replacePacket(args)

1.8.4

Replaces the packet of this event with a new one of the same type, created from the given
arguments. It's recommended to use [EventSendPacket#getPacketBuffer()](#getPacketBuffer-) to modify the packet instead.

| Parameter | Type | Description |
|---|---|---|
| args | Object[] | the arguments to pass to the packet's constructor |

##### Returns: void



#### .getPacketBuffer()

1.8.4

After modifying the buffer, use [PacketByteBufferHelper#toPacket()](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/PacketByteBufferHelper.html#toPacket-) to get the modified
packet and replace this packet with the modified one.


##### Returns: [PacketByteBufferHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/PacketByteBufferHelper.html)

a helper for accessing and modifying the packet's data.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




