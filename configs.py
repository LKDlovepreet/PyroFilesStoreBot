# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "20408350"))
	API_HASH = os.environ.get("5a82fc4cdb04d5874b77e902ba903271")
	BOT_TOKEN = os.environ.get("7096813003:AAFgmqcS2OQHRUe3xKurLCnpiuaOb6nVm4Q")
	BOT_USERNAME = os.environ.get("LKDFILESHARING_01_BOT")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002148823393"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7372840699"))
	DATABASE_URL = os.environ.get("mongodb+srv://singhlovepreet05198:K6wo5uVJ1PmKl2Li@lkdfilesharing.j5g5msi.mongodb.net/?retryWrites=true&w=majority&appName=LKDFILESHARING")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002162688170")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://filesstorebot-pmoo.onrender.com")
sync

eventlet - Requires eventlet >= 0.24.1 (or install it via pip install gunicorn[eventlet])

gevent - Requires gevent >= 1.4 (or install it via pip install gunicorn[gevent])

tornado - Requires tornado >= 0.2 (or install it via pip install gunicorn[tornado])

gthread - Python 2 requires the futures package to be installed (or install it via pip install gunicorn[gthread])
