from menu import bank_menu


def balance(bot, update):
    reply_markup = bank_menu.menu(bot, update)

    message = """
    Ваш баланс: $5.0
Минимальная сумма вывода: $300"""
    update.message.reply_text(message, reply_markup=reply_markup)


def withdraw(bot, update):
    message = """ВЫ не достигли минимальной суммы для выплаты, РАБОТАЙТЕ УСЕРДНЕЕ!"""
    message_id = update.callback_query.message.message_id
    chat_id = update.callback_query.message.chat.id
    bot.editMessageReplyMarkup(chat_id, message_id)
    bot.sendMessage(chat_id, message)
