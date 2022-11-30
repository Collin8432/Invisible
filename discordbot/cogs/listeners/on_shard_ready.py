import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_shard_ready(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_shard_ready(self, shard_id):
         print("Shard {} ready".format(shard_id))
                        