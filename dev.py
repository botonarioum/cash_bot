#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import os
from time import sleep

import telegram
from dotenv import load_dotenv, find_dotenv
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Dispatcher

from events.events import AnyAction
from init_database import init_database
from init_events import user_make_action
from init_handlers import init_handlers

load_dotenv(find_dotenv())
init_database()

update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(os.getenv('TELEGRAM_TOKEN'))

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # ------------------------
    dispatcher = Dispatcher(bot, None)
    # ------------------------

    while True:
        try:
            echo(bot, dispatcher)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot, dispatcher):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        init_handlers(dispatcher)

        # todo: update user
        user_make_action.send(AnyAction(bot, update))
        dispatcher.process_update(update)


if __name__ == '__main__':
    main()
