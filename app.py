import disnake
from disnake.ext.commands import AutoShardedInteractionBot
import logging
from flask import Flask, render_template, request, redirect
from functools import partial
from threading import Thread
import requests
from operator import contains


from discordbot.utils.db import *


logger = logging.getLogger('disnake')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discordbot/disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
logger.addHandler(handler)

intents = disnake.Intents.all()
bot = AutoShardedInteractionBot(intents=intents)
   
def loadcogs():
   bot.load_extension(f"discordbot.cogs.__init__")
   bot.load_extension(f"discordbot.cogs.listeners.__init__")

def getPerms(perms):
   ALL_PERMS = {
      "CREATE_INSTANT_INVITE": 0x1,
      "KICK_MEMBERS": 0x2,
      "BAN_MEMBERS": 0x4,
      "ADMINISTRATOR": 0x8,
      "MANAGE_CHANNELS": 0x10,
      "MANAGE_GUILD": 0x20,
      "ADD_REACTIONS": 0x40,
      "VIEW_AUDIT_LOG": 0x80,
      "PRIORITY_SPEAKER": 0x100,
      "STREAM": 0x200,
      "VIEW_CHANNEL": 0x400,
      "SEND_MESSAGES": 0x800,
      "SEND_TTS_MESSAGES": 0x1000,
      "MANAGE_MESSAGES": 0x2000,
      "EMBED_LINKS": 0x4000,
      "ATTACH_FILES": 0x8000,
      "READ_MESSAGE_HISTORY": 0x10000,
      "MENTION_EVERYONE": 0x20000,
      "USE_EXTERNAL_EMOJIS": 0x40000,
      "VIEW_GUILD_INSIGHTS": 0x80000,
      "CONNECT": 0x100000,
      "SPEAK": 0x200000,
      "MUTE_MEMBERS": 0x400000,
      "DEAFEN_MEMBERS": 0x800000,
      "MOVE_MEMBERS": 0x1000000,
      "USE_VAD": 0x2000000,
      "CHANGE_NICKNAME": 0x4000000,
      "MANAGE_NICKNAMES": 0x8000000,
      "MANAGE_ROLES": 0x10000000,
      "MANAGE_WEBHOOKS": 0x20000000,
      "MANAGE_EMOJIS_AND_STICKERS": 0x40000000,
      "USE_APPLICATION_COMMANDS": 0x80000000,
      "REQUEST_TO_SPEAK": 0x100000000,
      "MANAGE_EVENTS": 0x200000000,
      "MANAGE_THREADS": 0x400000000,
      "CREATE_PUBLIC_THREADS": 0x800000000,
      "CREATE_PRIVATE_THREADS": 0x1000000000,
      "USE_EXTERNAL_STICKERS": 0x2000000000,
      "SEND_MESSAGES_IN_THREADS": 0x4000000000,
      "USE_EMBEDDED_ACTIVITIES": 0x8000000000,
      "MODERATE_MEMBERS": 0x10000000000,
   }
   has_perms = []

   for p, v in ALL_PERMS.items():
      if int(perms) & v == v:
         has_perms.append(p.replace("_", " ").title())
         
   return has_perms

def checkPerms(perms):
   ALL_PERMS = {
      "CREATE_INSTANT_INVITE": 0x1,
      "KICK_MEMBERS": 0x2,
      "BAN_MEMBERS": 0x4,
      "ADMINISTRATOR": 0x8,
      "MANAGE_CHANNELS": 0x10,
      "MANAGE_GUILD": 0x20,
      "ADD_REACTIONS": 0x40,
      "VIEW_AUDIT_LOG": 0x80,
      "PRIORITY_SPEAKER": 0x100,
      "STREAM": 0x200,
      "VIEW_CHANNEL": 0x400,
      "SEND_MESSAGES": 0x800,
      "SEND_TTS_MESSAGES": 0x1000,
      "MANAGE_MESSAGES": 0x2000,
      "EMBED_LINKS": 0x4000,
      "ATTACH_FILES": 0x8000,
      "READ_MESSAGE_HISTORY": 0x10000,
      "MENTION_EVERYONE": 0x20000,
      "USE_EXTERNAL_EMOJIS": 0x40000,
      "VIEW_GUILD_INSIGHTS": 0x80000,
      "CONNECT": 0x100000,
      "SPEAK": 0x200000,
      "MUTE_MEMBERS": 0x400000,
      "DEAFEN_MEMBERS": 0x800000,
      "MOVE_MEMBERS": 0x1000000,
      "USE_VAD": 0x2000000,
      "CHANGE_NICKNAME": 0x4000000,
      "MANAGE_NICKNAMES": 0x8000000,
      "MANAGE_ROLES": 0x10000000,
      "MANAGE_WEBHOOKS": 0x20000000,
      "MANAGE_EMOJIS_AND_STICKERS": 0x40000000,
      "USE_APPLICATION_COMMANDS": 0x80000000,
      "REQUEST_TO_SPEAK": 0x100000000,
      "MANAGE_EVENTS": 0x200000000,
      "MANAGE_THREADS": 0x400000000,
      "CREATE_PUBLIC_THREADS": 0x800000000,
      "CREATE_PRIVATE_THREADS": 0x1000000000,
      "USE_EXTERNAL_STICKERS": 0x2000000000,
      "SEND_MESSAGES_IN_THREADS": 0x4000000000,
      "USE_EMBEDDED_ACTIVITIES": 0x8000000000,
      "MODERATE_MEMBERS": 0x10000000000,
   }
   has_perms = []

   for p, v in ALL_PERMS.items():
      if int(perms) & v == v:
         has_perms.append(p.replace("_", " ").title())
         
   if contains(has_perms, "Administrator"):
      return True
   else:
      return False
   
