from orm.area import Area
from orm.channel import Channel


def update_user(sender):
    update = sender.update

    area = Area.get_by_id(2)

    if (update.callback_query):
        chat_id = update.callback_query.message.chat.id
        first_name = update.callback_query.message.chat.first_name
        last_name = update.callback_query.message.chat.last_name
    else:
        chat_id = update.message.chat.id
        first_name = update.message.chat.first_name
        last_name = update.message.chat.last_name

    defaults = {'channel_id': chat_id, 'first_name': first_name, 'last_name': last_name, 'area': area}
    chanel, is_new = Channel.get_or_create(area=area, channel_id=chat_id, defaults=defaults)
    chanel.update_me()
