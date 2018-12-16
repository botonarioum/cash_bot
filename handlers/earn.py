from menu import earn_menu


def earn(bot, update):
    reply_markup = earn_menu.menu(bot, update)

    message = 'Выбери способ заработка:'
    update.message.reply_text(message, reply_markup=reply_markup)
