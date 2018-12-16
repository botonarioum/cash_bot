from telegram.ext import BaseFilter

from constants.text import DefaultButtonTitles


class HelpFilter(BaseFilter):
    def filter(self, message):
        return message.text == DefaultButtonTitles.HELP.value
