import asyncio
from random import choice
from threading import Thread as th
from telethon import TelegramClient
from telethon.events import NewMessage
from colorama import init, Fore
import os
init()

APP_ID = 9790192
API_HASH = 'a0fca3da6a7a2dfc65346805af8b9998'
EDIT_DELAY = 0.01

songFiles = os.listdir('songs')
magic_frases = []
songs = {}
for song in songFiles:
    with open('songs/' + song, 'r') as f:
        songs.update({song[:-4]:list(f.read().split('\n'))})
        magic_frases.append(song[:-4])


client = TelegramClient('tg-account', APP_ID, API_HASH)

async def signify(event: NewMessage.Event, song):
    for string in song:
        await client.edit_message(event.peer_id.user_id, event.message.id, string)
        await asyncio.sleep(0.9)

@client.on(NewMessage(outgoing=True))
async def handle_message(event: NewMessage.Event):
    global magic_frases, songs
    message = event.message.message
    if message in magic_frases:
        await signify(event,songs[message])

if __name__ == '__main__':
    print(Fore.BLUE + '[*] Connecting to Telegram ACOUNT...')
    client.start()
    print(Fore.GREEN + '[+] Successfully connected')
    print(Fore.RED)
    client.run_until_disconnected()
