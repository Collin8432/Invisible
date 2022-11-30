import disnake
from disnake.ext import commands

from discordbot.utils.color import color

import logging
logger = logging.getLogger(__name__)


import traceback

def fancy_traceback(exc: Exception) -> str:
    """May not fit the message content limit"""
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

class On_slash_command_error(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error: commands.CommandError):
         msg = f"Slash command `{interaction.data.name}` failed due to `{error}`"
         logger.error(msg, exc_info=True)

         embed = disnake.Embed(
               title=msg,
               description=fancy_traceback(error),
               color=disnake.Color.red(),
         )
         if interaction.response.is_done():
               send = interaction.channel.send
         else:
               send = interaction.response.send_message
         await send(embed=embed)