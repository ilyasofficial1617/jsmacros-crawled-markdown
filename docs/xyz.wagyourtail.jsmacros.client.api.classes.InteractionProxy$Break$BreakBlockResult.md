

xyz.wagyourtail.jsmacros.client.api.classes.InteractionProxy$Break$BreakBlockResult
-----------------------------------------------------------------------------------

Static
#### 

### Constructors

#### new InteractionProxy$Break$BreakBlockResult (reason, pos)

| Parameter | Type | Description |
|---|---|---|
| reason | String |  |
| pos | BlockPosHelper |  |



#### Fields

[UNAVAILABLE](#UNAVAILABLE)
S
F


[reason](#reason)
F


[pos](#pos)
F



#### Methods

[toString()](#toString-)



### Fields

#### .UNAVAILABLE

Static
Final

##### Type: [InteractionProxy$Break$BreakBlockResult](#)



#### .reason

Final

Can be one of the following reason:  

\* `SUCCESS` - the block has been destroyed on client side, no promise that the server will accept it.  

for example if the block is in protected area, or the server is lagging very hard, then the break will get ignored.  

\* `CANCELLED` - if [InteractionManagerHelper#cancelBreakBlock()](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/InteractionManagerHelper.html#cancelBreakBlock-) was called.  

\* `INTERRUPTED` - if block breaking was interrupted by attack key. (left mouse by default)  

\* `NOT\_BREAKING` - if the block breaking was invalid for some reason.  

\* `RESET` - if interaction proxy has been reset or not in a world.  

\* `NO\_OVERRIDE` - if block breaking override was false but there's remaining callback for some reason.  

\* `IS\_AIR` - if the targeted block was air.  

\* `NO\_TARGET` - if there's no targeted block.  

\* `TARGET\_LOST` - if there's no longer a targeted block.  

\* `TARGET\_CHANGE` - if the targeted block has changed.  

\* `UNAVAILABLE` - if InteractionManager was unavailable. (mc.interactionManager is null)  

\* null - unknown. (proxy method has been called outside the api)  



##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



#### .pos

Final

##### Type: [BlockPosHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/BlockPosHelper.html)



### Methods

#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




