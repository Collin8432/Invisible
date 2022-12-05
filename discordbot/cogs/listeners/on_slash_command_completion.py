import disnake
from disnake.ext import commands

from utils.color import color

class On_slash_command_completion(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_slash_command_completion(self, interaction):
         ...
                        