import discord 
import re
import random 
import os
from dotenv import load_dotenv
from discord.ext import commands
intents=discord.Intents.default()
intents.message_content = True
Host = commands.Bot(command_prefix="?", intents=intents)

load_dotenv()  # take environment variables from .env.

FILE_NAME = os.getenv("FILE_NAME")
TOKEN = os.getenv("YOUR_BOT_ACCOUNT_TOKEN")

# Simply tell the USER if the Bot are ready or not.
@Host.event
async def on_ready():
    print('Ready.')

# When triggered, will choose any random attachment link from the memes list.
@Host.command()
async def memepls(msg, ID=None):
    _PATH = f'{FILE_NAME}.txt'

    with open(_PATH, 'r') as f:
        total_lines = sum(1 for line in f)

    if total_lines == 0:
        print("The file is empty.")
    else:
        # Generate a random line number
        if ID is None:
            random_line_number = random.randint(1, total_lines)
        else:
            random_line_number = int(ID)

        with open(_PATH, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if line_number == random_line_number:
                    pattern = r'\[(\d+) \(([\w\-\:.+]+)\) ]\s+:+\s+(https?:\/\/cdn.discordapp.com\/attachments\/\d+\/\d+\/[\w.-]+)'
                    Line = line.strip()
                    match = re.search(pattern, Line)
                    if match:
                        def random_color():
                            return int(''.join([random.choice('0123456789ABCDEF') for _ in range(2)]), 16)
                        user_id = match.group(1)
                        date_human_readable = match.group(2)
                        link = match.group(3)
                        color = discord.Colour.from_rgb(random_color(), random_color(), random_color())  # Create a random color
                        await msg.reply(f"""
                                        Sure! Here\'s some fresh meme for you! :sunglasses:
                                        > Date: {date_human_readable}
                                        > Credit to User ID: **{user_id}**
                                        > Meme ID: {random_line_number}
                                        > Source: [Click here]({link})
                                        
**Note: Also please be aware and be mindful to realize that some of the memes may come offensive, no context, unfunny, or even dark. This whole memes are collected randomly from the targeted discord's channel server.**
                                        """)  # Obligatory message content.
                    else:
                        await msg.reply('Sorry! It seems I failed to response!')
                    break
    
Host.run(TOKEN)    
