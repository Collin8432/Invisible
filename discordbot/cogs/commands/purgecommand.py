import disnake
from disnake.ext import commands

from utils.color import color

class PurgeCommand(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(
      name="purge",
      description="purges a certain number of messages",
   )
   async def purge(self, interaction: disnake.ApplicationCommandInteraction, amount: int):
      await interaction.channel.purge(limit=amount)
      embed = disnake.Embed(
         title="Purged {} messages 🗑️".format(amount),
         timestamp=disnake.utils.utcnow(),
         color=color,
      )     
      await interaction.send(embed=embed)