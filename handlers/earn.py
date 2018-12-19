import os
from time import sleep

from events.events import ReadNews
from init_events import read_news_event
from menu import earn_menu


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


def see_news(bot, update):
    channel_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id

    position = 0
    balance = 0.00
    for item in news():
        position += 1
        balance += 0.30

        message = """
Выполнено: {} из {}
Текущая статья: {}
---------------------
Заработок с просмотра: ${}
        """.format(position, len(news()), item, round(balance, 2))
        bot.editMessageText(message, channel_id, message_id)
        sleep(3)

    bot.editMessageText('Выполнено: {}  из {}'.format(len(news()), len(news())), channel_id, message_id)
    call_events(bot, update)
    bot.sendMessage(channel_id, 'Вам начисленно: $3.0')

    invite_friend(bot, update)


def news():
    return [
        'РБК',
        'Коммерсантъ',
        'Эхо Москвы',
        'Газета.Ru',
        'PressaRU',
        'Российская газета',
        'Аргументы и Факты',
        'Lenta RU',
        'Московский комсомолец',
        'Мир новостей',
    ]


def call_events(bot, update):
    read_news_event.send(ReadNews(bot, update))
