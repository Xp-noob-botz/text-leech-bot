import math, time
from datetime import datetime
from pytz import timezone
from config import Config, Txt 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002188153245

async def send_log(b, u):
    if Config.LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            Config.LOG_CHANNEL,
            f"""**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**
            
Uꜱᴇʀ: {u.mention}
Iᴅ: `{u.id}`

Uɴ: @{u.username}
Dᴀᴛᴇ: {date}

Tɪᴍᴇ: {time}

By: {b.mention}
            """
        )
        



