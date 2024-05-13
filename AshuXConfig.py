import re
import os
from os import getenv, environ


#requrments
# API_ID = int(environ.get("API_ID", "29917436"))
# API_HASE = environ.get("API_HASE", "4a926822b076a086a167fe8f2701d3e9")
# BOT_TOKEN = environ.get("BOT_TOKEN", "6679365516:AAGYRwUkGGLNCoHP_AvTTqBG4CNbarstBVs")

API_ID = int(environ.get("API_ID", "29917436"))
API_HASE = environ.get("API_HASE", "4a926822b076a086a167fe8f2701d3e9")
BOT_TOKEN = environ.get("BOT_TOKEN", "7126726584:AAEvsulTILtDO44lctlzDDYTGGvwL5oXQU0")
AUTH_USERS = [7062828064, 5601277336, 6142138951, 6687634412]

#img
QRPICS = (environ.get('QRPICS', 'https://graph.org/file/867866ae66f1d42413c71.jpg https://graph.org/file/867866ae66f1d42413c71.jpg')).split()

PICS = (environ.get('PICS', 'https://graph.org/file/3148e0aa43073985fa9c0.jpg https://graph.org/file/3148e0aa43073985fa9c0.jpg')).split()

BUY_PRIME_PICS = (environ.get('BUY_PRIME_PICS', 'https://graph.org/file/867866ae66f1d42413c71.jpg https://graph.org/file/867866ae66f1d42413c71.jpg')).split()

USE = (environ.get('USE', 'https://graph.org/file/e014588ed2c1b2bf5b82a.jpg https://graph.org/file/e014588ed2c1b2bf5b82a.jpg')).split()

DONATE_TXT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> <code>PandaWep@ybl</code>"""

USE_TXT = """
<b><i>

1) Send /upload and then

2) Send any Txt file and then get file

3) Send start number like you have 100 Txt links and you want to start downloading into 10 then send 10

4) Then send batch name, it's only saved in captcha

5) Then send quality like 144p, 360p, 720p, 1080p. Also, it compresses video.

6) Then send custom thumbnail Telegraph link. If you don't want this, send no.

If you want to buy your own bot for only 70₹, then message him: <a href="https://t.me/AshuXRobot">Ashu Robot</a>.
</i></b><b><i>
1) /upload भेजें फिर

2) कोई Txt फ़ाइल भेजें फिर फ़ाइल प्राप्त करें

3) शुरू संख्या भेजें जैसे आपके पास 100 Txt लिंक हैं और आप 10 में डाउनलोड करना चाहते हैं तो 10 भेजें

4) फिर बैच का नाम भेजें, यह केवल कैप्चा में सहेजा जाता है

5) फिर क्वालिटी भेजें जैसे 144p, 360p, 720p, 1080p। यह वीडियो को कंप्रेस भी करता है।

6) फिर कस्टम थंबनेल टेलीग्राफ लिंक भेजें। यदि आप इसे नहीं चाहते, तो no भेजें।

अगर आपको अपना बॉट खरीदना है, तो केवल 70₹ में उससे संपर्क करें: <a href="https://t.me/AshuXRobot">Ashu Robot</a>
</i></b>"""

OWN_TXT = """<b>Send Money 70₹ & DM Me
➠ 16MbPs Download Speed
➠ 7 MbPs Upload Speed [If You Have Telegram Prime Then 10 To 16MbPs(40₹+)]
➠ File Size 2GB [If You Have Telegram Prime Then 4GB(40₹+)]
➠ Bast And Fast Video Compressor [40₹+]
➠ Error Support For 7 Day
</b>"""

START_TXT = """<b>Hay {} I AM {} Bot!

I am a Telegram bot for students to download TXT files with video compression. Click on "How to Use" for instructions.

मैं एक टेलीग्राम बॉट हूं जो छात्रों को वीडियो संपीड़न के साथ TXT फ़ाइलें डाउनलोड करने के लिए हूं। "कैसे उपयोग करें" पर क्लिक करें निर्देशों के लिए।
</b>
"""

PRIME_TXT = """
<b>
1) Scan the code
2) Pay 20₹ and take a screenshot
3) Send the screenshot to him: <a href="https://t.me/AshuXRobot">Ashu Robot</a>
4) Wait for a maximum of 1 day,
5) Then use the bot

<i>Create your own Txt lecher bot only in 70₹</i>

🛍 𝗨𝗣𝗜 𝗜𝗗: <code>PandaWep@ybl</code></b>
<b>
1) कोड स्कैन करें
2) 20₹ देकर एक स्क्रीनशॉट लें
3) स्क्रीनशॉट को इसके पास भेजें: <a href="https://t.me/AshuXRobot">Ashu Robot</a>
4) अधिकतम 1 दिन इंतजार करें,
5) फिर Bot उपयोग करें

<i>अपना खुद का Txt lecher बॉट केवल 70₹ में बनाएं</i>

🛍 𝗨𝗣𝗜 𝗜𝗗: <code>PandaWep@ybl</code>

</b>"""
