from telegram.ext import BaseFilter

from constants.text import OtherTitles


class BackFilter(BaseFilter):
    def filter(self, message):
        return message.text == OtherTitles.BACK.value
