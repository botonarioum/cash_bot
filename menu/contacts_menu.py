from telegram import KeyboardButton, ReplyKeyboardMarkup

from constants.text import OtherTitles
from constants.text import ShareContactsTitles


def share(bot, update):
    buttons = []
    buttons.append([KeyboardButton(ShareContactsTitles.PHONE.value, True, None),
                    KeyboardButton(ShareContactsTitles.LOCATION.value, None, True)])
    buttons.append([KeyboardButton(OtherTitles.BACK.value)])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
