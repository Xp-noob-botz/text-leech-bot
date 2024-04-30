import re
import os
from os import getenv, environ




api_id = int(environ.get("api_id", ""))
api_hash = environ.get("api_hash", "")
SUDO_USERS = int(environ.get("SUDO_USERS", "6945082854"))
bot_token = environ.get("bot_token", "")
OWNER_ID = int(environ.get("OWNER_ID", "6945082854"))

QRPICS = (environ.get('QRPICS', 'https://graph.org/file/867866ae66f1d42413c71.jpg https://graph.org/file/867866ae66f1d42413c71.jpg')).split()
PICS = (environ.get('PICS', 'https://graph.org/file/3148e0aa43073985fa9c0.jpg https://graph.org/file/3148e0aa43073985fa9c0.jpg')).split()
START_TXT = """<b>Welcome to My Bot!</b>
Send /upload Then Send Any Txt File Then Get File 
If You Want To Buy Bot @AshuSupport
And Plz Donate For Devloper /donate
"""
DONATE_TXT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> <code>PandaWep@ybl</code>"""
