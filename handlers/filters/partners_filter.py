from telegram.ext import BaseFilter

from constants.text import DefaultButtonTitles


class PartnersFilter(BaseFilter):
    def filter(self, message):
        return message.text == DefaultButtonTitles.PARTNERS.value
