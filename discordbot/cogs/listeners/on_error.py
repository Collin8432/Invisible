import disnake
from disnake.ext import commands

from utils.color import color

class On_error(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_error(self, event, *args, **kwargs):
         print("Error: {}\n{}\n{}".format(event, args, kwargs))
                        