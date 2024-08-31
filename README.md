# Wildberries Search Telegram Bot

## Overview

**Wildberries Rowi Bot** is a Telegram bot designed to search for products on the Wildberries platform. The bot offers two primary functions:

1. **/start** - Sends a welcome message to the user.
2. **/search <article> <string>** - Searches for products by the specified article number and search string using Wildberries' hidden API.

## Features

### /start
- **Description**: Sends a welcome message to the user. This command initializes interaction with the bot.
- **Usage**: Simply type `/start` in the chat with the bot.

### /search <article> <string>
- **Description**: Allows you to search for products by article number within the results of a search string.
- **Parameters**:
  - `<article>`: The product article number (an integer).
  - `<string>`: The search string (words or phrases).
- **Usage**: Enter `/search <article> <string>`. For example, `/search 123456 children's bicycle`.
- **Details**: The bot operates through Wildberries' hidden API, requiring a request to be made on behalf of a seller to access the data.

## Example Usage

- Start interaction with the bot by sending the command `/start`.
- Use the `/search` command to find products:

    ```bash
    /search 123456 children's bicycle
    ```

  The bot will perform the search and return results if the article is found within the search results for the specified string.

## Dependencies

- **Aiogram**: Framework for creating Telegram bots in Python.
- **Python-dotenv**: Manage environment variables from a `.env` file.

## Notes

- The bot utilizes Wildberries' hidden API for search queries. To use Wildberries' official API, registration as a seller is required.

## Bot Link

[Wildberries Rowi Bot](https://t.me/wildberries_rowi_bot)
