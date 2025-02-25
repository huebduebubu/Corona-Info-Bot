import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Corona-Info-Bot",
    bot_token = "5409233419:AAEgRrOhh8WxU3Dbzrqv_pj0fk-BJzAIKo8",
    api_id = 10837069,
    api_hash = "8c369144619c9c8fd6a55a2a35f2203d"
)

API = "https://api.sumanjay.cf/covid/?country="

START_TEXT = """Hello {},
I am a simple corona information of a country telegram bot.

Made by @FayasNoushad"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')]])


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def reply_info(bot, update):
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(update.text),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--

Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`

Made by @FayasNoushad"""
        return covid_info
    except Exception as error:
        return error


Bot.run()
