

xyz.wagyourtail.jsmacros.client.gui.editor.History
--------------------------------------------------

#### 

### Constructors

#### new History (start, cursor)

| Parameter | Type | Description |
|---|---|---|
| start | String |  |
| cursor | SelectCursor |  |



#### Fields

[onChange](#onChange)


[current](#current)



#### Methods

[addChar(position, content)](#addChar-int-char-)


[add(position, content)](#add-int-String-)


[deletePos(position, length)](#deletePos-int-int-)


[bkspacePos(position, length)](#bkspacePos-int-int-)


[shiftLine(startLine, lines, shiftDown)](#shiftLine-int-int-boolean-)


[replace(position, length, content)](#replace-int-int-String-)


[tabLines(startLine, lineCount, reverse)](#tabLines-int-int-boolean-)


[tabLinesKeepCursor(startLine, startLineIndex, endLineIndex, lineCount, reverse)](#tabLinesKeepCursor-int-int-int-int-boolean-)


[undo()](#undo-)


[redo()](#redo-)



### Fields

#### .onChange


##### Type: [Consumer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/Consumer.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>



#### .current


##### Type: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)



### Methods

#### .addChar(position, content)

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| content | char |  |

##### Returns: boolean

is new step.



#### .add(position, content)

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| content | String |  |

##### Returns: boolean



#### .deletePos(position, length)

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| length | int |  |

##### Returns: boolean

is new step.



#### .bkspacePos(position, length)

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| length | int |  |

##### Returns: boolean

is new step



#### .shiftLine(startLine, lines, shiftDown)

| Parameter | Type | Description |
|---|---|---|
| startLine | int |  |
| lines | int |  |
| shiftDown | boolean |  |

##### Returns: boolean



#### .replace(position, length, content)

| Parameter | Type | Description |
|---|---|---|
| position | int |  |
| length | int |  |
| content | String |  |

##### Returns: void



#### .tabLines(startLine, lineCount, reverse)

| Parameter | Type | Description |
|---|---|---|
| startLine | int |  |
| lineCount | int |  |
| reverse | boolean |  |

##### Returns: void



#### .tabLinesKeepCursor(startLine, startLineIndex, endLineIndex, lineCount, reverse)

| Parameter | Type | Description |
|---|---|---|
| startLine | int |  |
| startLineIndex | int |  |
| endLineIndex | int |  |
| lineCount | int |  |
| reverse | boolean |  |

##### Returns: void



#### .undo()


##### Returns: int

position of step. -1 if nothing to undo.



#### .redo()


##### Returns: int

position of step. -1 if nothing to redo.




