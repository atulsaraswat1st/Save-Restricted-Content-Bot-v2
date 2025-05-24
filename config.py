# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = "15578503"
API_HASH = "de14eccfa6fa8d7c2eee9656cc2bdc69"
BOT_TOKEN = "7501679052:AAFhMm4dtaXIcRiY4tBXn54tguj1H9CzCeg"
OWNER_ID = "5525620445"
MONGO_DB = "mongodb+srv://AtulSaraswat1st:Atul@9412@cluster0.qfeqk71.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
LOG_GROUP = "1002663715052"
CHANNEL_ID = "1002663715052"
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
