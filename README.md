# Discord SelfBot
Created By AARR<br>
次世代のcode。<br>
discord.pyやpycord、nextcordに依存しません
# Example
```py
import discord-sb
from discord-sb import *

client = easyBot(bot=False)#SelfBot
commands = client.tools()

channel = 12345678910


commands.typing(channel=channel)# typing Channel


content = "discord-sb　Sender"
commands.send(content=contents,channel=channel)# sending Channel

guild = 12345678910
commands.leave(guild=guild)# leave Guild
```
