import disnake
from disnake.ext import commands

from utils.color import color

class HelpCommand(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(
      name="help",
      description="help for the bot",
   )
   async def help(self, interaction: disnake.ApplicationCommandInteraction):
      embed = disnake.Embed(
         title="Help 🆘",
         description="Select a button for help, categories are listed on the button name",
         timestamp=disnake.utils.utcnow(),
         color=color,
      )
      await interaction.send(embed=embed)
      
      
   
      """class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value: Optional[bool] = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.send_message("Confirming...", ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`.
    @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.grey)
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.send_message("Cancelling...", ephemeral=True)
        self.value = False
        self.stop()
"""