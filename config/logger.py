
import logging

from logging.handlers import RotatingFileHandler

import config.ic_setup  # noqa: F401

from config.settings import BASE_DIR, LOG_LEVEL

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            f"{BASE_DIR}/logs/odbot.log", maxBytes=1000000, backupCount=3
        ),
        logging.StreamHandler(),
    ],
)
# set logging level to WARNING for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("odbot").setLevel(logging.getLevelName(LOG_LEVEL))

logger = logging.getLogger("odbot")

