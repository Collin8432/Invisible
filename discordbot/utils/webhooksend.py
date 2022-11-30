import disnake
from disnake import Webhook

import aiohttp

from discordbot.utils.db import *
from discordbot.utils.color import color


async def webhooksend(title: str, description: str, guild_id: str) -> None:
   try:
      async with aiohttp.ClientSession() as session:
         hook = get_discordserver(server_id=guild_id, data="server_webhook")
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
            text=f"Incognito Discord Bot"
         )
         await webhook.send(embed=embed)
   except: 
      pass