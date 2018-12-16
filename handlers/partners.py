from menu import partners_menu


def partners(bot, update):
    reply_markup = partners_menu.menu(bot, update)

    message = 'Посетите сайт наших партнёров:'
    update.message.reply_text(message, reply_markup=reply_markup)
