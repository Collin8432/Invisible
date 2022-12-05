import disnake
from disnake.ext import commands

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import random
import asyncio

from utils.webhooksend import webhooksend
from utils.color import color
from utils.db import *


class Verify(commands.Cog):

   def __init__(self, bot):
      self.bot = bot
      
   async def Checker(self, filename):
      try:
         def check(message):
            return message.content == filename.upper() or message.content == filename.lower()
         await self.bot.wait_for("message", check=check, timeout=500)
      except asyncio.TimeoutError:
         return Exception("Timeout")
   
   @commands.slash_command(
      name="verify",
      description="verify into the discord server",
   )
   async def verify(self, interaction: disnake.ApplicationCommandInteraction):
      verifych = get_discordserver(data="verification_channel_id", server_id=interaction.guild.id)
      verifychannel = int(verifych)  
      if interaction.channel.id != verifychannel:
         await interaction.send(f"You can only use this command in <#{verifychannel}>")
      else:
         list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
         FileName = ""
         for i in range(5, 15):
               FileName += (random.choice(list))
               continue
         img = Image.open('discordbot/verify/image-template.png')

         image = ImageDraw.Draw(img)
         font = ImageFont.truetype("discordbot/verify/font/MomB.ttf", 30)

         image.text((75,0), "How to verify", font=font)
         image.text((65, 30), "Enter this code:", font=font)
         image.text((85, 60), FileName, font=font)
         img.save(f"discordbot/verify/incognito{FileName}.png")
         
         await interaction.send(file=disnake.File(f"discordbot/verify/incognito{FileName}.png"))
         await self.Checker(filename=FileName)
         
         verifyrole = get_discordserver(data="verificaiton_role_id", server_id=interaction.guild.id)
         await interaction.author.add_roles(disnake.Object(verifyrole))  
         await webhooksend("Member Verified", f"Verified <@{interaction.author.id}>", f"{interaction.guild.id}")        
         await interaction.channel.purge(limit=9999999)
         embed = disnake.Embed(
               title=f"How To Verify!",
               description="Enter /verify in the chat to verify yourself into {}".format(interaction.guild.name),
               color=color,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
               text=f"Incognito Verification"
            )
         await interaction.send(embed=embed)