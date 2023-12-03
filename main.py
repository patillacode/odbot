from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from commands import (
    add_topic,
    ban,
    delete_topic,
    list_topics,
    show,
    start_help,
    whitelist,
    wrong,
)
from config.settings import TELEGRAM_BOT_TOKEN


def run_bot() -> None:
    # Create the Application instance
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # welcome message
    # application.job_queue.run_once(welcome, 5)

    # command handlers
    application.add_handler(CommandHandler("help", start_help))
    application.add_handler(CommandHandler("start", start_help))
    application.add_handler(CommandHandler("whitelist", whitelist))
    application.add_handler(CommandHandler("ban", ban))
    application.add_handler(CommandHandler("show", show))
    application.add_handler(CommandHandler("add", add_topic))
    application.add_handler(CommandHandler("del", delete_topic))
    application.add_handler(CommandHandler("list", list_topics))

    # message handlers
    application.add_handler(MessageHandler(filters.COMMAND, wrong))
    application.add_handler(MessageHandler(filters.TEXT, wrong))
    # application.add_handler(MessageHandler(filters.VOICE, whatever))

    # Run the application
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    run_bot()
