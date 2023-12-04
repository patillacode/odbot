import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WHITELIST_FILE_PATH = f"{BASE_DIR}/config/whitelist.txt"
TOPIC_LISTS_FOLDER_PATH = f"{BASE_DIR}/lists"

BOT_ADMIN_USERNAME = os.environ.get("BOT_ADMIN_USERNAME")
BOT_ADMIN_CHAT_ID = os.environ.get("BOT_ADMIN_CHAT_ID", None)

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

ENVIRONMENT = os.environ.get("ENVIRONMENT", "PRODUCTION")
