from handlers.start import start_text
from menu import default_menu


def help(bot, update):
    reply_markup = default_menu.menu(bot, update)
    # Reply to the message
    update.message.reply_text(start_text, reply_markup=reply_markup)
