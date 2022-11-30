import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_shard_connect(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_shard_connect(self, shard_id):
         print("Connected to shard {}".format(shard_id))                        