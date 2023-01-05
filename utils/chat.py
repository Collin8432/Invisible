import os
import json
import datetime

class Chat:
   def __init__(self):
      date = (datetime.datetime.today().strftime('%Y-%m-%d'))
      if not os.path.exists(path=f"static/chats/chat-{date}.json"):
         with open(f"static/chats/chat-{date}.json", "w") as f:
            f.write("""[
   {
      "Author": "Invisible",
      "Discriminator": "#0000",
      "Content": "Welcome to the Invisible Chat"
   }
]""")
            
   def getChatMessages(self):
      date = (datetime.datetime.today().strftime('%Y-%m-%d'))
      with open(f"static/chats/chat-{date}.json", "r") as f:
         data = json.load(f)
         return data
   
   def addChatMessage(self, author, discriminator, content):
      date = (datetime.datetime.today().strftime('%Y-%m-%d'))

      with open(f"static/chats/chat-{date}.json", "r") as f:
         messages = json.load(f)
      
      with open(f"static/chats/chat-{date}.json", "w") as f:
         new = {
            "Author": author,
            "Discriminator": discriminator,
            "Content": content  
         }

         
         messages.append(new)
         json.dump(messages, f)


chat = Chat()
chat.addChatMessage("f", "f", "ffff")
