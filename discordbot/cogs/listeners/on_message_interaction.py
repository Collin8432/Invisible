import disnake
from disnake.ext import commands

from utils.color import color

class On_message_interaction(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_message_interaction(self, interaction):
         ...
                        