import os
from datetime import datetime, timedelta
from time import sleep

from peewee import DoesNotExist

from constants.text import SeeNewsTimeout, Prices
from events.events import ReadNews, VisitLink
from init_events import read_news_event, visit_link_event
from menu import earn_menu
from menu.helpers import get_chat_id, get_message_id
from orm.area import Area
from orm.channel import Channel
from orm.event import Event
from orm.transition import Transition, STATUSES


def earn(bot, update):
    reply_markup = earn_menu.menu(bot, update)

    message = 'Выбери способ заработка:'
    update.message.reply_text(message, reply_markup=reply_markup)


def invite_friend(bot, update):
    referral_link = os.getenv('REFERRAL_LINK_PATTERN')

    message = """
Делитесь ссылкой с друзьями и зарабатывайте вместе:
{}""".format(referral_link.format(update.callback_query.message.chat.id))
    chat_id = update.callback_query.message.chat.id

    bot.sendMessage(chat_id, message)


def last_see_news_event(bot, update):
    try:
        if update.callback_query:
            channel_id = update.callback_query.message.chat.id
        else:
            channel_id = update.message.chat.id

        area = Area.get_by_id(2)

        current_channel = Channel.get(Channel.area == area, Channel.channel_id == channel_id)
        return Event.select().order_by(Event.created_at.desc()).where(Event.title == Prices.ON_READ_NEWS.name,
                                                                      Event.channel == current_channel).get()
    except DoesNotExist:
        return None


def see_news_available(bot, update):
    channel_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id

    position = 0
    balance = 0.00

    message = None

    for item in news():
        position += 1
        balance += 0.30

        text = """
    Выполнено: {} из {}
    Текущая статья: {}
    ---------------------
    Заработок с просмотра: ${}
            """.format(position, len(news()), item, round(balance, 2))

        if message:
            channel_id = message.chat.id
            message_id = message.message_id

            bot.editMessageText(text, channel_id, message_id)
        else:
            channel_id = update.callback_query.message.chat.id
            message_id = update.callback_query.message.message_id

            message = bot.sendMessage(channel_id, text)

        sleep(3)

    bot.editMessageText('Выполнено: {} из {}'.format(len(news()), len(news())), channel_id, message_id)
    call_events(bot, update)
    bot.sendMessage(channel_id, 'Вам начисленно: $3.0')

    referral_link = os.getenv('REFERRAL_LINK_PATTERN')

    message = """
        Делитесь ссылкой с друзьями и зарабатывайте вместе:
        {}""".format(referral_link.format(update.callback_query.message.chat.id))
    chat_id = update.callback_query.message.chat.id

    reply_markup = earn_menu.pickup_more(bot, update)

    bot.sendMessage(chat_id, message, reply_markup=reply_markup)

    return True


def see_news_unavailable(bot, update, prev_event):
    channel_id = update.callback_query.message.chat.id

    # wait = (prev_event.created_at + timedelta(seconds=SeeNewsTimeout.TIMEOUT.value)) - datetime.now()
    # wait_in_minutes = int(wait.total_seconds() / 60)

    # bot.sendMessage(channel_id, 'Текущее задание будет доступно через {} мин.'.format(wait_in_minutes))
    bot.sendMessage(channel_id, 'Текущее задани ещё не готово')
    return True


def see_news(bot, update):
    print('SEE NEWS')

    # channel_id = update.callback_query.message.chat.id
    # message_id = update.callback_query.message.message_id

    prev_event = last_see_news_event(bot, update)

    if prev_event and (datetime.now() < prev_event.created_at + timedelta(seconds=SeeNewsTimeout.TIMEOUT.value)):
        return see_news_unavailable(bot, update, prev_event)
        # print(datetime.now())
        # print('ok')
        # print(SeeNewsTimeout.TIMEOUT.value)
        # wait = (prev_event.created_at + timedelta(seconds=SeeNewsTimeout.TIMEOUT.value)) - datetime.now()
        # print(wait)
        # print(datetime.now())
        # wait_in_munutes = int(wait.total_seconds() / 60)
        #
        # bot.sendMessage(channel_id, 'Текущее задание будет доступно через {} мин.'.format(wait_in_munutes))
        # return False
    return see_news_available(bot, update)

