import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_automod_action_execution(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_automod_action_execution(self, execution):
         ...
                        