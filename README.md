![image](https://github.com/DaemonPooling/Discord-memes-fetcher-bot/assets/157283533/ae8951bb-da15-4e80-b5a5-7d9fb187f22e)![image](https://github.com/DaemonPooling/Discord-memes-fetcher-bot/assets/157283533/6065b9fe-d3a9-4bb0-a078-d0aa8a553b31)# Python meme Magician 🧙‍♂️
Welcome to Python meme Magician! A script where your one-stop solution for meme retrieval and random meme generation in the blink of an eye! 🚀

## 🌈 What's Inside?
- **Meme Fetcher:** This Python script allows you to summon memes of your choice by fetching .png, .jpeg, or any other image (optional format) format from a designated meme channel.

- **Meme Bot:** With this Python script that can deliver a joy by presenting you with a random meme or one of your specified meme ID. ✨

## 🚀 How to Use?
1. **Fetch Memes**: Invoke the `fetcher.py` by providing it with the expected format, channel id you seek. 
2. **Summon Random Meme:** Activate the Meme Bot, at this step, I assume you know how to create a python bot. If you do not have any idea how, follow this URL: [Discord Bot tutorial](https://github.com/discord-apps/bot-tutorial)

## 📜 Instructions:
1. **Clone the repository:**
```bash
git clone https://github.com/DaemonPooling/Discord-memes-fetcher-bot.git
```

2. **Navigate to the Project Folder:**
```bash
cd Discord-memes-fetcher-bot
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure the environment variables (important):**
Configure these variables below. If you do not know how, follow after the code:
```env
# .env file
YOUR_DISCORD_ACCOUNT_TOKEN='put_your_discord_token_here'
YOUR_BOT_ACCOUNT_TOKEN='put_your_discord_bot_token_here'
FILE_NAME='what_is_the_file_name_looks_like'
```
### 1. Setting up your discord's token:
1. Go to your discord.
2. Open the Developer console, or Inspect element then go to Console, you can simply Press F12.
![image](https://github.com/DaemonPooling/Discord-memes-fetcher-bot/assets/157283533/4eb7b51d-e20b-4c6a-9e23-3bdca71dd382)
3. In the console paste this and enter.
```js
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
![image](https://github.com/DaemonPooling/Discord-memes-fetcher-bot/assets/157283533/933e5297-4944-47e1-b5ea-ab4bee47a0c4)

### 2. Setting up your discord's bot token:
1. I can't really show them much, since the steps itself are comprehensive and I am trying to make this README.md short. Though, you can visit this link for the tutorial [Discord Bot tutorial](https://github.com/discord-apps/bot-tutorial)

5. **Run fetcher.py:**
```bash
python source/fetcher.py
```

6. **Run bot.py (YOU SHOULD HAVE YOUR DISCORD BOT PREPARED):**
```bash
python source/bot.py
```
