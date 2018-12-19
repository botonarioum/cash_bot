import os

from handlers.bank import get_balance
from menu.helpers import get_chat_id


def partners(bot, update):
    from orm.area import Area
    from orm.channel import Channel

    area = Area.get_by_id(2)

    channel_id = get_chat_id(update)

    referral_link = os.getenv('REFERRAL_LINK_PATTERN')
    current_channel = Channel.get(Channel.area == area, Channel.channel_id == channel_id)

    balance = get_balance(bot, update)
    referrals = Channel.select().where(Channel.partner == current_channel)

    message = """
    Приглашайте партнёров в бот и получайте за них деньги!

Отправьте другу ссылку
{}

10$ за каждого приглашенного Вами партнёра
10% от заработка ваших друзей

Приглашено пользователей: {}
Заработок: {}$""".format(
        referral_link.format(get_chat_id(update)),
        len(referrals),
        float(balance)
    )
    update.message.reply_text(message)
