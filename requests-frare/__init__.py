import cloudscraper
scraper = cloudscraper.create_scraper()
import discord
from discord import commands



class selfBot():
  async def tools(token):
    global token
    def send(content,channel):
      headers = {"authorization": token}
      threading.Thread(target=requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",data={"content": content},headers=headers)).start
    def typing(channenl):
