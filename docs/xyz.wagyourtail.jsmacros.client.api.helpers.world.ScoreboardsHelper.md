

xyz.wagyourtail.jsmacros.client.api.helpers.world.ScoreboardsHelper
-------------------------------------------------------------------

#### extends [BaseHelper](1.9.2/xyz/wagyourtail/jsmacros/core/helpers/BaseHelper.html)<[Scoreboard](https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App?mapping=INTERMEDIARY,YARN&version=1.20.5&search=net/minecraft/scoreboard/Scoreboard)>

1.2.9

### Constructors

#### new ScoreboardsHelper (board)

| Parameter | Type | Description |
|---|---|---|
| board | Scoreboard |  |



#### Methods

[getObjectiveForTeamColorIndex(index)](#getObjectiveForTeamColorIndex-int-)


[getObjectiveSlot(slot)](#getObjectiveSlot-int-)


[getPlayerTeamColorIndex(entity)](#getPlayerTeamColorIndex-PlayerEntityHelper-)


[getPlayerTeamColorIndex()](#getPlayerTeamColorIndex-)


[getTeamColorFormatting()](#getTeamColorFormatting-)


[getTeamColorFormatting(player)](#getTeamColorFormatting-PlayerEntityHelper-)


[getTeamColor(player)](#getTeamColor-PlayerEntityHelper-)


[getTeamColor()](#getTeamColor-)


[getTeamColorName(player)](#getTeamColorName-PlayerEntityHelper-)


[getTeamColorName()](#getTeamColorName-)


[getTeams()](#getTeams-)


[getPlayerTeam(p)](#getPlayerTeam-PlayerEntityHelper-)


[getPlayerTeam()](#getPlayerTeam-)


[getCurrentScoreboard()](#getCurrentScoreboard-)


[toString()](#toString-)



### Methods

#### .getObjectiveForTeamColorIndex(index)

1.2.9

| Parameter | Type | Description |
|---|---|---|
| index | int |  |

##### Returns: [ScoreboardObjectiveHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ScoreboardObjectiveHelper.html)



#### .getObjectiveSlot(slot)

1.2.9

`0` is tab list, `1` or `3 + getPlayerTeamColorIndex()` is sidebar, `2` should be below name.
therefore max slot number is 18.

| Parameter | Type | Description |
|---|---|---|
| slot | int |  |

##### Returns: [ScoreboardObjectiveHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ScoreboardObjectiveHelper.html)



#### .getPlayerTeamColorIndex(entity)

1.2.9

| Parameter | Type | Description |
|---|---|---|
| entity | PlayerEntityHelper<PlayerEntity> |  |

##### Returns: int



#### .getPlayerTeamColorIndex()

1.6.5


##### Returns: int

team index for client player



#### .getTeamColorFormatting()

1.8.4


##### Returns: [FormattingHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/FormattingHelper.html)

the formatting for the client player's team, `null` if the player is not in a
team.



#### .getTeamColorFormatting(player)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| player | PlayerEntityHelper<PlayerEntity> | the player to get the team color's formatting for. |

##### Returns: [FormattingHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/FormattingHelper.html)

the formatting for the client player's team, `null` if the player is not in a
team.



#### .getTeamColor(player)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| player | PlayerEntityHelper<PlayerEntity> | the player to get the team color for |

##### Returns: int

the color of the specified player's team or `-1` if the player is not in a team.



#### .getTeamColor()

1.8.4


##### Returns: int

the color of this player's team or `-1` if this player is not in a team.



#### .getTeamColorName(player)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| player | PlayerEntityHelper<PlayerEntity> | the player to get the team color's name for |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the name of the specified player's team color or `null` if the player is not in
a team.



#### .getTeamColorName()

1.8.4


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

the color of this player's team or `null` if this player is not in a team.



#### .getTeams()

1.3.0


##### Returns: [List](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/List.html)<[TeamHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/TeamHelper.html)>



#### .getPlayerTeam(p)

1.3.0

| Parameter | Type | Description |
|---|---|---|
| p | PlayerEntityHelper<PlayerEntity> |  |

##### Returns: [TeamHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/TeamHelper.html)



#### .getPlayerTeam()

1.6.5


##### Returns: [TeamHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/world/TeamHelper.html)

team for client player



#### .getCurrentScoreboard()

1.2.9


##### Returns: [ScoreboardObjectiveHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ScoreboardObjectiveHelper.html)

the [ScoreboardObjectiveHelper](1.9.2/xyz/wagyourtail/jsmacros/client/api/helpers/screen/ScoreboardObjectiveHelper.html) for the currently displayed sidebar scoreboard.



#### .toString()


##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)




