from constants.text import Wallet
from menu import bank_menu


def balance(bot, update):
    reply_markup = bank_menu.menu(bot, update)

    total, min_withdraw = float(get_balance(bot, update)), float(Wallet.MIN_WITHDRAW.value)

    message = """
    Ваш баланс: ${}
Минимальная сумма вывода: ${}""".format(total, min_withdraw)
    update.message.reply_text(message, reply_markup=reply_markup)


def withdraw(bot, update):
    if get_balance(bot, update) >= Wallet.MIN_WITHDRAW.value:
        message = """Отлично. Теперь ВЫ можете вывести заработаные деньги, перейдите по ссылке:"""
        message_id = update.callback_query.message.message_id
        chat_id = update.callback_query.message.chat.id
        bot.editMessageReplyMarkup(chat_id, message_id)
        bot.sendMessage(chat_id, message, reply_markup=bank_menu.withdraw(bot, update))
    else:
        message = """ВЫ не достигли минимальной суммы для выплаты, РАБОТАЙТЕ УСЕРДНЕЕ!"""
        message_id = update.callback_query.message.message_id
        chat_id = update.callback_query.message.chat.id
        bot.editMessageReplyMarkup(chat_id, message_id)
        bot.sendMessage(chat_id, message)


def get_balance(bot, update):
    from orm.event import Event
    from orm.area import Area
    from orm.channel import Channel

    if update.callback_query:
        channel_id = update.callback_query.message.chat.id
    else:
        channel_id = update.message.chat.id

    area = Area.get_by_id(2)

    current_channel = Channel.get(Channel.area == area, Channel.channel_id == channel_id)
    referrals = Channel.select().where(Channel.partner == current_channel)

    current_channel_events = Event.select().where(Event.channel == current_channel)
    referral_events = Event.select().where(Event.channel << referrals)

    return sum(
        [sum(map(lambda e: e.price, current_channel_events)),
         sum(map(lambda e: e.price / 100 * Wallet.REFERRAL_PERCENTAGE.value, referral_events))
         ]
    )
