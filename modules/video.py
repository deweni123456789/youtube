import os
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pytube import Search, YouTube

async def video_download(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Please provide a video name.\n\nUsage: `/video despacito`", quote=True)

    query = " ".join(message.command[1:])
    msg = await message.reply(f"🔎 Searching for **{query}** ...")

    try:
        # Search YouTube
        search = Search(query)
        video = search.results[0]
        yt = YouTube(video.watch_url)

        # Download video
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        os.makedirs("downloads", exist_ok=True)
        file_path = stream.download(output_path="downloads")

        await msg.edit("⬆️ Uploading video ...")
        await message.reply_video(
            video=file_path,
            caption=f"🎬 {yt.title}\n📺 [YouTube Link]({yt.watch_url})",
        )
        await msg.delete()
        os.remove(file_path)

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

video_handler = MessageHandler(video_download, filters.command("video"))
