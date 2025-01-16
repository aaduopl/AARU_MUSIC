import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("29129783"))
API_HASH = getenv("581c6687b82f22186565924cc6176a34")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7763199485:AAFELzHd_eDNraQgwyICxxhx-HmVkCFScHA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://Bishal:Bishal@bishal.dffybpx.mongodb.net/?retryWrites=true&w=majority&appName=Bishal", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1700))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002319978995", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("1302320722", 6972508083))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vishalpandeynkp1/Lundchut",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PAGLA_STUPID_P")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PAGLA_STUPID_P")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQG8fDcAIPctx7HH7uKoYlc72XiiGmX5gugJ47xbvtMMm4OGLHh-uEQrltnOuPdTSIoMtJCslI6WwavT6o6SOlNr-PhVW3Y6v11VQeFLZypyTsPX8TkZICt8ef4LwYzfF8vSUCBBNimp-J0QNm4yJZBlRSDAkpCV5gSf7XGUPZ3j8IPXV0h4XrK_22suTMrXqgFkyronnWDhzwcnKQ7UGTfFimZaFlaR5DUO1J-50RttuFZOAZ8C3l7O74nYYcF8SvAj17KywyfZPY7b-rTglAvRM09ZZCbNxFsD7KPglrsBaCxKEf81YHgrpn9wQCOeQLIkZVCHOIbztw007qPqBF3XbWJqCAAAAAGnz7_mAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/A1B.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/A1B.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/A1B.jpg"
STATS_IMG_URL = "https://envs.sh/A1B.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/A1B.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/A1B.jpg"
STREAM_IMG_URL = "https://envs.sh/A1B.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/A1B.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/A1B.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/A1B.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/A1B.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/A1B.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
