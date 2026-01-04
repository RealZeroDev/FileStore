# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github
# Released under the MIT License

import os
import logging
from logging.handlers import RotatingFileHandler

# ================== TELEGRAM API CONFIG ==================
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "28449420"))  # Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "608b71c13cec20da6662327fa1fc7d35")  # Your API Hash from my.telegram.org

# ================== CHANNEL / OWNER CONFIG ==================
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002753638629"))  # Your db channel Id
OWNER = os.environ.get("OWNER", "RealZeroking")  # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "6819408964"))  # Owner id

# ================== DATABASE CONFIG ==================
PORT = os.environ.get("PORT", "8001")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://thezerodev:GtiCjva8tQnD1PRN@cluster0.t9gtmbv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "thezerodev")

# ================== BOT SETTINGS ==================
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/ZeroNetBots")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b68ad5167c77e15439d44.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/3fe52b8f4fe34349f6c58.jpg")

# ================== MESSAGES ==================
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n<blockquote>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴠɪᴅᴇ ʟɪɴᴋs ғᴏʀ ᴏᴛʜᴇʀs.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ʀᴇʟᴏᴀᴅ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ.</b>")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ-ᴛᴏ-ʟɪɴᴋ ʙᴏᴛ\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├ /start : start bot\n├ /about : about us\n└ /help : help</b>"
ABOUT_TXT = "<b>◈ Creator: <a href=https://t.me/RealZeroking>ᴢᴇʀᴏ</a>\n◈ Network: <a href=https://t.me/ZeroNetHQ>ᴢᴇʀᴏ ɴᴇᴛᴡᴏʀᴋ</a></b>"

CMD_TXT = """<b>» Admin Commands:</b>

/dlt_time - set auto delete time
/check_dlt_time - check delete time
/dbroadcast - broadcast doc/video
/ban - ban user
/unban - unban user
/banlist - list banned users
/addchnl - add force sub channel
/delchnl - remove force sub channel
/listchnl - list force sub channels
/fsub_mode - toggle force sub mode
/pbroadcast - send photo broadcast
/add_admin - add admin
/deladmin - remove admin
/admins - list admins
/delreq - remove leftover requests
"""

# ================== FILE SETTINGS ==================
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @ZeroNetDrama</b>")
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ !!"

# ================== LOGGING ==================
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
