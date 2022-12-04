import disnake
from disnake.ext import commands

from discordbot.utils.color import color

class Website(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(
      name="website",
      description="Website commands"
   )
   async def website(self, interaction):
      pass
   
   @website.sub_command(
      name="url",
      description="returns website link"
   )
   async def url(self, interaction):
      embed= disnake.Embed(
         title="Website Link",
         description="https://incognitobot.ga",
         timestamp=disnake.utils.utcnow(),
         color=color
      )
      await interaction.send(embed=embed)