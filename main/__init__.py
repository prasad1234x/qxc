#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28123666
API_HASH = "e0a07eff8e5ff1dd72edcac6bb213a42"
BOT_TOKEN = "5638540601:AAE_Rm3_aYp2Lerc2KJyI8XwaqHDBeuptx0"
SESSION = "BQCwPsWsG-jS7wOfzX6JuWhm_-0eeNxAO_gXtrVyXsQfsRYurr__xa4zowWT2cqCB-LJYHV6hfNPhhJDiY2x9VHYbfbmnEvozp60CSz_shY2GN0ts48GzPy24EfF2rG36QrZkSlnK9baAyqLvV0gx3yQ1c3hNjC7UBz0Jr-hYaLOzgKuk0jc_6NBv1yG_9C4TD2qPq9w4Y81Lwj0gOYfJwMtyBtsrXbtsd2l8pxqaOdQc3J8xKFQBwaw1M5Pvy-mQINRhkVPc9MXNuYctuKFnCLVqy0AQWmxMVVffriA0SokUYLDJc3-o0LsGvEwK5CeZZerBppFfgVOTS4VY27AtTe5AAAAAU71gHgA"
FORCESUB = "asdadsadfa"
AUTH = 5619679352

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
