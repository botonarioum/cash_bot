from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from handlers import start, earn, bank, partners, contact, default, share_contacts, help
from handlers.filters.back_filter import BackFilter
from handlers.filters.bank_filter import BankFilter
from handlers.filters.earn_filter import EarnFilter
from handlers.filters.help_filter import HelpFilter
from handlers.filters.partners_filter import PartnersFilter


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start.info))
    dispatcher.add_handler(MessageHandler(EarnFilter(), earn.earn))
    dispatcher.add_handler(MessageHandler(BankFilter(), bank.balance))
    dispatcher.add_handler(MessageHandler(HelpFilter(), help.help))
    dispatcher.add_handler(MessageHandler(PartnersFilter(), partners.partners))
    dispatcher.add_handler(CallbackQueryHandler(bank.withdraw, False, False, 'bank.action.withdraw'))
    dispatcher.add_handler(CallbackQueryHandler(contact.share_info, False, False, 'earn.action.share_contacts'))
    dispatcher.add_handler(CallbackQueryHandler(earn.invite_friend, False, False, 'earn.action.invite_friend'))
    dispatcher.add_handler(CallbackQueryHandler(earn.see_news, False, False, 'earn.action.view_news'))
    dispatcher.add_handler(CallbackQueryHandler(earn.pickup_more, False, False, 'user.action.more'))
    dispatcher.add_handler(MessageHandler(Filters.text, default.select_menu_item))
    dispatcher.add_handler(MessageHandler(BackFilter(), default.select_menu_item))
    dispatcher.add_handler(MessageHandler(Filters.location, share_contacts.save_location))
    dispatcher.add_handler(MessageHandler(Filters.contact, share_contacts.save_phone))
    # dispatcher.process_update(update)

    # return dispatcher