from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/levinachannel")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/dlwrml")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}</b>\n/help 👈 tekan untuk info lebih lanjut"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
