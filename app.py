import disnake
from disnake.ext.commands import AutoShardedInteractionBot
import logging
import asyncio
from flask import Flask, render_template, request


logger = logging.getLogger('disnake')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discordbot/disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
logger.addHandler(handler)

logger2 = logging.getLogger('flask')
logger2.setLevel(logging.DEBUG)
handler2 = logging.FileHandler(filename='flask.log', encoding='utf-8', mode='w')
handler2.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
logger.addHandler(handler2)

intents = disnake.Intents.all()
bot = AutoShardedInteractionBot(intents=intents)
   
def loadcogs():
   bot.load_extension(f"discordbot.cogs.__init__")
   bot.load_extension(f"discordbot.cogs.listeners.__init__")

app = Flask(__name__)

num = 0
@app.route("/")
def index():
   global num
   num += 1
   return render_template("pages/index.html", var=num)

if __name__ == "__main__":
   loadcogs()
   print("Starting up {} shard{}...".format(bot.shard_count,"" if bot.shard_count == 1 else "s"))
   asyncio.create_task(app.run(host='0.0.0.0', port=5000))
   asyncio.create_task(bot.run("MTA0MTQxMTY2NjMwMDExNzE1Mw.Gd1dwP.aN9qnEP_A2rKAuHwnINJ3gNYPk59Drsr-RXiAk"))
