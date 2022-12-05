import disnake
from disnake.ext import tasks, commands


import random

from utils.db import *


class Tasks(commands.Cog):
   def __init__(self, bot: commands.AutoShardedInteractionBot):
      self.bot = bot
      self.status_task.start()
      
   @tasks.loop(minutes=1.0)
   async def status_task(self) -> None:
      statuses = ["IncognitoBot", "IncognitoBot.ga", "Incognito Discord Bot"]
      # statuses = [f"Watching Over {len(self.bot.guilds)} Servers!", "With You!", "With Astro!", "In Space!"]
      await self.bot.wait_until_ready()
      await self.bot.change_presence(activity=disnake.Game(random.choice(statuses)))
      try:
         for guild in self.bot.guilds:
            members = guild.member_count
            ch = get_discordserver(guild.id, "server_membercountvc")
            if ch is not None:
                  try:
                     channel = await self.bot.fetch_channel(int(ch))
                  except disnake.NotFound:
                     pass
                  try:
                     await channel.edit(name=f"Members: {members}")
                  except Exception as e:
                     print(e)
      except Exception as e:
         print("task error")
         