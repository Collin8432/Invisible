from django.shortcuts import render, redirect
from django.http import HttpRequest

from autocorrect import Speller

spell = Speller(lang='en')


from typing import Any

from utils.db import *
from utils.web import *
from utils.chat import *

def visit() -> int:
   visitors = databaseSearch("sitevisitors", "*", "visits")
   visits = int(visitors)
   visits = visits + 1
   databaseUpdate("sitevisitors", {"visits": visits}, "visits", visitors)
   return visits
      
def index(request) -> Any:
   visits = visit()
   context = {"visitors": visits}
   return render(request, 'main/index.html', context)


def discordoauth(request: HttpRequest) -> Any:
   code = request.GET.get("code")
   if code is not None:
      print("cnn")
      resp, access_token = exchangeCode(code)
      context = {"servers": resp}
      data = render(request, "admin/discordoauth.html", context)
      data.set_cookie("access_token", access_token)
      return data
   else:
      try:
         cookie = request.COOKIES.get("access_token")
         context = getServers(cookie)
         for server in context:
            Perms = getPerms(server["permissions"])
            Perms = str(Perms).replace("[", "").replace("]", "").replace("'", "")
            Features = server["features"]
            Features = str(Features).replace("[", "").replace("]", "").replace("'", "")
            server["features"] = Features
            server["permissions"] = Perms
            
         context = {"servers": context}
         data = render(request, "admin/discordoauth.html", context)
         return data
      except Exception as e:
         print(e)
         # return redirect("https://discord.com/api/oauth2/authorize?client_id=1051162194722685039&redirect_uri=https%3A%2F%2FInvisiblebot.ga%2Fadmin%2Fdiscordoauth&response_type=code&scope=guilds%20identify")
         return redirect("https://discord.com/api/oauth2/authorize?client_id=1051162194722685039&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fadmin%2Fdiscordoauth&response_type=code&scope=guilds%20identify")

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

            
   if server["owner"]: # type: ignore
      Permission = True
   else:
      Permission = checkPerms(server["permissions"]) # type: ignore
   

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


   Perms = getPerms(server["permissions"]) # type: ignore
   Perms = str(Perms).replace("[", "").replace("]", "").replace("'", "")
   
   Name = server["name"] # type: ignore
   
   Features = server["features"] # type: ignore
   Features = str(Features).replace("[", "").replace("]", "").replace("'", "")
   
   try:
      server_webhook = database["server_webhook"]   # type: ignore
      server_invite = database["server_invite"]   # type: ignore
      verification_channel_id = database["verification_channel_id"]   # type: ignore
      verification_role_id = database["verification_role_id"]   # type: ignore
      server_membercountvc = database["server_membercountvc"]   # type: ignore
      welcome_message = database["welcome_message"] # type: ignore
   except:
      server_webhook = "Not enough permission and/or guild not in database"
      server_invite = "Not enough permission and/or guild not in database"
      verification_channel_id = "Not enough permission and/or guild not in database"
      verification_role_id = "Not enough permission and/or guild not in database"
      server_membercountvc = "Not enough permission and/or guild not in database"
      welcome_message = "Not enough permission and/or guild not in database"
   
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

def search(request):
   homepage = {
      "name": "Website Homepage",
      "href": "/",
      "description": "The website homepage, including the about and contact sections"
   }
   
   adminpage = {
      "name": "Admin Page",
      "href": "/admin/discordoauth",
      "description": "The admin page for the discord dashboard"
   }
   
   nonepage = {
      "name": "No Results Found",
      "href": "/",
      "description": "No results found, Click to return to the homepage"
   }
   
   mainpages = ["main", "home", "index", "default"]
   adminpages = ["admin", "database", "dashboard", "administrator", "manager", "execuitive", "director", "superintendent", "dash"]
   
   q = request.GET.get("q")
   print(q)
   q = spell(q)
   print(q)
   q = q.lower()
   print(q)

   if q in mainpages:
      print("main")
      context = homepage
   elif q in adminpages:
      print("admin")
      context = {
         "name": "Admin Page",
         "href": "/admin/discordoauth",
         "description": "The admin page for the discord dashboard"
      }
      print(context)
   else:
      context = nonepage
      
   return render(request, "main/search.html", context)

def searching(request):
   if request.method == "POST":
      search = request.POST.get('search_input', None)
      return redirect(f"/search?q={search}")

def chat(request):
   chat = Chat()
   messages = chat.getChatMessages()
   code = request.GET.get("code")
   
   if code is not None:
      resp, access_token = exchangeCodeChat(code)
      context = {"user": resp, "messages": messages}
      data = render(request, "chat/chat.html", context)
      data.set_cookie("access_token", access_token)
      return data
   else:
      try:
         cookie = request.COOKIES.get("access_token")
         context = getSelfUser(cookie)
         context = {"user": context, "messages": messages}
         return render(request, "chat/chat.html", context)
      except:
         return redirect("https://discord.com/api/oauth2/authorize?client_id=1051162194722685039&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fchat&response_type=code&scope=identify")
         # return redirect("https://discord.com/api/oauth2/authorize?client_id=1051162194722685039&redirect_uri=https%3A%2F%2Fincognitobot.ga%2Fchat&response_type=code&scope=identify")
   