#     position = 0
#     balance = 0.00
#
#     message = None
#
#     for item in news():
#         position += 1
#         balance += 0.30
#
#         text = """
# Выполнено: {} из {}
# Текущая статья: {}
# ---------------------
# Заработок с просмотра: ${}
#         """.format(position, len(news()), item, round(balance, 2))
#
#         if message:
#             channel_id = message.chat.id
#             message_id = message.message_id
#
#             bot.editMessageText(text, channel_id, message_id)
#         else:
#             channel_id = update.callback_query.message.chat.id
#             message_id = update.callback_query.message.message_id
#
#             message = bot.sendMessage(channel_id, text)
#
#         sleep(3)
#
#     bot.editMessageText('Выполнено: {} из {}'.format(len(news()), len(news())), channel_id, message_id)
#     call_events(bot, update)
#     bot.sendMessage(channel_id, 'Вам начисленно: $3.0')
#
#     referral_link = os.getenv('REFERRAL_LINK_PATTERN')
#
#     message = """
#     Делитесь ссылкой с друзьями и зарабатывайте вместе:
#     {}""".format(referral_link.format(update.callback_query.message.chat.id))
#     chat_id = update.callback_query.message.chat.id
#
#     reply_markup = earn_menu.pickup_more(bot, update)
#
#     bot.sendMessage(chat_id, message, reply_markup=reply_markup)
#
#     return True


def news():
    return [
        # 'РБК',
        # 'Коммерсантъ',
        # 'Эхо Москвы',
        # 'Газета.Ru',
        # 'PressaRU',
        # 'Российская газета',
        # 'Аргументы и Факты',
        # 'Lenta RU',
        # 'Московский комсомолец',
        # 'Мир новостей',
    ]


def call_events(bot, update):
    read_news_event.send(ReadNews(bot, update))


def pickup_more(bot, update):
    reply_markup = earn_menu.menu(bot, update)

    chat_id = get_chat_id(update)
    message_id = get_message_id(update)

    bot.editMessageReplyMarkup(chat_id, message_id, reply_markup=reply_markup)


def visit_url(bot, update):
    from orm.transition import Transition, STATUSES
    transition = Transition()
    transition.status = STATUSES.NEW.value
    transition.channel = 10
    transition.save()

    reply_markup = earn_menu.visit_url_menu(bot, update, transition)

    chat_id = get_chat_id(update)

    message = """
Задание:
1) Посетите сайт наших партнёров
2) Возвращайтесь сюда и получите вознаграждение."""

    bot.sendMessage(chat_id, message, reply_markup=reply_markup)


def paid_for_visit(bot, update):
    channel_id = update.callback_query.message.chat.id

    try:
        callback_data = update.callback_query.data
        transition_id = callback_data.split('.').pop()

        transition = Transition.get_by_id(transition_id)

        if transition.status == STATUSES.VISIT.value:
            visit_link_event.send(VisitLink(bot, update))
            transition.mark_as(STATUSES.PAID.value)

            bot.sendMessage(channel_id, 'Вам начисленно: $0.5')

            referral_link = os.getenv('REFERRAL_LINK_PATTERN')

            message = """
                Делитесь ссылкой с друзьями и зарабатывайте вместе:
                {}""".format(referral_link.format(update.callback_query.message.chat.id))
            chat_id = update.callback_query.message.chat.id

            reply_markup = earn_menu.pickup_more(bot, update)

            bot.sendMessage(chat_id, message, reply_markup=reply_markup)
        elif transition.status == STATUSES.NEW.value:
            bot.sendMessage(channel_id, 'Для начала выполните задание - перейдите по ссылке!')
        else:
            bot.sendMessage(channel_id, 'Вы уже получили награду за выполнение этого задания!')
    except DoesNotExist:
        print('transition not found')
