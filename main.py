import os
from pyrogram import Client, filters
from modules.song import song_handler
from modules.video import video_handler

API_ID = int(os.getenv("API_ID", "12345"))       # Put your values
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

app = Client(
    "pytube_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register modules
app.add_handler(song_handler)
app.add_handler(video_handler)

print("Bot started 🚀")

app.run()
