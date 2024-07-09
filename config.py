import re, os, time
id_pattern = re.compile(r'^.\d+$') 
from os import getenv, environ


#requrments
# API_ID = int(environ.get("API_ID", "29917436"))
# API_HASE = environ.get("API_HASE", "4a926822b076a086a167fe8f2701d3e9")
# BOT_TOKEN = environ.get("BOT_TOKEN", "6679365516:AAGYRwUkGGLNCoHP_AvTTqBG4CNbarstBVs")

# API_ID = int(environ.get("API_ID", "29917436"))
# API_HASE = environ.get("API_HASE", "4a926822b076a086a167fe8f2701d3e9")
# BOT_TOKEN = environ.get("BOT_TOKEN", "7126726584:AAEvsulTILtDO44lctlzDDYTGGvwL5oXQU0")


AUTH_USERS = [7062828064, 6679365516, 7375364794]
AUTH_CHANNELS = [-1002188153245, -1002116868480]
#img
QRPICS = (environ.get('QRPICS', 'https://graph.org/file/867866ae66f1d42413c71.jpg https://graph.org/file/867866ae66f1d42413c71.jpg')).split()

PICS = (environ.get('PICS', 'https://graph.org/file/08fdfd18424ca5071c25c.jpg https://graph.org/file/08fdfd18424ca5071c25c.jpg')).split()

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
2) Pay 400₹ and take a screenshot
3) Send the screenshot to him: <a href="https://t.me/AshuXRobot">Ashu Robot</a>
4) Wait for a maximum of 1 day,
5) Then use the bot

<i>Create your own Txt lecher bot only in 70₹</i>

🛍 𝗨𝗣𝗜 𝗜𝗗: <code>PandaWep@ybl</code></b>
<b>
1) कोड स्कैन करें
2) 40₹ देकर एक स्क्रीनशॉट लें
3) स्क्रीनशॉट को इसके पास भेजें: <a href="https://t.me/AshuXRobot">Ashu Robot</a>
4) अधिकतम 1 दिन इंतजार करें,
5) फिर Bot उपयोग करें

<i>अपना खुद का Txt lecher बॉट केवल 70₹ में बनाएं</i>

🛍 𝗨𝗣𝗜 𝗜𝗗: <code>PandaWep@ybl</code>

</b>"""


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29917436")
    API_HASH  = os.environ.get("API_HASH", "4a926822b076a086a167fe8f2701d3e9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7375364794:AAEYHxXSx6tBlbirML_OZFvnKQOlG_h4www") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://botzashu:LjkXI1JoztDQiQlr@cluster0.38ague0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    # START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7062828064').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "AshutoshGoswami24") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002188153245"))
    PORT = int(os.environ.get("PORT", "8899"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @PandaWep</b>

<b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @PandaWep </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/PandaWep'>PandaWep</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/PandaWep'>PandaWep</a>
    
<b>♻️ Bot Made By :</b> @PandaWep"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @PandaWep
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - PandaWep@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @PandaWep To Help """





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer @AshutoshGoswami24

