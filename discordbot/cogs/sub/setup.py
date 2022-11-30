import disnake
from disnake.ext import commands

from discordbot.utils.db import insert_into_discordserver, insert_into_muterole, insert_into_bannedwords, rem_from_discordserver
from discordbot.utils.webhooksend import webhooksend

class SetupSelect(disnake.ui.Select):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
      options = [
         disnake.SelectOption(
            label="Complete Setup (recommended)",
            description="Complete setup, includes all of the options",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Server Member Count Voice Channel",
            # description="Creates a voice channel that periodically updates itself with the amount of members in the server",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Verification",
            # description="Creates a verification channel and verification role, the role will be able to view the rest of the server channels",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Logging Only",
            description="Discord webhook logging only",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Welcome Message",
            # description="sends a welcome message into the system messages channel, located in server settings", 
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Create mute role",
            description="creates a role that is not able to speak in voice channels", 
            emoji="⚙️"
         ),
      ]
      super().__init__(
         placeholder="Select An Option",
         min_values=1, 
         max_values=1,
         options=options
      )
      
   async def callback(self, interaction: disnake.MessageInteraction):
      print("callback")
      if self.values[0] == "Complete Setup (recommended)":
         print("value0")
         await interaction.send("Setup Started", ephemeral=True)
         with open("discordbot/utils/discord-avatar.png", "rb") as file:
            data = file.read()
         overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
         }
         category = await interaction.guild.create_category(name="Incognito", overwrites=overwrites)
         channel = await category.create_text_channel(name="IncognitoBot-Logs", overwrites=overwrites)
         webhook = await channel.create_webhook(name="Incognito", avatar=data)
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")

         memberchannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         
         verificationrole = await interaction.guild.create_role(name="Verified", permissions=disnake.Permissions(view_channel=True))
         _overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.get_role(verificationrole.id): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False)
         }
         verificationchannel = await interaction.guild.create_text_channel(name="verify", overwrites=_overwrites)
         await verificationchannel.send("Enter /verify in the chat to verify yourself into {}".format(interaction.guild.name))
         
         muterole = await interaction.guild.create_role(name="muted", permissions=disnake.Permissions(speak=False))
         
         await interaction.send(f"{interaction.author.mention} Enter the welcome message you would like to send when a member joins the server")
         def check(message):
            return message.content
         welcomemessage = await self.bot.wait_for("message", check=check, timeout=500)
         
         await interaction.send(f"{interaction.author.mention} Enter a list a words seperated by commas that will be banned from the server eg.: incognito, hi, hello")
         def check(message):
            return message.content
         bannedwords = await self.bot.wait_for("message", check=check, timeout=500)
         words = []
         for _ in bannedwords.content.split(","):
            _.strip()
            words.append(_)
     
         server_webhook=webhook.url
         server_id = interaction.guild.id
         server_membercountvc = memberchannel.id
         server_invite = await memberchannel.create_invite()
         verification_channel_id = verificationchannel.id
         verificaiton_role_id = verificationrole.id 
         welcome_message = welcomemessage.content
         
         insert_into_discordserver(server_webhook, server_id, server_membercountvc, server_invite, verification_channel_id, verificaiton_role_id, welcome_message)
         insert_into_muterole(muterole=muterole.id, server_id=interaction.guild.id)
         insert_into_bannedwords(words=str(words), server_id=interaction.guild.id)
      
      elif self.values[0] == "Verification":
         _verificationrole = await interaction.guild.create_role(name="Verified", permissions=disnake.Permissions(view_channel=True))
         _overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.get_role(verificationrole.id): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False)
         }
         _verificationchannel = await interaction.guild.create_text_channel(name="verify", overwrites=_overwrites)
         await _verificationchannel.send("Enter /verify in the chat to verify yourself into {}".format(interaction.guild.name))
         
         _server_webhook="None" #_webhook.url 
         _server_id = interaction.guild.id
         _server_membercountvc ="None" # _memberchannel.id
         _server_invite ="None" #await _memberchannel.create_invite()
         _verification_channel_id = _verificationchannel.id
         _verificaiton_role_id = _verificationrole.id 
         _welcome_message ="None" # _welcomemessage.content
         
         insert_into_discordserver(_server_webhook, _server_id, _server_membercountvc, _server_invite, _verification_channel_id, _verificaiton_role_id, _welcome_message)
         
      elif self.values[0] == "Server Member Count Voice Channel":
         __memberchannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         __server_webhook="None" #_webhook.url 
         __server_id = interaction.guild.id
         __server_membercountvc =__memberchannel.id
         __server_invite = await __memberchannel.create_invite()
         __verification_channel_id ="None" #verificationchannel.id
         __verificaiton_role_id ="None"# _verificationrole.id 
         __welcome_message ="None" # _welcomemessage.content
         
         insert_into_discordserver(__server_webhook, __server_id, __server_membercountvc, __server_invite, __verification_channel_id, __verificaiton_role_id, __welcome_message)

      elif self.values[0] == "Logging Only":
         with open("discordbot/utils/discord-avatar.png", "rb") as file:
            ___data = file.read()
         ___overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
         }
         ___category = await interaction.guild.create_category(name="Incognito", overwrites=___overwrites)
         ___channel = await ___category.create_text_channel(name="IncognitoBot-Logs", overwrites=___overwrites)
         ___webhook = await ___channel.create_webhook(name="Incognito", avatar=___data)
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
         
         ___server_webhook= ___webhook.url 
         ___server_id = interaction.guild.id
         ___server_membercountvc ="None" #__memberchannel.id
         ___server_invite ="None" #await __memberchannel.create_invite()
         ___verification_channel_id ="None" #verificationchannel.id
         ___verificaiton_role_id ="None"# _verificationrole.id 
         ___welcome_message ="None" # _welcomemessage.content
         
         insert_into_discordserver(___server_webhook, ___server_id, ___server_membercountvc, ___server_invite, ___verification_channel_id, ___verificaiton_role_id, ___welcome_message)
      
      elif self.values[0] == "Welcome Message":
         await interaction.send(f"{interaction.author.mention} Enter the welcome message you would like to send when a member joins the server")
         def check(message):
            return message.content
         ____welcomemessage = await self.bot.wait_for("message", check=check, timeout=500)
         
         ____server_webhook="None" #___webhook.url 
         ____server_id = interaction.guild.id
         ____server_membercountvc ="None" #__memberchannel.id
         ____server_invite ="None" #await __memberchannel.create_invite()
         ____verification_channel_id ="None" #verificationchannel.id
         ____verificaiton_role_id ="None"# _verificationrole.id 
         ____welcome_message = ____welcomemessage.content
         
         insert_into_discordserver(____server_webhook, ____server_id, ____server_membercountvc, ____server_invite, ____verification_channel_id, ____verificaiton_role_id, ___welcome_message)

         
   async def on_error(self, error: Exception):
      print(error)
      

class Setup(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(
      name="setup",
      description="setup commands",
   )
   async def setup(self, interaction):
      pass
   
   @setup.sub_command(
      name="help",
      description="setup help command"
   )
   async def setuphelp(self, interaction):
      view = disnake.ui.View()
      view.add_item(SetupSelect(self.bot))
      await interaction.send(view=view) 
      
   @setup.sub_command(
      name="fix",
      description="fix database errors"
   )
   async def fix(self, interaction):
      rem_from_discordserver(interaction.guild.id)
      await interaction.send("fixed, run /setup help or one of the /setup (option) to refix the database", ephemeral=True)
