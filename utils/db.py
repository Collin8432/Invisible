import os
from supabase import create_client, Client
SUPABASE_URL="https://xyowqbyxqtypxzhqtpyu.supabase.co"
from dotenv import load_dotenv
load_dotenv(".env")
SUPABASE_KEY=os.environ.get("SUPABASEKEY")
url: str = SUPABASE_URL
key: str = SUPABASE_KEY



def databaseInsert(table: str, data: dict): 
   supabase: Client = create_client(url, key)
   data = supabase.table(table).insert(data).execute()
   assert len(data.data) > 0

def databaseSearch(table: str, select: str, info: str):
   supabase: Client = create_client(url, key)
   data = supabase.table(f"{table}").select(f"{select}").execute()
   assert len(data.data) > 0
   if info.lower() == "all":
      return data.data[0]
   else:
      return data.data[0][info]

def databaseSearchSpecific(table: str, select: str, what: str, isequaltoo: str):
   supabase: Client = create_client(url, key)
   data = supabase.table(f"{table}").select(select).eq(what, isequaltoo).execute()
   assert len(data.data) > 0
   if select.lower() == "*":
      return data.data[0]
   else:
      return data.data[0][select]


def databaseUpdate(table: str, data: dict, what: str, isequaltoo: str):
   supabase: Client = create_client(url, key)
   data = supabase.table(table).update(data).eq(what, isequaltoo).execute()
   assert len(data.data) > 0

def databaseDelete(table: str, what: str, isequaltoo: str):
   supabase: Client = create_client(url, key)
   data = supabase.table(table).delete().eq(what, isequaltoo).execute()
   assert len(data.data) > 0






# conn = psycopg2.connect(
#     host="db.xyowqbyxqtypxzhqtpyu.supabase.co",
#     database="postgres",
#     user="postgres",
#     password="Cash22741!?!?",
#     port="5432"
# )


# cur = conn.cursor()

# def create_conn():
#    return psycopg2.connect(
#     host="db.xyowqbyxqtypxzhqtpyu.supabase.co",
#     database="postgres",
#     user="postgres",
#     password="Cash22741!?!?",
#     port="5432"
# )

# def insert_into_discordserver(server_webhook, server_id, server_membercountvc, server_invite, verification_channel_id, verificaiton_role_id, welcome_message):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""INSERT INTO DiscordServer(server_webhook, server_id, server_membercountvc, server_invite, verification_channel_id, verificaiton_role_id, welcome_message)
#                VALUES('{server_webhook}', {server_id}, {server_membercountvc}, '{server_invite}', {verification_channel_id}, {verificaiton_role_id}, '{welcome_message}');""")
#    conn.commit()
   
# def update_discordserver(server_id, data, new):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""UPDATE DiscordServer SET {data} = "{new}" WHERE server_id = {server_id}""")
#    conn.commit()
    
# def get_discordserver(server_id, data):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""SELECT {data} FROM DiscordServer WHERE server_id = '{server_id}'""")
#    rows = cur.fetchall()
#    return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")           
      
               
# def insert_into_muterole(muterole, server_id):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""INSERT INTO MuteRole(muterole, server_id)
#                VALUES({muterole}, {server_id});""")
#    conn.commit()
   
# def update_muterole(new, server_id):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""UPDATE MuteRole SET muterole = "{new}" WHERE server_id = {server_id}""")
#    conn.commit()
   
# def get_muterole(server_id):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""SELECT muterole FROM MuteRole WHERE server_id = '{server_id}'""")
#    rows = cur.fetchall()
#    return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")
   

# def insert_into_userxp(user_id, user_xp, user_lvl):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""INSERT INTO UserXP(user_id, user_xp, user_lvl)
#                VALUES({user_id}, {user_xp}, {user_lvl});""")  
#    conn.commit()
   
# def update_userxp(user_id, new, condition):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""UPDATE UserXP SET {condition} = "{new}" WHERE user_id = {user_id}""")
   
# def rem_from_discordserver(server_id):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""DELETE FROM DiscordServer WHERE server_id = '{server_id}'""")
#    cur.execute(f"""DELETE FROM MuteRole WHERE server_id = '{server_id}'""")
#    conn.commit()

# def get_sitevisitors():
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""SELECT visits FROM SiteVisitors""")
#    rows = cur.fetchall()
#    return str(rows).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")

# def insert_into_sitevisitors():
#    conn = create_conn()
#    cur = conn.cursor()
#    s=get_sitevisitors()
#    s = int(s)
#    num = s + 1
#    cur.execute(f"""UPDATE SiteVisitors SET visits = '{num}'""")
#    conn.commit()


# def webget(server_id):
#    conn = create_conn()
#    cur = conn.cursor()
#    cur.execute(f"""SELECT * FROM DiscordServer WHERE server_id = '{server_id}'""")
#    rows = cur.fetchall()
#    return rows
   



# cur.execute("""CREATE TABLE DiscordServer(
#     server_id varchar(255) NOT NULL,
#     server_webhook varchar(255) NOT NULL,
#     server_membercountvc varchar(255) NOT NULL,
#     server_invite varchar(255) NOT NULL,
#     verification_channel_id varchar(255) NOT NULL,
#     verificaiton_role_id varchar(255) NOT NULL,
#     welcome_message varchar(255) NOT NULL
# )""")

# cur.execute("""CREATE TABLE UserXP(
#     user_id varchar(255) NOT NULL,
#     user_xp varchar(255) NOT NULL,
#     user_lvl varchar(255) NOT NULL 
# )""")

# cur.execute("""CREATE TABLE MuteRole(
#     server_id varchar(255) NOT NULL,
#     muterole varchar(255) NOT NULL
# )""")

# cur.execute("""CREATE TABLE SiteVisitors(
#     visits varchar(255) NOT NULL
# )""")


# conn.commit()
