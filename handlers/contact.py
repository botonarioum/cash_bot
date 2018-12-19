from menu import contacts_menu


def share_info(bot, update):
    reply_markup = contacts_menu.share(bot, update)

    message = 'Расскажи нам о себе:'

    chat_id = update.callback_query.message.chat.id

    bot.sendMessage(chat_id, message, reply_markup=reply_markup)
