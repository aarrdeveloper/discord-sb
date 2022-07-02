import requests
import discord
from discord import commands



class selfBot():
  async def tools(token):
    global token
    header = {"authorization": token}
    data = requests.get("https://discord.com/api/v9/users/@me",headers=header).json()
    print(data["username"] + data["discriminator"] + " : login")
    def send(content,channel):
      headers = {"authorization": token}
      threading.Thread(target=requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",data={"content": content},headers=headers)).start
    def typing(channenl):
      headers = {"authorization": token}
      threading.Thread(target=requests.get(f"https://discord.com/api/v9/channels/{channel}/typing",headers=headers)).start
