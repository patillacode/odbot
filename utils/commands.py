from telegram import ForceReply, Update
from telegram.ext import ContextTypes

from config.logger import logger


def get_command_list() -> str:
    return (
        "\n\t/add <topic>: Añadir un tema a la lista.\n"
        "\t/del <topic>/<all>: Eliminar un tema de la lista. <all> para borrar todo\n"
        "\t/list: Listar todos los temas.\n"
        "\t/help: Mostrar mensaje de ayuda.\n"
    )


def get_message_and_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if getattr(update, "callback_query", None):
        message = update.callback_query.message
        user = update.effective_user
    else:
        message = update.message
        user = update.effective_user
    return message, user


async def select_forced_reply_for_command(message, user, command):
    messages = {
        "command": (rf"Vale, vamos a intentarlo {user.mention_html()}...\n"),
    }
    if command not in messages:
        logger.error(f"Unknown command to force reply upon: {command}")
        return
    await message.reply_html(
        (messages[command]), reply_markup=ForceReply(selective=True)
    )


async def force_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message, user = get_message_and_user(update, context)
    command = update.callback_query.data
    logger.info(
        f"{command} (force_reply) command received from user "
        f"{user.first_name} (chat_id: {message.chat_id})"
    )
    reply = await select_forced_reply_for_command(message, user, command)
    if reply:
        await message.reply_html(
            reply,
            reply_markup=ForceReply(selective=True),
        )
        logger.info("Force reply message sent")
