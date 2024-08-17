from bs4 import BeautifulSoup
from telegram import Bot
import requests
import asyncio

# Telegram bot token and chat ID
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your actual bot token
CHAT_ID = 'CHAT_ID'  # Your chat ID for receiving messages

# Initialize the bot
bot = Bot(token=TOKEN)

# URL of the product to track
URL_TO_TRACK_PRICE = 'https://www.amazon.com/PlayStation-5-Digital/dp/B09DFHJTF5/ref=sr_1_1?crid=28SJS2Y5SABVY&dib=eyJ2IjoiMSJ9.czOVbXlAu7Jf8Ts4SpNxUuUSip0z5QBAz1EJj3_WoOwIa3PHEUX_pxtIDmXMmfwWf8e4s7wd8s2HrBmkrnSGknmHyD_MWHKjFKtKb1oBwIuxnS0mAiG5nDBkzDic4NO29lYzwPb51vAEexgqk6ucnBlD9yn2TAQICriwUV_4NILK5EeWR2KoccmPRqGbE9mwhClwzQaXefOPkMgp06qIOT3kpK50J34vqLllVLXN4oU._y6n1oL5fM6-pawjCBmOurUQsQ3ZZPqsJF4ejToNJwk&dib_tag=se&keywords=ps5&qid=1723780283&sprefix=ps%2Caps%2C438&sr=8-1&th=1'

def get_ps5_price(url):
    """
    Fetch the price of the PS5 from the provided URL.
    """
    headers = {"User-Agent": "Mozilla/5.0"}  # Headers to mimic a browser request
    page = requests.get(url, headers=headers)  # Send a GET request to the URL
    soup = BeautifulSoup(page.content, "html.parser")  # Parse the HTML content using BeautifulSoup
    price = soup.find("span", class_="a-offscreen").text  # Extract the price from the specific HTML element
    return price

async def send_message(message):
    """
    Send a message to the specified Telegram chat.
    """
    await bot.send_message(chat_id=CHAT_ID, text=message)  # Send the message using the bot
    print("Message sent!")

def get_chat_id():
    """
    Fetch updates from the bot and return the chat ID of the latest message.
    """
    # Get updates from the bot
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()

    # Extract chat ID from the latest update
    try:
        updates = response.get("result", [])
        if updates:
            latest_update = updates[-1]  # Get the latest update
            chat_id = latest_update["message"]["chat"]["id"]  # Extract chat ID
            print(f"Chat ID: {chat_id}")
            return chat_id
        else:
            print("No updates found.")
            return None
    except KeyError as e:
        print(f"Error fetching chat ID: {e}")
        return None


async def start():
    """
    Start the bot and send the current PS5 price.
    """
    price = get_ps5_price(URL_TO_TRACK_PRICE)  # Get the PS5 price
    await send_message(f"The current price of PS5 is {price}")  # Send the price as a message

if __name__ == "__main__":
    asyncio.run(start())  # Run the start function asynchronously
