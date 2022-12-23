import disnake
from disnake.ext import commands

from utils.db import *
from utils.webhooksend import webhooksend
   

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
      name="all",
      description="setup command"
   )
   async def setupall(self, interaction: disnake.ApplicationCommandInteraction):
      await interaction.send("Setup Started", ephemeral=True)
      with open("utils/discord-avatar.png", "rb") as file:
         data = file.read()
      overwrites = {
         interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
      }
      category = await interaction.guild.create_category(name="Invisible", overwrites=overwrites)
      channel = await category.create_text_channel(name="InvisibleBot-Logs", overwrites=overwrites)
      webhook = await channel.create_webhook(name="Invisible", avatar=data)
      
      try:
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
      except Exception as e:
         print(e)

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
      
   
      server_webhook=webhook.url
      server_id = interaction.guild.id
      server_membercountvc = memberchannel.id
      server_invite = str(await memberchannel.create_invite())
      verification_channel_id = verificationchannel.id
      verification_role_id = verificationrole.id 
      welcome_message = welcomemessage.content
      
      databaseInsert("discordserver", {"server_webhook": server_webhook, "server_id": server_id, "server_membercountvc": server_membercountvc, "server_invite": server_invite, "verification_channel_id": verification_channel_id, "verification_role_id": verification_role_id, "welcome_message": welcome_message})
      databaseInsert("muterole", {"muterole": muterole.id, "server_id": interaction.guild.id})
      await interaction.send("Setup Complete", ephemeral=True)
      
   @setup.sub_command(
      name="fix",
      description="fix database errors"
   )
   async def fix(self, interaction):
      databaseDelete("discordserver", "server_id", interaction.guild.id)
      databaseDelete("muterole", "server_id", interaction.guild.id)
      await interaction.send("fixed, run /setup help or one of the /setup (option) to refix the database", ephemeral=True)
