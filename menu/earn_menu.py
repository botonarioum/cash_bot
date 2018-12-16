from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants.text import EarnButtonTitles


def menu(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(EarnButtonTitles.INVITE_FRIEND.value, None, 'earn.action.invite_friend')])
    buttons.append([InlineKeyboardButton(EarnButtonTitles.VIEW_NEWS.value, None, 'earn.action.view_news')])
    buttons.append([InlineKeyboardButton(EarnButtonTitles.SUBSCRIBE_CHANNEL.value, None, 'earn.action.subscribe_channel')])
    buttons.append([InlineKeyboardButton(EarnButtonTitles.SHARE_CONTACTS.value, None, 'earn.action.share_contacts')])

    return InlineKeyboardMarkup(buttons)
