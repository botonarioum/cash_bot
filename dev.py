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
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handlers import default
from handlers import earn
from handlers import bank
from handlers import start
from handlers import help
from handlers import partners
from handlers.filters.earn_filter import EarnFilter
from handlers.filters.bank_filter import BankFilter
from handlers.filters.help_filter import HelpFilter
from handlers.filters.partners_filter import PartnersFilter

load_dotenv(find_dotenv())

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

        # if update.message:
        dispatcher.add_handler(CommandHandler('start', start.info))
        dispatcher.add_handler(MessageHandler(EarnFilter(), earn.earn))
        dispatcher.add_handler(MessageHandler(BankFilter(), bank.balance))
        dispatcher.add_handler(MessageHandler(HelpFilter(), help.help))
        dispatcher.add_handler(MessageHandler(PartnersFilter(), partners.partners))
        dispatcher.add_handler(CallbackQueryHandler(bank.withdraw, False, False, 'bank.action.withdraw'))
        dispatcher.add_handler(MessageHandler(Filters.text, default.select_menu_item))
        dispatcher.process_update(update)


if __name__ == '__main__':
    main()
