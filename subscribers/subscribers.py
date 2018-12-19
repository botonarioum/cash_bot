import datetime

from constants.text import Prices
from orm.area import Area
from orm.channel import Channel
from orm.event import Event


def update_user(sender):
    print('on user action')
    update = sender.update

    area = Area.get_by_id(2)

    now = datetime.datetime.now()

    if update.callback_query:
        chat_id = update.callback_query.message.chat.id
        first_name = update.callback_query.message.chat.first_name
        last_name = update.callback_query.message.chat.last_name
    else:
        chat_id = update.message.chat.id
        first_name = update.message.chat.first_name
        last_name = update.message.chat.last_name

    defaults = {
        'channel_id': chat_id,
        'first_name': first_name,
        'last_name': last_name,
        'area': area,
        'created_at': now,
        'updated_at': now
    }

    chanel, is_new = Channel.get_or_create(area=area, channel_id=chat_id, defaults=defaults)
    chanel.update_me(now)


def on_start_usage(sender):
    print('on start usage event')
    update = sender.update

    area = Area.get_by_id(2)

    event_title = Prices.ON_USER_CONNECT.name
    event_price = Prices.ON_USER_CONNECT.value

    if update.callback_query:
        chat_id = update.callback_query.message.chat.id
    else:
        chat_id = update.message.chat.id

    channel = Channel.get(Channel.channel_id == chat_id, Channel.area == area)

    defaults = {
        'channel_id': channel.id,
        'title': event_title,
        'price': event_price,
    }

    Event.get_or_create(channel_id=channel.id, defaults=defaults)
