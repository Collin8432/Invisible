import disnake
from disnake.ext import commands

from utils.color import color

class On_shard_resumed(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_shard_resumed(self, shard_id):
         print("Shard {} resumed".format(shard_id))
                        