import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto

from helper.database import AshutoshGoswami24
from config import *
import random


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
