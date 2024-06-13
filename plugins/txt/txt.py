import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from helper.database import AshutoshGoswami24
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto, Message
import random

from bot import bot
import plugins.txt.core as helper
from plugins.txt.utils import *
from config import *

# Handler for the /donate command
@Client.on_message(filters.command("donate") & filters.private)
async def donate_command_handler(client, m):
    buttons = [
        [InlineKeyboardButton('💸𝗱𝗼𝗻𝗮𝘁𝗲💸', url='https://ashubotz.github.io/Pay/bot/txtdonet.html')],
        [InlineKeyboardButton('💸Buy Bot Only 5$💸', url='https://t.me/AshuSupport')],
        [InlineKeyboardButton('📸📸sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ🖼️🖼️', url='https://t.me/MovieXPrime_bot')],
        [InlineKeyboardButton('🏠Hᴏᴍᴇ🏠', callback_data='start')]
    ]
    await client.send_photo(
        chat_id=m.chat.id,
        photo=random.choice(QRPICS),
        caption=DONATE_TXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Handler for the /start command
@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    user = message.from_user
    await AshutoshGoswami24.add_user(user.id)  # Pass only the user ID

    buttons = [
        [InlineKeyboardButton('😁ʜᴏᴡ ᴛᴏ ᴜsᴇ😁', callback_data='use')],
        [InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/PandaWepChat')],
        [InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/pandawep')],
        [InlineKeyboardButton('😎 ᴏᴡɴ ʙᴏᴛ 😎', callback_data='own')],
        [InlineKeyboardButton('🧑‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ🧑‍💻', url='https://t.me/AshutoshGoswami24')],
        [InlineKeyboardButton('🧑‍💻ᴅᴇᴠ Sᴜᴘᴘᴏʀᴛ🧑‍💻', url='https://t.me/AshuSupport')],
        [InlineKeyboardButton('💸Bᴜʏ Pʀɪᴍᴇ Nᴏᴡ💸', callback_data='prime')]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    me2 = (await client.get_me()).mention
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_TXT.format(message.from_user.mention, me2),
        reply_markup=reply_markup
    )

# Callback query handler
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
        
    elif query.data == "start":
        buttons = [
            [InlineKeyboardButton('😁ʜᴏᴡ ᴛᴏ ᴜsᴇ😁', callback_data='use')],
            [InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/PandaWepChat')],
            [InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/pandawep')],
            [InlineKeyboardButton('😎 ᴏᴡɴ ʙᴏᴛ 😎', callback_data='own')],
            [InlineKeyboardButton('🧑‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ🧑‍💻', url='https://t.me/AshutoshGoswami24')],
            [InlineKeyboardButton('🧑‍💻ᴅᴇᴠ Sᴜᴘᴘᴏʀᴛ🧑‍💻', url='https://t.me/AshuSupport')],
            [InlineKeyboardButton('💸Bᴜʏ Pʀɪᴍᴇ Nᴏᴡ💸', callback_data='prime')]
        ]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        me2 = (await client.get_me()).mention
        await query.message.edit_text(
            text=START_TXT.format(query.from_user.mention, me2),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "use":
        buttons = [
            [InlineKeyboardButton('🏠Hᴏᴍᴇ🏠', callback_data='start')],
            [InlineKeyboardButton('💸Bᴜʏ Bᴏᴛ Oɴʟʏ ₹𝟽𝟶💸', callback_data='prime')]
        ]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(USE))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=USE_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )          

    elif query.data == "own":
        buttons = [
            [InlineKeyboardButton('🏠Hᴏᴍᴇ🏠', callback_data='start')],
            [InlineKeyboardButton('💸Bᴜʏ Pʀɪᴍᴇ Nᴏᴡ💸', callback_data='prime')]
        ]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(QRPICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=OWN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )  

    elif query.data == "prime":
        buttons = [
            [InlineKeyboardButton('💸𝗱𝗼𝗻𝗮𝘁𝗲💸', url='https://ashubotz.github.io/Pay/bot/txtdonet.html')],
            [InlineKeyboardButton('💸Bᴜʏ Bᴏᴛ Oɴʟʏ ₹𝟽𝟶💸', callback_data='own')],
            [InlineKeyboardButton('📸📸sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ🖼️🖼️', url='https://t.me/MovieXPrime_bot')],
            [InlineKeyboardButton('🏠Hᴏᴍᴇ🏠', callback_data='start')]
        ]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(QRPICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=PRIME_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )  


# Define your command handler for authenticated and prime users
async def is_prime_user_filter(_, __, message: Message):
    return await AshutoshGoswami24.is_prime_user(message.from_user.id)

prime_user_filter = filters.create(is_prime_user_filter)

async def download_file(url, filename):
    cmd = f'yt-dlp -o "{filename}" "{url}"'
    os.system(cmd)
    return filename

async def download_video(url, resolution, filename):
    ytf = f"b[height<={resolution}][ext=mp4]/bv[height<={resolution}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
    cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{filename}.mp4"'
    os.system(cmd)
    return f"{filename}.mp4"

@Client.on_message(filters.command(["upload"]) & (filters.user(AUTH_USERS) | prime_user_filter))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀 𝐓𝐱𝐭 𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝 𝐇𝐞𝐫𝐞 ⏍')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete()

    try:
        with open(x, "r") as f:
            content = f.read().splitlines()
        links = [line.split("://", 1) for line in content]
        os.remove(x)
    except Exception as e:
        await m.reply_text(f"∝ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭. Error: {str(e)}")
        os.remove(x)
        return

    await editable.edit(f"∝ 𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤 𝐅𝐨𝐮𝐧𝐝 𝐀𝐫𝐞 🔗 **{len(links)}**\n\n𝐒𝐞𝐧𝐝 𝐅𝐫𝐨𝐦 𝐖𝐡𝐞𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐢𝐚𝐥 𝐢𝐬 **1**")
    input0: Message = await bot.listen(editable.chat.id)
    start_index = int(input0.text) - 1
    await input0.delete()

    await editable.edit("∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞")
    input1: Message = await bot.listen(editable.chat.id)
    batch_name = input1.text
    await input1.delete()

    await editable.edit("∝ 𝐄𝐧𝐭𝐞𝐫 𝐑𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧 🎬\n☞ 144, 240, 360, 480, 720, 1080\nPlease Choose Quality\n**@AshutoshGoswami24 @PandaWep**")
    input2: Message = await bot.listen(editable.chat.id)
    resolution = input2.text
    await input2.delete()

    resolution_map = {
        "144": "256x144",
        "240": "426x240",
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080"
    }
    res = resolution_map.get(resolution, "UN")

    await editable.edit("✏️ Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    caption = input3.text
    await input3.delete()
    
    highlighter = f"️ ⁪⁬⁮⁮⁮"
    MR = highlighter if caption == 'Robin' else caption

    await editable.edit("🌄 Now send the Thumb url\nEg » \n\n Or if don't want thumbnail send = no")
    input6: Message = await bot.listen(editable.chat.id)
    thumb_url = input6.text
    await input6.delete()

    thumb = "no"
    if thumb_url.startswith("http://") or thumb_url.startswith("https://"):
        thumb = "thumb.jpg"
        getstatusoutput(f"wget '{thumb_url}' -O '{thumb}'")

    for i in range(start_index, len(links)):
        link = links[i][1]
        url = "https://" + link.replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
        name = f'{str(i + 1).zfill(3)}) {links[i][0].strip()[:60]}'
        ytf = f"b[height<={resolution}][ext=mp4]/bv[height<={resolution}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"

        if "visionias" in url:
            async with ClientSession() as session:
                async with session.get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
                }) as resp:
                    text = await resp.text()
                    url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

        elif 'videos.classplusapp' in url:
            url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={
                'x-access-token': 'your_token_here'
            }).json()['url']

        elif '/master.mpd' in url:
            id = url.split("/")[-2]
            url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

        cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

        try:
            if "drive" in url:
                filename = await download_file(url, name)
                await bot.send_document(chat_id=m.chat.id, document=filename, caption=f"**[ 📁 ] Pdf_ID:** {str(i + 1).zfill(3)}. {name} {MR}.pdf \n✉️ 𝐁𝐚𝐭𝐜𝐡 » **{batch_name}**")
                os.remove(filename)
            elif ".pdf" in url:
                filename = await download_file(url, f'{name}.pdf')
                await bot.send_document(chat_id=m.chat.id, document=filename, caption=f"**[ 📁 ] Pdf_ID:** {str(i + 1).zfill(3)}. {name} {MR}.pdf \n✉️ 𝐁𝐚𝐭𝐜𝐡 » **{batch_name}**")
                os.remove(filename)
            else:
                await m.reply_text(f"❊⟱𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📝 𝐍𝐚𝐦𝐞 » `{name}`\n⌨ 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {resolution}\n\n**🔗 𝐔𝐑𝐋 »** `{url}`")
                filename = await download_video(url, resolution, name)
                await bot.send_document(chat_id=m.chat.id, document=filename, caption=f"**[ 🎥 ] Vid_ID:** {str(i + 1).zfill(3)}
                    await m.reply_text("𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞 @AshutoshGoswami24 @PandaWep")

async def send_vid(bot, m, caption, filename, thumb, name, prog):
    try:
        if thumb != "no":
            await bot.send_video(chat_id=m.chat.id, video=filename, caption=caption, thumb=thumb)
        else:
            await bot.send_video(chat_id=m.chat.id, video=filename, caption=caption)
    except Exception as e:
        await m.reply_text(f"Error while sending video: {str(e)}")
        await prog.delete()

# Helper functions for downloading and processing videos and files
class Helper:
    @staticmethod
    async def download_video(url, cmd, filename):
        os.system(cmd)
        return filename

    @staticmethod
    async def download(url, filename):
        cmd = f'yt-dlp -o "{filename}" "{url}"'
        os.system(cmd)
        return filename

    @staticmethod
    async def send_vid(bot, m, caption, filename, thumb, name, prog):
        try:
            if thumb != "no":
                await bot.send_video(chat_id=m.chat.id, video=filename, caption=caption, thumb=thumb)
            else:
                await bot.send_video(chat_id=m.chat.id, video=filename, caption=caption)
        except Exception as e:
            await m.reply_text(f"Error while sending video: {str(e)}")
            await prog.delete()

# Define your command handler for stopping the bot
@Client.on_message(filters.command("stop") & (filters.user(AUTH_USERS)))
async def restart_handler(_, m):
    await m.reply_text("**Bot has been stopped.**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

# # Define your sorry message and help link for users who are not authenticated
# @Client.on_message(~filters.user(AUTH_USERS))
# async def unauthorized_user(bot, message):
#     sorry_message = (
#        """If you need to buy a prime membership, pay and send a screenshot to <a href="https://t.me/AshuXRobot">Ashu Robot</a>."""
#     )
#     await message.reply_text(sorry_message, disable_web_page_preview=True)

@Client.on_message(~filters.user(AUTH_USERS) & ~filters.chat(AUTH_CHANNELS))
async def unauthorized_user(bot, message):
    sorry_message = (
        """If you need to buy a prime membership, pay and send a screenshot to <a href="https://t.me/AshuXRobot">Ashu Robot</a>. /plan /donate"""
    )
    await message.reply_text(sorry_message, disable_web_page_preview=True)
