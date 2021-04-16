from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"silahkan kirimkan link video youtube yang ingin di download. Kirimkan link video, bukan link playlist"
    await message.reply_text(helptxt)
