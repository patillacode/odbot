import os

from telegram.ext import ContextTypes

from config.logger import logger
from config.settings import TOPIC_LISTS_FOLDER_PATH


def set_topics(context: ContextTypes.DEFAULT_TYPE) -> None:
    if "topics" not in context.user_data:
        logger.debug("Setting topics to empty list")
        context.user_data["topics"] = []


def write_topic_to_list(topic, chat_id, user) -> None:
    file_name = f"{TOPIC_LISTS_FOLDER_PATH}/{chat_id}_{user}.txt"
    logger.debug(f"Writing topic to {file_name}")

    if not os.path.exists(file_name):
        logger.debug(f"Creating file {file_name}")
        with open(file_name, "w") as file:
            file.write("")

    with open(file_name, "a") as file:
        file.write(f"{topic}\n")

    return True


def delete_topic_from_list(topic, chat_id, user) -> None:
    file_name = f"{TOPIC_LISTS_FOLDER_PATH}/{chat_id}_{user}.txt"
    logger.debug(f"Deleting topic from {file_name}")
    found = False

    if not os.path.exists(file_name):
        logger.debug(f"File {file_name} doesn't exist")
        return False

    if topic == "all":
        logger.debug("Deleting all topics")
        with open(file_name, "w") as file:
            file.write("")
        return True

    with open(file_name, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip("\n") != topic:
                file.write(line)
            else:
                found = True

        file.truncate()

    return found


def list_topics_from_list(chat_id, user) -> None:
    file_name = f"{TOPIC_LISTS_FOLDER_PATH}/{chat_id}_{user}.txt"
    logger.debug(f"Listing topics from {file_name}")

    if not os.path.exists(file_name):
        logger.debug(f"File {file_name} doesn't exist")
        return []

    with open(file_name, "r") as file:
        topics = file.readlines()
        return topics
