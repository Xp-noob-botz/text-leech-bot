import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto

from helper.database import AshutoshGoswami24
from config import *
import random

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


# Define the command handler for prime users to check their plan
@Client.on_message(filters.command("plan"))
async def check_plan(client, message: Message):
    user_id = message.from_user.id
    remaining_time = await AshutoshGoswami24.get_remaining_time(user_id)
    if remaining_time:
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        response = f"Your prime membership expires in {days} days, {hours} hours, and {minutes} minutes."
    else:
        price_7d = await AshutoshGoswami24.get_prime_membership_price('7d')
        price_1m = await AshutoshGoswami24.get_prime_membership_price('1m')
        response = f"You are not a prime user. To buy prime membership, pay {price_7d} rupees for 7 days or {price_1m} rupees for 1 month. Contact @x_dm_me to buy."
    await message.reply(response)
    
# @Client.on_message(filters.command("id"))
# def get_id(client, message):
#     # Get the user's ID
#     user_id = message.from_user.id
#     # Send the user's ID as a reply
#     message.reply_text(f"Your ID is: `{user_id}`")