import os
from pyrogram import Client, filters
from modules.song import song_handler
from modules.video import video_handler

API_ID = int(os.getenv("API_ID", "5047271"))       # Put your values
API_HASH = os.getenv("API_HASH", "047d9ed308172e637d4265e1d9ef0c27")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7896090354:AAE_NaVu_d-x-TCJt9CPNMl9t94Mltw_jrw")

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
