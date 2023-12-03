from telegram import Update
from telegram.ext import ContextTypes

from config.logger import logger
from utils.commands import get_command_list, get_message_and_user
from utils.decorators import only_whitelist
from utils.topics import set_topics


@only_whitelist
async def add_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"add_topic command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )
    set_topics(context)
    _, _, topic = message.text.partition(" ")
    if topic:
        context.user_data["topics"].append(topic)
        await update.message.reply_text(f"'{topic}' añadido a la lista")
    else:
        await update.message.reply_text(f"Debes añadir un tema.\n{get_command_list()}")


@only_whitelist
async def delete_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"delete_topic command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )
    set_topics(context)
    _, _, topic = message.text.partition(" ")
    if topic == "all":
        context.user_data["topics"] = []
        await update.message.reply_text(
            "Todos los temas han sido eliminados de la lista."
        )

    elif topic in context.user_data["topics"]:
        context.user_data["topics"].remove(topic)
        await update.message.reply_text(f"'{topic}' eliminado de la lista.")

    else:
        await update.message.reply_text(
            f"'{topic}' no está en la lista.\n{get_command_list()}"
        )


@only_whitelist
async def list_topics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    logger.info(
        f"list_topics command received from user {user.first_name} (@{user.username}) "
        f"(chat_id: {message.chat_id})"
    )
    set_topics(context)
    topics = context.user_data.get("topics", [])
    if topics:
        await update.message.reply_text("\n".join([f"- {topic}" for topic in topics]))
    else:
        await update.message.reply_text(
            f"Todavía no hay ninguna orden del día.\n{get_command_list()}"
        )
