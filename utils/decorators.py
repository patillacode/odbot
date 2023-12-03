
import os

from config.logger import logger
from config.settings import BOT_ADMIN_USERNAME, WHITELIST_FILE_PATH
from utils.admin import inform_admin
from utils.tg import telegram_bot


def only_whitelist(func):
    async def wrapper(*args, **kwargs):
        update = args[0]
        chat_id = update.message.chat.id
        username = update.effective_user.username

        if not os.path.exists(WHITELIST_FILE_PATH):
            logger.debug("No whitelist defined. Running function.")
            return await func(*args, **kwargs)

        with open(WHITELIST_FILE_PATH, "r") as f:
            for line in f.readlines():
                if username in line:
                    logger.debug(
                        f"Found username {username} in whitelist. Running command "
                        f"{func.__name__}"
                    )
                    return await func(*args, **kwargs)

        await telegram_bot.send_message(
            text=(
                f"Lo siento {username}... no tienes acceso a este bot...\n"
                "Pídele a @dvitto que te dé acceso."
            ),
            chat_id=chat_id,
        )

        unauthorized_message = (
            f"*Unauthorized user* with username: @{username} is trying to "
            f"use the odbot.\n"
            f"Run `/whitelist {username}` to give them access."
        )
        await inform_admin(unauthorized_message)

        return False

    return wrapper


def only_admins(func):
    async def wrapper(*args, **kwargs):
        update = args[0]
        username = update.effective_user.username
        if username == BOT_ADMIN_USERNAME:
            logger.debug(
                f"Found username {username} in admin list. Running admin-only command. "
                f"{func.__name__}"
            )
            return await func(*args, **kwargs)

        unauthorized_message = (
            f"*Unauthorized user* with username: @{username} is trying to use "
            f"admin commands ({func.__name__}) in the odbot"
        )
        await inform_admin(unauthorized_message)

        await telegram_bot.send_message(
            text=f"Fuck off @{username} 🖕🏻",
            chat_id=update.message.chat.id,
            parse_mode="Markdown",
        )
        return False

    return wrapper

