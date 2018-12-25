from enum import Enum


class DefaultButtonTitles(Enum):
    EARN = "🤑 Заработать"
    PARTNERS = "👥 Партнёры"
    BANK = "💰 Мой банк"
    HELP = "ℹ ️Помощь"


class EarnButtonTitles(Enum):
    INVITE_FRIEND = "📢 Пригласить друга ($10.0)"
    VIEW_NEWS = "👀 Посмотреть новости ($5.0)"
    SUBSCRIBE_CHANNEL = "➕ Посетить сайт ($2.0)"
    SHARE_CONTACTS = "🤝 Рассказать о себе ($50.0)"


class BankButtonTitles(Enum):
    WITHDRAW = "💶 Вывод средств"
    PAYOUT = "👉 Страница вывода средств"


class PartnerTitles(Enum):
    PARTNER_1 = 'Google'
    PARTNER_2 = 'Yandex'


class EventNames(Enum):
    START_USAGE = 'start_usage'
    READ_NEWS = 'read_news'
    VISIT_LINK = 'visit_link'
    ANY_ACTION = 'any_action'


class ShareContactsTitles(Enum):
    PHONE = "👍 Рассказать кто ты (25 у.е)"
    LOCATION = "✌️ Рассказать откуда ты (25 у.е)"


class OtherTitles(Enum):
    BACK = '↩️ Назад'
    MORE = 'Заработать ещё'


class Prices(Enum):
    ON_USER_CONNECT = 0.0
    ON_REFERRAL_CONNECT = 10.0
    ON_READ_NEWS = 5.0
    ON_VIEW_LINK = 2.0


class Wallet(Enum):
    MIN_WITHDRAW = 300
    REFERRAL_PERCENTAGE = 10


class TransitionTitles(Enum):
    VISIT = 'Открыть сайт'
    PAID = 'Получить награду'


class SeeNewsTimeout(Enum):
    TIMEOUT = 60 * 60
