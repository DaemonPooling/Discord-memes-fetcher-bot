import os
from dotenv import load_dotenv
### MAIN MODULE ###
import httpx as x 
import asyncio as io 
from colorama import init as initiate_color, Fore as Color, Style; initiate_color()
import threading

load_dotenv()  # take environment variables from .env.

class Secret:
    token = os.getenv("YOUR_DISCORD_ACCOUNT_TOKEN")

FILE_NAME = os.getenv("FILE_NAME")
channel_id = "TARGET_DISCORD_CHANNEL" # Put your desired target channel here where you want all the memes inside the channel to be retrieved.
api_url = f"https://discord.com/api/v10/channels/{channel_id}/messages" # Discord API Endpoint
FILE_FORMATS = ['.png', '.mp4', '.jpeg', '.mov', '.jpg', '.webp', '.wmv', '.webm', '.avi']  # List of file formats to retrieved. Since, most memes are .png, .jpeg, or .mp4 formats. 
LIMITS = 100 # How many messages should be retrieved per request. Do not input more than 100.

headers = {
    "Authorization": f"{Secret.token}", 
}

# Send GET requests to a Discord API endpoint and fetches messages in batches.
async def fetch_messages():
    all_messages = []
    params = {"limit": LIMITS} 
    while True:
        async with x.AsyncClient() as client:
            response = await client.get(api_url, headers=headers, params=params)
            if response.status_code == 200:
                messages = response.json()
                if not messages:
                    break 
                await process_messages(messages)
                all_messages.extend(messages)
                params["before"] = messages[-1]["id"]
            else:
                print(f"Failed to fetch messages. Status code: {response.status_code}")
                return None

    return all_messages

# For each message, checks if there are any ‘attachments’. If there are, iterates over each attachment.
async def process_messages(messages):
    with open(f'{FILE_NAME}.txt', 'a') as f:
        for message in messages:
            if 'attachments' in message:
                for attachment in message['attachments']:
                    filename = attachment['filename']
                    if any(filename.endswith(format) for format in FILE_FORMATS):
                        file_url = attachment['url']
                        print(f'{Color.GREEN}{Style.BRIGHT}[{message["author"]["id"]}#{message["author"]["discriminator"]} ({message["timestamp"]:.10})]{Color.WHITE}     :::     {Color.YELLOW}{Style.BRIGHT}{file_url}{Color.WHITE}')
                        author = f'{message["author"]["id"]}'
                        timestamp = message["timestamp"]
                        file_url = attachment['url']
                        # File name
                        f.writelines(f'[{author} ({timestamp}) ]            :::             {file_url}\n')
    f.close()
    

# New event loop is created and set as the current event loop.
async def run_async():
    loop = io.new_event_loop()
    io.set_event_loop(loop)

    messages = await fetch_messages()
    await process_messages(messages)

if __name__ == "__main__":
    initiate_color()
    # Create a thread to run the async code
    thread = threading.Thread(target=io.run, args=(run_async(),))
    thread.start()
    thread.join()