import disnake
from disnake.ext import commands

from utils.color import color

global starttime
starttime = disnake.utils.utcnow()

class Invisible(commands.Cog):

   def __init__(self, bot):
      self.bot = bot
   
   @commands.slash_command(
      name="Invisible",
      description="uptime"
   )
   async def Invisible(self, interaction):
      pass
   
   @Invisible.sub_command(
      name="uptime",
      description="displays the bot uptime",
   )
   async def uptime(self, interaction: disnake.ApplicationCommandInteraction):
      embed = disnake.Embed(
         title="Bot Uptime 🕛",
         description=f"{disnake.utils.format_dt(starttime, 'R')}",
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      await interaction.send(embed=embed)
   
   
   