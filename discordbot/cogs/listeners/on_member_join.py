import disnake
from disnake.ext import commands

from discordbot.utils.color import color
from discordbot.utils.webhooksend import webhooksend
from discordbot.utils.db import *

class On_member_join(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_member_join(self, member):  
         await webhooksend(title="Member Joined !", description=f"{member.mention} joined at {member.joined_at}!", guild_id=member.guild.id)
         msg = get_discordserver(member.guild.id, "welcome_message")
         if member.guild.system_channel is not None:
            await member.guild.system_channel.send(msg)