def exchange_code(code: str):
   data = {
      "client_id": "1041411666300117153",
      "client_secret": "HBnXStGTRD59mMTJ5iUgGRPEhWmJQr20",
      "grant_type": "authorization_code",
      "code": code,
      "redirect_uri": "http://127.0.0.1:5000/recieveinfo",
      "scope": "  identify guild email"
   }
   headers = {
      "Content-Type": "application/x-www-form-urlencoded"
   }
   response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
   credentials = response.json()
   access_token = credentials["access_token"]
   # response = requests.get("https://discord.com/api/v10/users/@me", headers={
   #    "Authorization": f"Bearer {access_token}"
   # })
   # user = response.json()

   response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={
      "Authorization": f"Bearer {access_token}"
   })
   resp = response.json()
   return resp, access_token

         
app = Flask(__name__)

@app.route("/")
def index():   
   insert_into_sitevisitors()
   vis = get_sitevisitors()
   return render_template("pages/index.html", visitors=vis)

@app.route("/about")
def about():
   insert_into_sitevisitors()
   return render_template("pages/about.html")

@app.route("/contact")
def contact():
   insert_into_sitevisitors()
   return render_template("pages/contact.html")

@app.route("/admin")
def admin():
   insert_into_sitevisitors()
   return render_template("admin/admin.html")
   
@app.route("/recieveinfo")
def recieveinfo():
   insert_into_sitevisitors()
   code = request.args.get("code")
   resp, access_token = exchange_code(code)
   return render_template("admin/recieveinfo.html", servers=resp, access_token=access_token)

   
@app.route("/adminpage")
def adminpage():
   insert_into_sitevisitors()
   server_id = request.args.get("server_id")
   access_token = request.args.get("access_token")
   response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={
      "Authorization": f"Bearer {access_token}"
   })
   resp = response.json()
   
   for item in resp:
      if item.get("id") == server_id:
         server = item
   
   if server["owner"]:
      Permission = True
   else:
      Permission = checkPerms(server["permissions"])
      
   try:
      if Permission == True:
         database = webget(server_id)
         database = database[0]
      else:
         database = ["", "", "", "", "", "", "", "", ""]
         database[0] = "Not enough permission and/or guild not in database"
         database[1] = "Not enough permission and/or guild not in database"
         database[2] = "Not enough permission and/or guild not in database"
         database[3] = "Not enough permission and/or guild not in database"
         database[4] = "Not enough permission and/or guild not in database"
         database[5] = "Not enough permission and/or guild not in database"
         database[6] = "Not enough permission and/or guild not in database"
         database[7] = "Not enough permission and/or guild not in database"
         database[8] = "Not enough permission and/or guild not in database"
   except:
      database = ["", "", "", "", "", "", "", "", ""]
      database[0] = "Not enough permission and/or guild not in database"
      database[1] = "Not enough permission and/or guild not in database"
      database[2] = "Not enough permission and/or guild not in database"
      database[3] = "Not enough permission and/or guild not in database"
      database[4] = "Not enough permission and/or guild not in database"
      database[5] = "Not enough permission and/or guild not in database"
      database[6] = "Not enough permission and/or guild not in database"
      database[7] = "Not enough permission and/or guild not in database"
      database[8] = "Not enough permission and/or guild not in database"
      
      
      
   
   Perms = getPerms(server["permissions"])
   Perms = str(Perms).replace("[", "").replace("]", "").replace("'", "")
   
   Name = server["name"]
   
   Features = server["features"]
   Features = str(Features).replace("[", "").replace("]", "").replace("'", "")
   
   return render_template("admin/adminpage.html", perms=Perms, name=Name, features=Features, server_id=server_id, database=database)



if __name__ == "__main__":
   loadcogs()
   print("Starting up {} shard{}...".format(bot.shard_count,"" if bot.shard_count == 1 else "s"))
   partial_run = partial(app.run, host="0.0.0.0", port=5000, debug=True, use_reloader=False)
   t = Thread(target=partial_run)
   t.start()

   bot.run("MTA0MTQxMTY2NjMwMDExNzE1Mw.Gd1dwP.aN9qnEP_A2rKAuHwnINJ3gNYPk59Drsr-RXiAk")
