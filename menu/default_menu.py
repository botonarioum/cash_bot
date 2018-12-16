from telegram import KeyboardButton, ReplyKeyboardMarkup

from constants.text import DefaultButtonTitles


def menu(bot, update):
    keyboard = [
        [KeyboardButton(DefaultButtonTitles.EARN.value, callback_data='1'),
         KeyboardButton(DefaultButtonTitles.PARTNERS.value, callback_data='2')],
        [KeyboardButton(DefaultButtonTitles.BANK.value, callback_data='3'),
         KeyboardButton(DefaultButtonTitles.HELP.value, callback_data='3')]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
