
from telegram import Update
from telegram.ext import ContextTypes

from config.logger import logger
from config.settings import WHITELIST_FILE_PATH
from utils.commands import get_message_and_user
from utils.decorators import only_admins
from utils.tg import telegram_bot


@only_admins
async def whitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    _, _, user_to_whitelist = update.message.text.partition(" ")
    logger.info(
        f"Whitelist command received from user {user.first_name} (@{user.username}) "
        f"to add {user_to_whitelist} to the whitelist (chat_id: {message.chat_id})"
    )
    found = False
    if not user_to_whitelist:
        await telegram_bot.send_message(
            text="Usage: /whitelist <username> (without @)",
            chat_id=message.chat_id,
            parse_mode="Markdown",
        )
        return

    with open(WHITELIST_FILE_PATH, "r") as f:
        for line in f.readlines():
            if user_to_whitelist in line:
                logger.debug(f"Found username {user.username} in whitelist already!")
                await telegram_bot.send_message(
                    text=f"User @{user.username} already in the whitelist! Skipping...",
                    chat_id=message.chat_id,
                    parse_mode="Markdown",
                )
                found = True

    if not found:
        with open(WHITELIST_FILE_PATH, "a") as f:
            f.write(f"{user_to_whitelist}\n")

        await telegram_bot.send_message(
            text=f"Added @{user_to_whitelist} to whitelist! They can now use the bot!",
            chat_id=message.chat_id,
            parse_mode="Markdown",
        )

    logger.info("Whitelist command executed successfully")


@only_admins
async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    _, _, user_to_ban = update.message.text.partition(" ")
    logger.info(
        f"Ban command received from user {user.first_name} (@{user.username}) "
        f"to ban {user_to_ban} (chat_id: {message.chat_id})"
    )

    found = False
    users_to_keep = []
    if not user_to_ban:
        await telegram_bot.send_message(
            text="Usage: /ban <username> (without @)",
            chat_id=message.chat_id,
            parse_mode="Markdown",
        )
        return

    logger.warning(f"User to ban: {user_to_ban}")

    with open(WHITELIST_FILE_PATH, "r") as f:
        for line in f.readlines():
            if f"{user_to_ban}\n" == line:
                found = True
                logger.debug(f"Found username {user_to_ban} to be banned!")
            else:
                users_to_keep.append(line)

    with open(WHITELIST_FILE_PATH, "w"):
        pass

    with open(WHITELIST_FILE_PATH, "w") as f:
        for user in users_to_keep:
            f.write(user)

    if found:
        await telegram_bot.send_message(
            text=(
                f"Removed @{user_to_ban} from whitelist! They can no longer use the bot."
            ),
            chat_id=message.chat_id,
            parse_mode="Markdown",
        )
    else:
        await telegram_bot.send_message(
            text=f"User @{user_to_ban} was not found in whitelist! Skipping...",
            chat_id=message.chat_id,
            parse_mode="Markdown",
        )

    logger.info("Ban command executed successfully")


@only_admins
async def show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"Show whitelist command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )

    with open(WHITELIST_FILE_PATH, "r") as f:
        whitelist = f.read()

    await telegram_bot.send_message(
        text=f"Whitelist:\n\n{whitelist}",
        chat_id=message.chat_id,
        parse_mode="Markdown",
    )

    logger.info("Show whitelist command executed successfully")

