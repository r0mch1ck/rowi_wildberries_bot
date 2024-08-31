import asyncio
import logging
from dotenv import load_dotenv
import os
import re
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from search_position import article_position

# Load environment variables from .env file
load_dotenv()

# Configure logging settings
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("bot.log"),
                        logging.StreamHandler()
                    ])

# Create a logger instance
logger = logging.getLogger(__name__)

# Retrieve API keys and bot token from environment variables
logs_key = os.getenv('LOGS_KEY')
bot = Bot(token=os.getenv("TOKEN"))

# Create a dispatcher for handling bot updates
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message):
    """
        This function handles the '/start' command. It logs the user's ID and sends a welcome message.

        Parameters:
        message (aiogram.types.Message): The incoming message object containing the user's ID and command.

        Returns:
        None
        """
    user_id = message.from_user.id
    logger.info(f"User {user_id} issued /start command")
    await message.answer("Hello! This bot helps to determine the position of an article by a given search string")


@dp.message(Command("search"))
async def cmd_search(message, command):
    """
        This function handles the '/search' command. It extracts an article number and a search string from the user's command,
        then calls the 'article_position' function to find the position of the article in a list of articles containing the search string.
        If the article is found, it sends a message with the position. If not, it sends an error message.

        Parameters:
        message (aiogram.types.Message): The incoming message object containing the user's ID and command.
        command (aiogram.types.Command): The command object containing the command and its arguments.

        Returns:
        None
        """
    user_id = message.from_user.id
    logger.info(f"User {user_id} requested article position")

    text = command.args.strip()

    match = re.match(r"(\d+)\s+(.+)", text)

    if match:
        article = int(match.group(1))
        search_string = match.group(2)

        position = article_position(search_string, article)

        if position is None:
            await message.answer("Error! Unable to find the article")
        else:
            await message.answer(f"{position} place")
    else:
        await message.answer("Error! Enter the command in the format: /search <article> <search string>")

@dp.message(Command("log"))
async def cmd_log(message, command):
    """
        This function handles the '/log' command. It checks if the provided key matches the logs key,
        and if so, it sends the bot.log file as a document message.

        Parameters:
        message (aiogram.types.Message): The incoming message object containing the user's ID and command.
        command (aiogram.types.Command): The command object containing the command and its arguments.

        Returns:
        None
        """
    key = command.args
    user_id = message.from_user.id
    if key == logs_key:
        logger.info(f"User {user_id} requested logs")
        file = types.FSInputFile("bot.log")
        await message.answer_document(file)

async def main():
    logger.info("Bot started polling")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot encountered an error: {e}")
    finally:
        logger.info("Bot stopped polling")


if __name__ == "__main__":
    asyncio.run(main())
