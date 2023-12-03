from telegram import Update
from telegram.ext import ContextTypes

from config.logger import logger
from config.settings import BOT_ADMIN_USERNAME
from utils.commands import get_command_list, get_message_and_user
from utils.decorators import only_whitelist
from utils.tg import telegram_bot


@only_whitelist
async def start_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"Help command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )
    help_message = "*¡Bienvenid@ a odbot!*\n\n"
    help_message += get_command_list()
    if user.username == BOT_ADMIN_USERNAME:
        help_message += (
            "\n\n"
            "*Comandos de administrador*\n\n"
            "- /whitelist <username>: Añade a un usuario a la whitelist, "
            "de modo que pueda usar el bot aunque no esté en el grupo.\n"
            "- /ban <username>: Banea a un usuario, de modo que no pueda usar el bot.\n"
            "- /show: Muestra los usuarios de la whitelist.\n"
        )

    await telegram_bot.send_message(
        text=help_message, chat_id=message.chat_id, parse_mode="Markdown"
    )
    logger.info("Help/Start message sent")
