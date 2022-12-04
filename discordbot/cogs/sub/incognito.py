import disnake
from disnake.ext import commands

from discordbot.utils.color import color

global starttime
starttime = disnake.utils.utcnow()

class Incognito(commands.Cog):

   def __init__(self, bot):
      self.bot = bot
   
   @commands.slash_command(
      name="incognito",
      description="uptime"
   )
   async def incognito(self, interaction):
      pass
   
   @incognito.sub_command(
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
   
   
   