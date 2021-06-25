import os
from re import compile
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, custom
from telethon.sessions import StringSession
from telethon.events import callbackquery, InlineQuery, NewMessage
from math import ceil


load_dotenv("config.env")

# Pengaturan log bot:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

ASYNC_POOL = []

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - @TeamSquadUserbotSupport - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - @TeamSquadUserbotSupport - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("Anda harus memiliki setidaknya python versi 3.6."
              "Beberapa fitur bergantung padanya. Bot dimatikan.")
    quit(1)

# Periksa apakah konfigurasi telah diedit menggunakan variabel yang digunakan sebelumnya.
# Pada dasarnya, periksa file konfigurasi.
CONFIG_CHECK = os.environ.get(
    "___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Harap hapus baris yang ditentukan dalam tagar pertama dari file config.env"
    )
    quit(1)

# Bot'un dili
LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()

if not LANGUAGE in ["DEFAULT"]:
    LOGS.info("BAhasanya Default")
    LANGUAGE = "DEFAULT"
    
# Alpha
ALPHA_USERBOT = "ALPHA.21.By.Alfareza"
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "Alpha UserBot")

ALPHA_TEKS_KUSTOM = os.environ.get("ALPHA_TEKS_KUSTOM", "I am Alive.")
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/4486546e8185a3012c86f.jpg"

G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Telegram API KEY ve HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

SILINEN_PLUGIN = {}
# UserBot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

#Grup ID 
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# UserBot 
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Tentang aku dan dia
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Tentang aku dan dia
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# Tentang aku dan dia
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/AftahBagas/Alpha-UserBot.git")

# Tentang aku dan dia
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL 
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///asena.db")

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# AUTO PP
AUTO_PP = os.environ.get("AUTO_PP", None)

# Modul peringatan
WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE = os.environ.get("WARN_MODE", "gmute")

if not WARN_MODE in ["gmute", "gban"]:
    WARN_MODE = "gmute"

# Galeri
GALERI_SURE = int(os.environ.get("GALERI_SURE", 60))

# Driver Chrome dan file Google Chrome
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

PLUGINID = os.environ.get("PLUGIN_CHANNEL_ID", None)
# Plugin İçin
if not PLUGINID:
    PLUGIN_CHANNEL_ID = "me"
else:
    PLUGIN_CHANNEL_ID = int(PLUGINID)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# Anti Spambot
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Saat & Tarih - Ülke ve Saat Dilimi
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Tentang aku dan dia
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Modul Last.fm
BIO_PREFIX = os.environ.get("BIO_PREFIX", "@TeamSquadUserbotSupport | ")
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Untuk pekerjaan bot sebaris
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
HELP_EMOJI = os.environ.get("HELP_EMOJI", "🔸")

# Genius
GENIUS = os.environ.get("GENIUS", None)
CMD_HELP = {}
CMD_HELP_BOT = {}
PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 6))

SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)

PAKET_ISMI = os.environ.get("PAKET_ISMI", "@TeamSquadUserbotSupport Paket")

# Otomatis 
OTOMATIS_JOIN = sb(os.environ.get("OTOMATIS_JOIN", "True"))

# Pola Kustom
PATTERNS = os.environ.get("PATTERNS", ".;!,")
WHITELIST = get('https://gitlab.com/Quiec/asen/-/raw/master/whitelist.json').json()

# Menyiapkan CloudMail.ru dan MEGA.nz
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# sepatu bot variabel
if STRING_SESSION:
    # pylint: dinonaktifkan = nama tidak valid
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: dinonaktifkan = nama tidak valid
    bot = TelegramClient("userbot", API_KEY, API_HASH)


if os.path.exists("learning-data-root.check"):
    os.remove("learning-data-root.check")
else:
    LOGS.info("Tidak ada file braincheck, dibawa...")

URL = 'https://raw.githubusercontent.com/quiec/databasescape/master/learning-data-root.check'
with open('learning-data-root.check', 'wb') as load:
    load.write(get(URL).content)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work.")
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work")
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)

with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)


async def check_alive():
    await bot.send_message(BOTLOG_CHATID, "```Alpha UserBot Is Online```")
    return

with bot:
    try:
        bot.loop.run_until_complete(check_alive())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)
        
