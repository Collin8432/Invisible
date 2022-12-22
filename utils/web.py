from operator import contains
import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")


def getPerms(perms: int) -> list:
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

def checkPerms(perms: str) -> bool:
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
   
def exchangeCode(code: str) -> tuple:
   data = {
      "client_id": os.environ.get("DISCORDCLIENTID"),
      "client_secret": os.environ.get("DISCORDSECRET"),
      "grant_type": "authorization_code",
      "code": code,
      "redirect_uri": "https://incognitobot.ga/admin/discordoauth",
      "scope": "identify guild"
   }
   headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
   }
   response = requests.post("https://discord.com/api/v10/oauth2/token", data=data, headers=headers)
   credentials = response.json()
   access_token = credentials["access_token"]
   response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={
      "Authorization": f"Bearer {access_token}"
   })
   resp = response.json()
   return resp, access_token

def getServers(cookie) -> dict:
   response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={
      "Authorization": f"Bearer {cookie}"
   })
   resp = response.json()
   return resp