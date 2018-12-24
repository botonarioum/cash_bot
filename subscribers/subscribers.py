import datetime

from peewee import DoesNotExist

from constants.text import Prices


def update_user(sender):
    from orm.channel import Channel
    from orm.area import Area
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
    from orm.channel import Channel
    from orm.area import Area
    from orm.event import Event
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


def attach_partner(sender):
    from orm.channel import Channel
    from orm.area import Area
    print('attach partner')
    update = sender.update

    split_by = ' '
    partner_id_position = 1

    try:
        referral_id = update.message.text.split(split_by)[partner_id_position]
        area = Area.get_by_id(2)

        partner = Channel.get(Channel.channel_id == referral_id, Channel.area == area)
        referral = Channel.get(Channel.channel_id == update.message.chat.id, Channel.area == area)

        if referral.partner:
            print('has partner')
        else:
            print('has no partner')

            referral.set_partner(partner)
            add_referral_bonus(sender)

    except IndexError:
        print('Registration without partnership')


def add_referral_bonus(sender):
    from orm.channel import Channel
    from orm.area import Area
    from orm.event import Event
    print('add referral bonus')
    update = sender.update

    channel = Channel.get(Channel.channel_id == update.message.chat.id, Channel.area == Area.get_by_id(2))

    try:
        partner = channel.partner

        event_title = Prices.ON_REFERRAL_CONNECT.name
        event_price = Prices.ON_REFERRAL_CONNECT.value

        event = Event()
        event.title = event_title
        event.price = event_price
        event.channel = partner
        event.save()

    except DoesNotExist:
        pass


def process_user_connect(sender):
    print('process user connection -------------------------')
    update_user(sender)
    on_start_usage(sender)
    attach_partner(sender)


def user_viewed_news(sender):
    from orm.channel import Channel
    from orm.area import Area
    from orm.event import Event
    print('on read news')

    update = sender.update

    channel = Channel.get(Channel.channel_id == update.callback_query.message.chat.id,
                          Channel.area == Area.get_by_id(2))
    print(channel)

    try:
        event_title = Prices.ON_READ_NEWS.name
        event_price = Prices.ON_READ_NEWS.value

        event = Event()
        event.title = event_title
        event.price = event_price
        event.channel = channel
        event.save()

    except DoesNotExist:
        pass


def user_visit_link(sender):
    print('on visit link')

    from orm.channel import Channel
    from orm.area import Area
    from orm.event import Event

    update = sender.update

    channel = Channel.get(Channel.channel_id == update.callback_query.message.chat.id,
                          Channel.area == Area.get_by_id(2))
    print(channel)

    try:
        event_title = Prices.ON_VIEW_LINK.name
        event_price = Prices.ON_VIEW_LINK.value

        event = Event()
        event.title = event_title
        event.price = event_price
        event.channel = channel
        event.save()

    except DoesNotExist:
        pass
