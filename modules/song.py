import os
import re
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pytube import Search, YouTube

async def song_download(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Please provide a song name.\n\nUsage: `/song despacito`", quote=True)

    query = " ".join(message.command[1:])
    msg = await message.reply(f"🔎 Searching for **{query}** ...")

    try:
        # Search YouTube
        search = Search(query)
        video = search.results[0]
        yt = YouTube(video.watch_url)

        # Download audio
        stream = yt.streams.filter(only_audio=True).first()
        os.makedirs("downloads", exist_ok=True)
        file_path = stream.download(output_path="downloads")

        await msg.edit("⬆️ Uploading song ...")
        await message.reply_audio(
            audio=file_path,
            title=yt.title,
            performer=yt.author,
            caption=f"🎵 {yt.title}\n📺 [YouTube Link]({yt.watch_url})",
        )
        await msg.delete()
        os.remove(file_path)

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

song_handler = MessageHandler(song_download, filters.command("song"))
