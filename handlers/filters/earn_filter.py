from telegram.ext import BaseFilter

from constants.text import DefaultButtonTitles


class EarnFilter(BaseFilter):
    def filter(self, message):
        return message.text == DefaultButtonTitles.EARN.value
