
from telegram import Update
from telegram.ext import ContextTypes

from config.logger import logger
from utils.commands import get_message_and_user
from utils.tg import telegram_bot


async def wrong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"Wrong command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )

    await telegram_bot.send_message(
        text=f"`{message.text.partition(' ')[0]}` is not a valid command. Try /help",
        chat_id=message.chat_id,
        parse_mode="Markdown",
    )

    logger.info("wrong_command command executed successfully")

