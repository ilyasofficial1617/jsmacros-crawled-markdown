

xyz.wagyourtail.jsmacros.client.api.event.impl.EventRecvPacket
--------------------------------------------------------------

#### extends [BaseEvent](1.9.2/xyz/wagyourtail/jsmacros/core/event/BaseEvent.html)

1.8.4

### Constructors

#### new EventRecvPacket (packet)

| Parameter | Type | Description |
|---|---|---|
| packet | Packet<?> |  |



#### Fields

[packet](#packet)


[type](#type)
F



#### Methods

[getPacketBuffer()](#getPacketBuffer-)


[toString()](#toString-)



### Fields

#### .packet


##### Type: [Packet](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/network/packet/Packet)< ? >



#### .type

Final

##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .getPacketBuffer()

1.8.4

After modifying the buffer, use [PacketByteBufferHelper#toPacket()](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/PacketByteBufferHelper.html#toPacket-) to get the modified
packet and replace this packet with the modified one.


##### Returns: [PacketByteBufferHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/PacketByteBufferHelper.html)

a helper for accessing and modifying the packet's data.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




