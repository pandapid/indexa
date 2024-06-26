from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "26796802"))
    API_HASH = getenv("API_HASH", "b8cc96196eb105c33d8ce193e5efff5c")
    BOT_TOKEN = getenv("BOT_TOKEN", "6478225213:AAH8oATDQxRF8V6ZnVtjkDhPl8BXe-X_94k")
    PORT = int(getenv("PORT", "8080"))
    BASE_URL = getenv("BASE_URL", "https://indexa-5ec7a8c430f7.herokuapp.com/").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://Eln:Chaik2501@cipid.4whqkv9.mongodb.net/")
    AUTH_CHANNEL = [channel.strip()
                    for channel in getenv("AUTH_CHANNEL").split(",")]
    THEME = getenv("THEME", "quartz")
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
