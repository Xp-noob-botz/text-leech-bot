from config import Config, Txt
from helper.database import AshutoshGoswami24
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002188153245

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ADMIN_USER_ID = Config.ADMIN

# Flag to indicate if the bot is restarting
is_restarting = False

# Define the command handler to add a prime user
@Client.on_message(filters.command("add_prime") & filters.user(ADMIN_USER_ID))
async def add_prime_user(client, message: Message):
    try:
        _, user_id, duration = message.text.split()
        user_id = int(user_id)
        await AshutoshGoswami24.add_user(user_id)  # Ensure only user_id is passed
        await AshutoshGoswami24.promote_to_prime(user_id, duration)
        await message.reply(f"User {user_id} has been promoted to prime user for {duration}.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")


# Define the command handler to delete a prime user
@Client.on_message(filters.command("del_prime") & filters.user(ADMIN_USER_ID))
async def delete_prime_user(client, message: Message):
    try:
        _, user_id = message.text.split()
        user_id = int(user_id)
        await AshutoshGoswami24.delete_prime_user(user_id)
        await message.reply(f"User {user_id} is no longer a prime user.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

# Define the command handler to show all prime users
@Client.on_message(filters.command("show_prime_user") & filters.user(ADMIN_USER_ID))
async def show_prime_user(client, message: Message):
    prime_users = await AshutoshGoswami24.get_prime_users()
    if prime_users:
        response = "Prime Users:\n"
        for user in prime_users:
            username = (await client.get_users(user['_id'])).username
            expiry_date = user.get('prime_expiry', 'Unknown')
            if expiry_date != 'Unknown':
                expiry_date = expiry_date.strftime('%Y-%m-%d %H:%M:%S')
            response += f"Username: @{username}, ID: {user['_id']}, Expiry: {expiry_date}\n"
    else:
        response = "No prime users found."
    await message.reply(response)


    
@Client.on_message(filters.private & filters.command("restart") & filters.user(ADMIN_USER_ID))
async def restart_bot(b, m):
    global is_restarting
    if not is_restarting:
        is_restarting = True
        await m.reply_text("**🔄 Restarting.....**")

        # Gracefully stop the bot's event loop
        b.stop()
        time.sleep(2)  # Adjust the delay duration based on your bot's shutdown time

        # Restart the bot process
        os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.private & filters.command(["tutorial"]))
async def tutorial(bot,message):
	user_id = message.from_user.id
	format_template = await AshutoshGoswami24.get_format_template(user_id)
	await message.reply_text(
	    text =Txt.FILE_NAME_TXT.format(format_template=format_template),
	    disable_web_page_preview=True,
	    reply_markup=InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/PandaWepChat"), 
        			InlineKeyboardButton("⚡ Tutorial",url = "https://t.me/PandaWepChat") ]])
	)



@Client.on_message(filters.command(["stats", "status"]) & filters.user(ADMIN_USER_ID))
async def get_stats(bot, message):
    total_users = await AshutoshGoswami24.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))    
    start_t = time.time()
    st = await message.reply('**Accessing The Details.....**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await st.edit(text=f"**--Bot Status--** \n\n**⌚️ Bot Uptime :** {uptime} \n**🐌 Current Ping :** `{time_taken_s:.3f} ms` \n**👭 Total Users :** `{total_users}`")

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_USER_ID) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} or {m.from_user.id} Is Started The Broadcast......")
    all_users = await AshutoshGoswami24.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Broadcast Started..!") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await AshutoshGoswami24.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await AshutoshGoswami24.delete_user(user['_id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"Broadcast In Progress: \n\nTotal Users {total_users} \nCompleted : {done} / {total_users}\nSuccess : {success}\nFailed : {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ: \nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ `{completed_in}`.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")
           
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Deactivated")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Blocked The Bot")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : User ID Invalid")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500




# PandaWep
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer https://github.com/PandaWep
