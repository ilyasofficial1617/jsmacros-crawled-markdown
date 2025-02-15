

xyz.wagyourtail.jsmacros.client.api.classes.TextBuilder
-------------------------------------------------------

#### 

1.3.0

usage: `builder.append("hello,").withColor(0xc).append(" World!").withColor(0x6)`

### Constructors

#### new TextBuilder ()




#### Methods

[append(text)](#append-Object-)


[withColor(color)](#withColor-int-)


[withColor(r, g, b)](#withColor-int-int-int-)


[withFormatting(underline, bold, italic, strikethrough, magic)](#withFormatting-boolean-boolean-boolean-boolean-boolean-)


[withFormatting(formattings)](#withFormatting-FormattingHelper[]-)


[withShowTextHover(text)](#withShowTextHover-TextHelper-)


[withShowItemHover(item)](#withShowItemHover-ItemStackHelper-)


[withShowEntityHover(entity)](#withShowEntityHover-EntityHelper-)


[withCustomClickEvent(action)](#withCustomClickEvent-MethodWrapper-)


[withClickEvent(action, value)](#withClickEvent-String-String-)


[withStyle(style)](#withStyle-StyleHelper-)


[getWidth()](#getWidth-)


[build()](#build-)



### Methods

#### .append(text)

1.3.0

move on to next section and set it's text.

| Parameter | Type | Description |
|---|---|---|
| text | Object | a String, TextHelper or TextBuilder |

##### Returns: [TextBuilder](#)



#### .withColor(color)

1.3.0

set current section's color by color code as hex, like `0x6` for gold
and `0xc` for red.

| Parameter | Type | Description |
|---|---|---|
| color | int |  |

##### Returns: [TextBuilder](#)



#### .withColor(r, g, b)

1.3.1

Add text with custom colors.

| Parameter | Type | Description |
|---|---|---|
| r | int | red 0-255 |
| g | int | green 0-255 |
| b | int | blue 0-255 |

##### Returns: [TextBuilder](#)



#### .withFormatting(underline, bold, italic, strikethrough, magic)

1.3.0

set other formatting options for the current section

| Parameter | Type | Description |
|---|---|---|
| underline | boolean |  |
| bold | boolean |  |
| italic | boolean |  |
| strikethrough | boolean |  |
| magic | boolean |  |

##### Returns: [TextBuilder](#)



#### .withFormatting(formattings)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| formattings | FormattingHelper[] | the formattings to apply |

##### Returns: [TextBuilder](#)

self for chaining.



#### .withShowTextHover(text)

1.3.0

set current section's hover event to show text

| Parameter | Type | Description |
|---|---|---|
| text | TextHelper |  |

##### Returns: [TextBuilder](#)



#### .withShowItemHover(item)

1.3.0

set current section's hover event to show an item

| Parameter | Type | Description |
|---|---|---|
| item | ItemStackHelper |  |

##### Returns: [TextBuilder](#)



#### .withShowEntityHover(entity)

1.3.0

set current section's hover event to show an entity

| Parameter | Type | Description |
|---|---|---|
| entity | EntityHelper<Entity> |  |

##### Returns: [TextBuilder](#)



#### .withCustomClickEvent(action)

1.3.0

custom click event.

| Parameter | Type | Description |
|---|---|---|
| action | MethodWrapper<Object, Object, Object, ?> |  |

##### Returns: [TextBuilder](#)



#### .withClickEvent(action, value)

1.3.0

normal click events like: `open_url`, `open_file`, `run_command`, `suggest_command`, `change_page`, and `copy_to_clipboard`

| Parameter | Type | Description |
|---|---|---|
| action | String |  |
| value | String |  |

##### Returns: [TextBuilder](#)



#### .withStyle(style)

| Parameter | Type | Description |
|---|---|---|
| style | StyleHelper |  |

##### Returns: [TextBuilder](#)



#### .getWidth()

1.8.4


##### Returns: int

the width of this text.



#### .build()

1.3.0

Build to a [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)


##### Returns: [TextHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/TextHelper.html)




