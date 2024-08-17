
# Python PS5 Price Tracker telegram Bot

This Python script tracks the price of the PlayStation 5 on Amazon and sends a Telegram message with the current price to a specified chat. The script uses `BeautifulSoup` to scrape the price from Amazon and the `python-telegram-bot` library to send messages.

## Features
- **Web Scraping**: Extracts the current price of the PS5 from an Amazon product page.
- **Telegram Integration**: Sends the price to a specified Telegram chat.
- **Chat ID Retrieval**: Provides a helper function to retrieve the `chat_id` of the latest message sent to the bot.

## Prerequisites
- Python 3.x
- Install required libraries:
  ```bash
  pip install requests beautifulsoup4 python-telegram-bot
  ```

## Setup
1. **Telegram Bot**:
   - Create a new bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
   - Obtain your `TOKEN` from BotFather and replace `"YOUR_TELEGRAM_BOT_TOKEN"` in the script.

2. **Chat ID**:
   - Use the `get_chat_id()` function to retrieve your chat ID. Replace `'CHAT_ID'` with this value in the script.

3. **Product URL**:
   - The script is set up to track the PS5. You can replace the `URL_TO_TRACK_PRICE` with the URL of any product you'd like to monitor.

## Usage
- **Track Price**: Run the script to fetch the PS5 price and send it to your Telegram chat.
- **Retrieve Chat ID**: Use the `get_chat_id()` function to fetch the chat ID if needed.

## How to Run
```bash
poetry run python app.py
```

The bot will fetch the current PS5 price and send it to the specified Telegram chat.

## Functions

- **`get_ps5_price(url)`**: Scrapes the price of the PS5 from the provided Amazon URL.
- **`send_message(message)`**: Sends a message to the Telegram chat.
- **`get_chat_id()`**: Retrieves the chat ID from the latest Telegram message sent to the bot.
- **`start()`**: Orchestrates the process of getting the price and sending it as a Telegram message.

## Example Output
```
Message sent!
The current price of PS5 is $499.99
```
