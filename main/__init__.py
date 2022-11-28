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
SESSION = "BQB3cyqcYXRZXXgHboacYpRnlPGOIJAvgmaJ-QAyLsexfynE-Txa08RbWaRn-jFdOf4qvdU-ee9ZmiiafTbZ94XWvgCDdWcjTkvoIbwv1tWqPfwxLxzCRGHRGTN4yLS6So-alHv8cCnuWZVR4HvI209fWArSOuvEoXWJAsYEqgyMKmjVZXxmcIxkZzV0w3NELd9QCG1b3cXoJSqEr-E91NYSWXvtnVjOuiFCg75ydshTZbiCwF77bij8kcXNFoAbfGEXbyGdmRC1ga3b9cMnoLbk2j2SiauxtImYPgWMLOsllIks472Z1DT7PbKHTeyVrC118YieZX9H3LfPK0RWf_7FAAAAAU71gHgA"
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
