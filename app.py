import os

import telegram
from flask import Flask, request
from telegram.ext import Dispatcher

from init_handlers import init_handlers

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
    else:
        return 'webhooks here {}'.format(token)


if __name__ == '__main__':
    app.run()
