import disnake
from disnake import Webhook

import aiohttp

from utils.db import *
from utils.color import color


async def webhooksend(title: str, description: str, guild_id: str) -> None:
   try:
      async with aiohttp.ClientSession() as session:
         hook = databaseSearchSpecific("discordserver", "server_webhook", "server_id", guild_id)
         webhook = Webhook.from_url(f"{hook}", session=session)
         description = str(description).replace("*", "")
         title = str(title).replace("!", "")
         embed = disnake.Embed(
            title=f"{title} 📍",
            description=f"**{description}**",
            color=color,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
            text=f"Invisible Discord Bot"
         )
         await webhook.send(embed=embed)
   except: 
      pass
   
