#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌

# Add your details here and then deploy by clicking on HEROKU Deploy button

import os

from os import environ



API_ID = int(environ.get("API_ID", "31815314"))

API_HASH = environ.get("API_HASH", "480160a314cf23e90f8b9bd89368959a")

BOT_TOKEN = environ.get("BOT_TOKEN", "8510187991:AAHd-YtLtrU8M8APaGQRjKVpCqlcq89Auss")

OWNER = int(environ.get("OWNER", "7674277191"))

CREDIT = "₹🌐STRANGER🙋‍♂️💠"

AUTH_USER = os.environ.get('AUTH_USERS', '7674277191').split(',')

AUTH_USERS = [int(user_id) for user_id in AUTH_USER]

if int(OWNER) not in AUTH_USERS:

    AUTH_USERS.append(int(OWNER))

  

#WEBHOOK = True  # Don't change this

#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

