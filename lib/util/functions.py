import json
import random
import os
import aiohttp
from random import randint
from dotenv import load_dotenv

load_dotenv()

# String utilities
def makelist(string):
    return string.split(";")

def sortimg(string):
    for img in random.sample(string, len(string)):
        if 'png' in img:
            return img
    return None

def RandomChoice(string):
    return random.choice(string.split(":"))

def RandomChoice2(string):
    if ',' in string:
        return random.choice(string.split(","))
    elif 'or' in string:
        return random.choice(string.split("or"))
    return string

def boldText(text):
    return f'**{text}**'

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.json()

            print("STATUS:", response.status)
            return text

# aiohttp version of fetch_data
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("STATUS:", response.status)

            # Read raw text (for debugging)
            raw = await response.text()
            print("RAW RESPONSE:", raw)

            # Convert to JSON
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                print("JSON decode failed")
                return None


# Select a random GIF from the API response
def RandomGif(api_json):

    container = api_json.get("data", {})
    array = container.get("data", [])

    if not array:
        print("No results array found")
        return None

    # Choose a random GIF object
    item = random.choice(array)

    file_hd = item.get("file", {}).get("hd", {})
    gif_url = file_hd.get("gif", {}).get("url")

    if not gif_url:
        print("GIF URL missing")
        return None

    return gif_url


# Fetch a random GIF from the Klipy API
async def action(search):
    try:
        app_key = os.environ['KLIPY_API_KEY']

        if not app_key:
            print("API key not found")
            return None

        encoded = quote(search)
        url = f"https://api.klipy.com/api/v1/{app_key}/gifs/search?page=1&per_page=10&q={encoded}"

        data = await fetch_data(url)
        if not data:
            print("No data returned")
            return None

        return RandomGif(data)

    except Exception as e:
        print("Action error:", e)
        return None
