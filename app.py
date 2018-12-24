import os
from random import choice

import telegram
from flask import Flask, request, redirect
from telegram.ext import Dispatcher

from init_database import init_database

init_database()

from init_handlers import init_handlers
from orm.transition import Transition, STATUSES

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook/<token>', methods=['GET', 'POST'])
def webhook_endpoint(token):
    if request.method == 'POST':
        bot = telegram.Bot(os.getenv('TELEGRAM_TOKEN'))
        dispatcher = Dispatcher(bot, None, workers=0)

        init_handlers(dispatcher)

        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'webhooks here {}'.format(token)


@app.route('/earn/<redirect_id>', methods=['GET', 'POST'])
def visit_partner(redirect_id):
    routes = [
        'https://google.com',
        'https://yandex.ru'
    ]

    transition = Transition.get_by_id(redirect_id)
    transition.mark_as(STATUSES.VISIT.value)

    selected_route = choice(routes)

    return redirect(selected_route)


if __name__ == '__main__':
    app.run()
