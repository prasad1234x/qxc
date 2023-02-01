#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 24178917)
API_HASH = config("API_HASH", "d2cd91eee12f6abb7edb296bb0b416a9")
BOT_TOKEN = config("BOT_TOKEN", "6110125214:AAE7Gc-P1_pyQhFgEyTtU4z0KCCUYGiE3EE")
SESSION = config("SESSION", "BQBeIWH6vB-KHKpK6lulCffq4n7zfC5KkyQ-WKYA-CIR0vm-zdRSYHBWKQNo-31PMYp31hc3333rAbzrFtUr3NfH9S21xva018SH_eC90q1iOf8kRSwYIFIi--B1OyUxowqOOJghyFMY3tWBylou1cv8xoTePVz2fLJ7GMBWHIaWnTqpApZ75h6tcZVrkgKq2CjPhARwS9v6sKuJXeX3KEnx8ZZsnWYAHYcNoJ_0ThTU3EOqaKx1qm3Eix48al84ne67rjs7BzzsNKnNcPom5km3gFVRsCMpzQmeC5-ToQMixkCG8UhMe0ec1tImISk5y2BqJLuuHDE2aBfV8g1dPjqxAAAAAWSToswA")
FORCESUB = config("FORCESUB", -1001773945431)
AUTH = config("AUTH", 5982364364)

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
