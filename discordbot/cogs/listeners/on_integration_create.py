import disnake
from disnake.ext import commands

from utils.color import color

class On_integration_create(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_integration_create(self):
         ...
                        