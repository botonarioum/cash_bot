from constants.text import EventNames


class StartUsage:
    EVENT_NAME = EventNames.START_USAGE.value

    bot = None
    update = None

    def __init__(self, bot, update):
        self.bot = bot
        self.update = update


class ReadNews:
    EVENT_NAME = EventNames.READ_NEWS.value

    bot = None
    update = None

    def __init__(self, bot, update):
        self.bot = bot
        self.update = update
