from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt


from utils.db import *
from utils.web import *

def visit():
   visitors = databaseSearch("sitevisitors", "*", "visits")
   visits = int(visitors)
   visits = visits + 1
   databaseUpdate("sitevisitors", {"visits": visits}, "visits", visitors)
   return visits

@csrf_exempt
def login(request):
   cookie = request.COOKIES.get("access_token")
   if cookie is None or cookie.lower() == "none":
      return redirect("https://discord.com/api/oauth2/authorize?client_id=1051162194722685039&redirect_uri=https%3A%2F%2Fincognitobot.ga%2Fadmin%2Fdiscordoauth&response_type=code&scope=guilds")
   else:
      resp = getservers(cookie)
      
   context = {"servers": resp}   
   return render(request, "admin/discordoauth.html", context)

def index(request):
   visits = visit()
   context = {"visitors": visits}
   return render(request, 'pages/index.html', context)

def about(request):
   visit()
   return render(request, "pages/about.html")

def contact(request):
   visit()
   return render(request, "pages/contact.html")

def admin(request):
   visit()
   return render(request, "admin/admin.html")

def discordoauth(request: HttpRequest):
   code = request.GET.get("code")
   print(code)
   resp, access_token = exchange_code(code)
   
   context = {"servers": resp}
   data = render(request, "admin/discordoauth.html", context)
   data.set_cookie("access_token", access_token)
   return data

def authed(request: HttpRequest):
   visit()
   server_id = request.GET.get("server_id")
   access_token = request.COOKIES.get("access_token")
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
      try:
         database = databaseSearchSpecific("discordserver", "*", "server_id", server_id)
      except:
         server_webhook = "Not enough permission and/or guild not in database"
         server_invite = "Not enough permission and/or guild not in database"
         verification_channel_id = "Not enough permission and/or guild not in database"
         verification_role_id = "Not enough permission and/or guild not in database"
         server_membercountvc = "Not enough permission and/or guild not in database"
         welcome_message = "Not enough permission and/or guild not in database"


   Perms = getPerms(server["permissions"])
   Perms = str(Perms).replace("[", "").replace("]", "").replace("'", "")
   
   Name = server["name"]
   
   Features = server["features"]
   Features = str(Features).replace("[", "").replace("]", "").replace("'", "")
   
   try:
      server_webhook = database["server_webhook"]  
      server_invite = database["server_invite"]  
      verification_channel_id = database["verification_channel_id"]  
      verification_role_id = database["verification_role_id"]  
      server_membercountvc = database["server_membercountvc"]  
      welcome_message = database["welcome_message"]
   except:
      pass
   
   context = {
      "perms": Perms,
      "name": Name,
      "features": Features,
      "server_id": server_id,
      "server_webhook": server_webhook,
      "server_invite": server_invite,
      "verification_channel_id": verification_channel_id,
      "verification_role_id": verification_role_id,
      "server_membercountvc": server_membercountvc,
      "welcome_message": welcome_message
   }
   return render(request, "admin/authed.html", context)