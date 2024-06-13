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

# Define your command handler for authenticated users
@Client.on_message(filters.command(["upload"]) & (filters.user(AUTH_USERS) | prime_user_filter))
async def account_login(client: Client, message: Message):
    try:
        editable = await message.reply_text('𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀 𝐓𝐱𝐭 𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝 𝐇𝐞𝐫𝐞 ⏍')
        input_message = await client.listen(editable.chat.id)
        x = await input_message.download()
        await input_message.delete(True)

        path = f"./downloads/{message.chat.id}/"

        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = [i.split("://", 1) for i in content]
        os.remove(x)

        await editable.edit(f"∝ 𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤 𝐅𝐨𝐮𝐧𝐝 𝐀𝐫𝐞 🔗 **{len(links)}**\n\n𝐒𝐞𝐧𝐝 𝐅𝐫𝐨𝐦 𝐖𝐡𝐞𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐚𝐥 𝐢𝐬 **1**")
        input0 = await client.listen(editable.chat.id)
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞")
        input1 = await client.listen(editable.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)

        await editable.edit("∝ 𝐄𝐧𝐭𝐞𝐫 𝐑𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧 🎬\n☞ 144, 240, 360, 480, 720, 1080\nPlease Choose Quality\n**@AshutoshGoswami24 @PandaWep**")
        input2 = await client.listen(editable.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)

        res = {
            "144": "256x144",
            "240": "426x240",
            "360": "640x360",
            "480": "854x480",
            "720": "1280x720",
            "1080": "1920x1080"
        }.get(raw_text2, "UN")

        await editable.edit("✏️ Now Enter A Caption to add caption on your uploaded file")
        input3 = await client.listen(editable.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)

        MR = "️ ⁪⁬⁮⁮⁮" if raw_text3 == 'Robin' else raw_text3

        await editable.edit("🌄 Now send the Thumb url\nEg » \n\n Or if don't want thumbnail send = no")
        input6 = await client.listen(editable.chat.id)
        raw_text6 = input6.text
        await input6.delete(True)
        await editable.delete()

        thumb = "thumb.jpg" if raw_text6.startswith("http://") or raw_text6.startswith("https://") else "no"

        if len(links) == 1:
            count = 1
        else:
            count = int(raw_text)

        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Referer': 'http://www.visionias.in/',
                        'Sec-Fetch-Dest': 'iframe',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'cross-site',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                    }) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'
                }).json()['url']

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                if "drive" in url:
                    ka = await helper.download(url, name)
                    cc = f'**[ 🎥 ] Vid_ID:** {str(count).zfill(3)}. {name1}{MR}.mkv\n✉️ 𝐁𝐚𝐭𝐜𝐡 » **{raw_text0}**'
                    copy = await client.send_document(chat_id=message.chat.id, document=ka, caption=cc)
                    count += 1
                    os.remove(ka)
                    time.sleep(1)
                
                elif ".pdf" in url:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                    os.system(download_cmd)
                    cc = f'**[ 📁 ] Pdf_ID:** {str(count).zfill(3)}. {name1}{MR}.pdf \n✉️ 𝐁𝐚𝐭𝐜𝐡 » **{raw_text0}**'
                    copy = await client.send_document(chat_id=message.chat.id, document=f'{name}.pdf', caption=cc)
                    count += 1
                    os.remove(f'{name}.pdf')

                else:
                    Show = f"❊⟱𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📝 𝐍𝐚𝐦𝐞 » `{name}\n⌨ 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** `{url}`"
                    prog = await message.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    
                    cc = f'**[ 🎥 ] Vid_ID:** {str(count).zfill(3)}. {name1}{MR}.mkv\n✉️ 𝐁𝐚𝐭𝐜𝐡 » **{raw_text0}**'
                    await helper.send_vid(client, message, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await message.reply_text(
                    f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐫𝐮𝐩𝐭𝐞𝐝\n{str(e)}\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await message.reply_text(str(e))

    await message.reply_text("𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞 @AshutoshGoswami24 @PandaWep")

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
