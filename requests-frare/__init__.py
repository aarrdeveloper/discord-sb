import requests
import discord
from discord.ext import commands



class selfBot(bot=None):
  global bot
  async def tools(token):
    if bot:
      token = "Bot + "token
    if not bot:
      token = token
    global token
    header = {"authorization": token}
    data = threading.Thread(target=requests.get("https://discord.com/api/v9/users/@me",headers=header).json())
    print(data["username"] + data["discriminator"] + " : login")
    def send(content,channel):
      headers = {"authorization": token}
      threading.Thread(target=requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",data={"content": content},headers=headers)).start
    def typing(channenl):
      headers = {"authorization": token}
      threading.Thread(target=requests.get(f"https://discord.com/api/v9/channels/{channel}/typing",headers=headers)).start
    def leave(guild):
      headers={'authorization': token}
      requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}",headers=headers)
