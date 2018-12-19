import os

from menu import earn_menu


def earn(bot, update):
    reply_markup = earn_menu.menu(bot, update)

    message = 'Выбери способ заработка:'
    update.message.reply_text(message, reply_markup=reply_markup)


def invite_friend(bot, update):
    referral_link = os.getenv('REFERRAL_LINK_PATTERN')

    message = referral_link.format(update.callback_query.message.chat.id)
    chat_id = update.callback_query.message.chat.id

    bot.sendMessage(chat_id, message)
