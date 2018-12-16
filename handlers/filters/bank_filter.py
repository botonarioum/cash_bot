from telegram.ext import BaseFilter

from constants.text import DefaultButtonTitles


class BankFilter(BaseFilter):
    def filter(self, message):
        return message.text == DefaultButtonTitles.BANK.value
