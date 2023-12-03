
from config.logger import logger
from config.settings import BOT_ADMIN_CHAT_ID
from utils.tg import telegram_bot


async def inform_admin(unauthorized_message):
    if BOT_ADMIN_CHAT_ID:
        await telegram_bot.send_message(
            text=unauthorized_message,
            chat_id=BOT_ADMIN_CHAT_ID,
            parse_mode="Markdown",
        )
    logger.warning(unauthorized_message.replace("\n", " "))

