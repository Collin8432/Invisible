import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class On_application_command_permissions_update(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_application_command_permissions_update(self, permissions: disnake.GuildApplicationCommandPermissions):
         ...
                        