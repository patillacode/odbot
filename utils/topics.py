from telegram.ext import ContextTypes

from config.logger import logger


def set_topics(context: ContextTypes.DEFAULT_TYPE) -> None:
    if "topics" not in context.user_data:
        logger.debug("Setting topics to empty list")
        context.user_data["topics"] = []
