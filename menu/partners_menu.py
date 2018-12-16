from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants.text import PartnerTitles


def menu(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(PartnerTitles.PARTNER_1.value, 'https://google.com')])
    buttons.append([InlineKeyboardButton(PartnerTitles.PARTNER_2.value, 'https://yadex.com')])

    return InlineKeyboardMarkup(buttons)
