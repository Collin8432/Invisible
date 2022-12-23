import os
import dotenv
import sys


from hata import Client, wait_for_interruption

dotenv.load_dotenv(".env")

Invisible = Client(os.environ.get("DISCORDTOKEN"))

@Invisible.events
async def ready(client):
    print(f'{client:f} logged in.')

@Invisible.events
async def message_create(client, message):
    if message.author.bot:
        return
    
    if message.content == 'ping':
        await client.message_create(message.channel, 'pong')

Invisible.start()

wait_for_interruption()