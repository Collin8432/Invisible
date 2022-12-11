import disnake
from disnake.ext.commands import AutoShardedInteractionBot

intents = disnake.Intents.all()
bot = AutoShardedInteractionBot(intents=intents)

import os
from dotenv import load_dotenv
load_dotenv(".env")

def loadcogs():
   bot.load_extension(f"discordbot.cogs.__init__")
   bot.load_extension(f"discordbot.cogs.listeners.__init__")
   
if __name__ == "__main__":
   loadcogs()
   print("Starting up {} shard{}...".format(bot.shard_count,"" if bot.shard_count == 1 else "s"))
   bot.run(os.environ.get("DISCORDTOKEN"))