import disnake
from disnake.ext.commands import AutoShardedInteractionBot
from flask import Flask, render_template, request, redirect
from functools import partial
from threading import Thread


from utils.db import *
from utils.web import *


intents = disnake.Intents.all()
bot = AutoShardedInteractionBot(intents=intents)
   
def loadcogs():
   bot.load_extension(f"discordbot.cogs.__init__")
   bot.load_extension(f"discordbot.cogs.listeners.__init__")

         
app = Flask(__name__)

@app.route("/")
def index():   
   visits = visit()
   return render_template("pages/index.html", visitors=visits)

@app.route("/about")
def about():
   visit()
   return render_template("pages/about.html")

@app.route("/contact")
def contact():
   visit()
   return render_template("pages/contact.html")

@app.route("/admin")
def admin():
   visit()
   return render_template("admin/admin.html")
   
@app.route("/recieveinfo")
def recieveinfo():
   visit()
   code = request.args.get("code")
   resp, access_token = exchange_code(code)
   return render_template("admin/recieveinfo.html", servers=resp, access_token=access_token)

   
@app.route("/adminpage")
def adminpage():
   visit()
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
   

   if Permission == True:
      database = databaseSearch("discordserver", "*", "all")
      print(database)
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

   Perms = getPerms(server["permissions"])
   Perms = str(Perms).replace("[", "").replace("]", "").replace("'", "")
   
   Name = server["name"]
   
   Features = server["features"]
   Features = str(Features).replace("[", "").replace("]", "").replace("'", "")
   
   return render_template("admin/adminpage.html", perms=Perms, name=Name, features=Features, server_id=server_id, database=database)



if __name__ == "__main__":
   loadcogs()
   print("Starting up {} shard{}...".format(bot.shard_count,"" if bot.shard_count == 1 else "s"))
   partial_run = partial(app.run, port=os.getenv("PORT"), debug=False, use_reloader=False)
   t = Thread(target=partial_run)
   t.start()

   bot.run("MTA0MTQxMTY2NjMwMDExNzE1Mw.Gd1dwP.aN9qnEP_A2rKAuHwnINJ3gNYPk59Drsr-RXiAk")
