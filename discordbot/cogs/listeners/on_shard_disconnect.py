import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_shard_disconnect(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_shard_disconnect(self, shard_id):
         print("Shard {} disconnected".format(shard_id))
                        