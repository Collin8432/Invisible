import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
      conn = sqlite3.connect(db_file)
      return conn
   except Error as e:
      print(e)
   return conn


def insert_into_discordserver(server_webhook, server_id, server_membercountvc, server_invite, verification_channel_id, verificaiton_role_id, welcome_message):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""INSERT INTO DiscordServer(server_webhook, server_id, server_membercountvc, server_invite, verification_channel_id, verificaiton_role_id, welcome_message)
               VALUES("{server_webhook}", "{server_id}", "{server_membercountvc}", "{server_invite}", "{verification_channel_id}", "{verificaiton_role_id}", "{welcome_message}");""")
   conn.commit()
   
def update_discordserver(server_id, data, new):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""UPDATE DiscordServer SET {data} = "{new}" WHERE server_id = {server_id}""")
   conn.commit()
    
def get_discordserver(server_id, data):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""SELECT {data} FROM DiscordServer WHERE server_id = {server_id}""")
   rows = cur.fetchall()
   rows = rows[1]
   return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")
                             
                             
                              
def insert_into_muterole(muterole, server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""INSERT INTO MuteRole(muterole, server_id)
               VALUES("{muterole}", "{server_id}");""")
   conn.commit()
   
def update_muterole(new, server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""UPDATE MuteRole SET muterole = "{new}" WHERE server_id = {server_id}""")
   conn.commit()
   
def get_muterole(server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""SELECT muterole FROM MuteRole WHERE server_id = {server_id}""")
   rows = cur.fetchall()
   return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")
   
   
   
def insert_into_bannedwords(words, server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""INSERT INTO BannedWords(server_id, words)
               VALUES("{server_id}", "{words}");""")
   conn.commit()
   
def update_bannedwords(new, server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""UPDATE BannedWords SET words = "{new}" WHERE server_id = {server_id}""")
   conn.commit()
   
def get_banned_words(server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""SELECT words FROM BannedWords WHERE server_id = {server_id}""")
   rows = cur.fetchall()
   return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")
   
def insert_into_userxp(user_id, user_xp, user_lvl):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""INSERT INTO UserXP(user_id, user_xp, user_lvl)
               VALUES({user_id}, {user_xp}, {user_lvl});""")  
   conn.commit()
   
def update_userxp(user_id, new, condition):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""UPDATE UserXP SET {condition} = "{new}" WHERE user_id = {user_id}""")
   

def rem_from_discordserver(server_id):
   conn = sqlite3.connect("discordbot/utils/db.sqlite3")
   cur = conn.cursor()
   cur.execute(f"""DELETE FROM DiscordServer WHERE server_id = {server_id}""")
   cur.execute(f"""DELETE FROM MuteRole WHERE server_id = {server_id}""")
   cur.execute(f"""DELETE FROM BannedWords WHERE server_id = {server_id}""")
   conn.commit()

   
if __name__ == '__main__':
   ...
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
"""CREATE TABLE DiscordServer (
      server_id varchar(255) NOT NULL,
      server_webhook varchar(255) NOT NULL,
      server_membercountvc varchar(255) NOT NULL,
      server_invite varchar(255) NOT NULL,
      verification_channel_id varchar(255) NOT NULL,
      verificaiton_role_id varchar(255) NOT NULL,
      welcome_message varchar(255) NOT NULL
   ); 
   
    
def task(conn):
   sql = "CREATE TABLE BannedWords(
      server_id INT, 
      words varchar255 NOT NULL
   ); "
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   
def get_banned_words(string):
   string = string.replace("[", "")
   string = string.replace("]", "")
   string = string.replace(",", "")
   string = string.replace('"', '')
   string = string.replace("words = ", "")
   banned_words = string.split()
   return banned_words
   """