#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24178917
API_HASH = "d2cd91eee12f6abb7edb296bb0b416a9"
BOT_TOKEN = "6110125214:AAE7Gc-P1_pyQhFgEyTtU4z0KCCUYGiE3EE"
SESSION = "BQBUwSSJZVZPvLZxIhsgUtkuSeBWHflwNgRC-x1Riuvbk_3n3G_2yOzYM0Eg7n0y3ecpumWqyt9F3nQoejKWtVrzOLihA-FyqkkCDDXMKIcXmdy5mRM7MyhKTKQBByubX5bOLJX4COh8MqOiH687XWZBGjPSzzqJNm5DgOSN81gF2qCkrAG0uuatnfEJBQukFQNVwJcKhcQ-uvni5ocjDPR5JkY4pTur83-Wey5Sr2xct8UAFnmCyIlhLBc5yaxnFJ7VNEk_vMGt9ANzYCD568GjXvCBKfbVlwh7aSCS_HwpJNAEMmPcT32F4NJWXmcoJcSMtX0SXiIMrCeBhuxBbdyKAAAAAWSToswA"
FORCESUB = -1001773945431
AUTH = 5982364364

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
