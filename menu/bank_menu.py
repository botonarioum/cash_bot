from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants.text import BankButtonTitles


def menu(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(BankButtonTitles.WITHDRAW.value, None, 'bank.action.withdraw')])

    return InlineKeyboardMarkup(buttons)


def withdraw(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(BankButtonTitles.PAYOUT.value, 'https://google.com')])

    return InlineKeyboardMarkup(buttons)
