from menu import default_menu


def select_menu_item(bot, update):
    reply_markup = default_menu.menu(bot, update)

    message = 'Выбери пункт меню 👇'
    update.message.reply_text(message, reply_markup=reply_markup)