if not BOT_TOKEN == None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None

def butonlastir(sayfa, moduller):
    Satir = 5
    Kolon = 2
    
    moduller = sorted([modul for modul in moduller if not modul.startswith("_")])
    pairs = list(map(list, zip(moduller[::2], moduller[1::2])))
    if len(moduller) % 2 == 1:
        pairs.append([moduller[-1]])
    max_pages = ceil(len(pairs) / Satir)
    pairs = [pairs[i:i + Satir] for i in range(0, len(pairs), Satir)]
    butonlar = []
    for pairs in pairs[sayfa]:
        butonlar.append([
            custom.Button.inline("{HELP_EMOJI} " + pair, data=f"bilgi[{sayfa}]({pair})") for pair in pairs
        ])

    butonlar.append([custom.Button.inline("<- Pʀᴇᴠɪᴏᴜs", data=f"sayfa({(max_pages - 1) if sayfa == 0 else (sayfa - 1)})"), custom.Button.inline("Cʟᴏsᴇ", b'close'), custom.Button.inline("Nᴇxᴛ ->", data=f"sayfa({0 if sayfa == (max_pages - 1) else sayfa + 1})")])
    return [max_pages, butonlar, pairs]

with bot:
    if OTOMATIS_JOIN:
        try:
            bot(JoinChannelRequest("@TheAlphaSupport"))
            bot(JoinChannelRequest("@TheAlphaSupport"))
        except:
            pass

    moduller = CMD_HELP
    me = bot.get_me()
    uid = me.id

    try:
        @alphabot.on(NewMessage(pattern='/start'))
        async def start_bot_handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'**Join grup untuk membuat Alpha UserBot mu sendiri** @TeamSquadUserbotSupport! **Saya Assistant Dari** (`@{me.username}')
            else:
                await event.reply(f'**Alpha UserBot ...⚡**')

        @alphabot.on(InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query == "@KanjengIngsun":
                rev_text = query[::-1]
                veriler = (butonlastir(0, sorted(CMD_HELP)))
                result = await builder.article(
                    f"Perintah .help petercird",
                    text=f"**HELP INLINE MODE**/n[Alpha UserBot](https://t.me/TeamSquadUserbotSupport) __Plugins__\n**• Jumlah Plugins :** `{len(CMD_HELP)}`\n• **Halaman :** 1/{veriler[0]}",
                    buttons=veriler[1],
                    link_preview=False
                )
            elif query.startswith("http"):
                parca = query.split(" ")
                result = builder.article(
                    "Alpha UserBot",
                    text=f"**Alpha UserBot {parca[2]} Lanjutan**\n\n{parca[1][:3]}\n[‏‏‎ ‎]({parca[0]})",
                    buttons=[
                        [custom.Button.url('URL', parca[0])]
                    ],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "@TesmSquadUserbotSupport",
                    text="""@TeamSquadUserbotSupport.""",
                    buttons=[
                        [custom.Button.url("Group Support", "@TeamSquadUserbotSupport"), custom.Button.url(
                            "Owners", "https://t.me/kanjengingsun")],
                        [custom.Button.url(
                            "GitHub", "https://github.com/AftahBagas/Alpha-UserBot")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)

        @alphabot.on(callbackquery.CallbackQuery(data=compile(b"sayfa\((.+?)\)")))
        async def sayfa(event):
            if not event.query.user_id == uid: 
                return await event.answer("Warning! Hey! kamu harus buat sendiri deploy! silakan anda join @TeamSquadUserbotSupport grup.", cache_time=0, alert=True)
            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            veriler = butonlastir(sayfa, CMD_HELP)
            await event.edit(
                f"**HELP MODE INLINE**\n[Alpha UserBot](https://t.me/TeamSquadUserbotSupport) __Plugins__\n**• Jumlah Plugins :** `{len(CMD_HELP)}`\n**• Halaman :** {sayfa + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False
            )
       
        @alphabot.on(callbackquery.CallbackQuery(data=compile(b"close")))
        async def close(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                await event.edit("**Button Inline Closed**")
            else:
                reply_pop_up_alert = f"Buat Alpha UserBot Mu Sendiri, Jangan Menggunakan Milik {ALIVE_NAME} Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        
        @alphabot.on(callbackquery.CallbackQuery(data=compile(b"bilgi\[(\d*)\]\((.*)\)")))
        async def bilgi(event):
            if not event.query.user_id == uid: 
                return await event.answer("Warning! Hey! kamu harus buat sendiri deploy! silakan anda join @TeamSquadUserbotSupport grup.", cache_time=0, alert=True)

            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            komut = event.data_match.group(2).decode("UTF-8")
            try:
                butonlar = [custom.Button.inline(f"{HELP_EMOJI} " + cmd[0], data=f"komut[{komut}[{sayfa}]]({cmd[0]})") for cmd in CMD_HELP_BOT[komut]['commands'].items()]
            except KeyError:
                return await event.answer(f"Buat Alpha UserBot Mu Sendiri Jangan Menggunakan Milik {ALIVE_NAME} Ini.", cache_time=0, alert=True)

            butonlar = [butonlar[i:i + 2] for i in range(0, len(butonlar), 2)]
            butonlar.append([custom.Button.inline("Bᴀᴄᴋ", data=f"sayfa({sayfa})")])
            await event.edit(
                f"**Daftar Plugins:** `{komut}`\n**• Jumlah Command : ** `{len(CMD_HELP_BOT[komut]['commands'])}`",
                buttons=butonlar,
                link_preview=False
            )
        
        @alphabot.on(callbackquery.CallbackQuery(data=compile(b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))
        async def komut(event):
            if not event.query.user_id == uid: 
                return await event.answer("Warning! Hey! kamu harus buat sendiri deploy! silakan anda join @TeamSquadUserbotSupport grup.", cache_time=0, alert=True)

            cmd = event.data_match.group(1).decode("UTF-8")
            sayfa = int(event.data_match.group(2).decode("UTF-8"))
            komut = event.data_match.group(3).decode("UTF-8")

            result = f"**Daftar Plugins :** `{cmd}`\n"
            if CMD_HELP_BOT[cmd]['info']['info'] == '':
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**Command :** {'' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                    result += f"**✖ Berbahaya :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                else:
                    result += f"**Command :** {'' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
            else:
                result += f"**Command :** {'' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**✖ Berbahaya :** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
                result += f"**• Informasi :** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

            command = CMD_HELP_BOT[cmd]['commands'][komut]
            if command['params'] is None:
                result += f"**Plugins Alpha UserBot :** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**• Command :** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**• Pesan :** `{command['usage']}`\n\n"
            else:
                result += f"**• Command :** `{command['usage']}`\n"
                result += f"**• Sampel Modules :** `{PATTERNS[:1]}{command['example']}`\n\n"

            await event.edit(
                result,
                buttons=[custom.Button.inline("Back", data=f"bilgi[{sayfa}]({cmd})")],
                link_preview=False
            )
    except Exception as e:
        print(e)
        LOGS.info(
            "Mode Inline Bot Mu Belom Di Aktifkan. "
            "Untuk Mengaktifkan Pergi Ke @BotFather, lalu settings bot > pilih mode inline > Turn On. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)


# Variabel Global
SON_GORULME = 0
COUNT_MSG = 0
USERS = {}
BRAIN_CHECKER = []
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
ISAFK = False
AFKREASON = None
ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
    [
    " ̍", " ̎", " ̄", " ̅", " ̿", " ̑", " ̆", " ̐", " ͒", " ͗",
    " ͑", " ̇", " ̈", " ̊", " ͂", " ̓", " ̈́", " ͊", " ͋", " ͌",
    " ̃", " ̂", " ̌", " ͐", " ́", " ̋", " ̏", " ̽", " ̉", " ͣ",
    " ͤ", " ͥ", " ͦ", " ͧ", " ͨ", " ͩ", " ͪ", " ͫ", " ͬ", " ͭ",
    " ͮ", " ͯ", " ̾", " ͛", " ͆", " ̚"
],
    [
    " ̕",
    " ̛",
    " ̀",
    " ́",
    " ͘",
    " ̡",
    " ̢",
    " ̧",
    " ̨",
    " ̴",
    " ̵",
    " ̶",
    " ͜",
    " ͝",
    " ͞",
    " ͟",
    " ͠",
    " ͢",
    " ̸",
    " ̷",
    " ͡",
]]
