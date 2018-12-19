def get_chat_id(update):
    if update.callback_query:
        return update.callback_query.message.chat.id
    else:
        return update.message.chat.id


def get_message_id(update):
    print(update)
    if update.callback_query:
        return update.callback_query.message.message_id
    else:
        return update.message.id
