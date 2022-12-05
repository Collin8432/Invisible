import disnake
from disnake.ext import commands

from utils.color import color

class On_command(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_command(self):
         ...
                        