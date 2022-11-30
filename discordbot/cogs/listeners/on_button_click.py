import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_button_click(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_button_click(self, interaction):
         ...
                        