from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants.text import EarnButtonTitles, OtherTitles, TransitionTitles


def menu(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(EarnButtonTitles.INVITE_FRIEND.value, None, 'earn.action.invite_friend')])
    buttons.append([InlineKeyboardButton(EarnButtonTitles.VIEW_NEWS.value, None, 'earn.action.view_news')])
    buttons.append(
        [InlineKeyboardButton(EarnButtonTitles.SUBSCRIBE_CHANNEL.value, None, 'earn.action.visit_url')])
    buttons.append([InlineKeyboardButton(EarnButtonTitles.SHARE_CONTACTS.value, None, 'earn.action.share_contacts')])

    return InlineKeyboardMarkup(buttons)


def pickup_more(bot, update):
    buttons = []
    buttons.append([InlineKeyboardButton(OtherTitles.MORE.value, None, 'user.action.more')])

    return InlineKeyboardMarkup(buttons)


def visit_url_menu(bot, update, transition):
    buttons = []
    buttons.append([InlineKeyboardButton(TransitionTitles.VISIT.value, transition.get_redirect_url())])
    buttons.append([InlineKeyboardButton(TransitionTitles.PAID.value, None, 'earn.visit.paid.{}'.format(transition.get_id()))])

    return InlineKeyboardMarkup(buttons)
