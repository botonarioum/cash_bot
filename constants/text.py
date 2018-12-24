from enum import Enum


class DefaultButtonTitles(Enum):
    EARN = "🤑 Заработать"
    PARTNERS = "👥 Партнёры"
    BANK = "💰 Мой банк"
    HELP = "ℹ ️Помощь"


class EarnButtonTitles(Enum):
    INVITE_FRIEND = "📢 Пригласить друга (10 у.е)"
    VIEW_NEWS = "👀 Посмотреть новости (3 у.е)"
    SUBSCRIBE_CHANNEL = "➕ Посетить сайт (0.5 у.е)"
    SHARE_CONTACTS = "🤝 Рассказать о себе (50 у.е)"


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


class ShareContactsTitles(Enum):
    PHONE = "👍 Рассказать кто ты (25 у.е)"
    LOCATION = "✌️ Рассказать откуда ты (25 у.е)"


class OtherTitles(Enum):
    BACK = '↩️ Назад'
    MORE = 'Заработать ещё'


class Prices(Enum):
    ON_USER_CONNECT = 0
    ON_REFERRAL_CONNECT = 50
    ON_READ_NEWS = 3
    ON_VIEW_LINK = 0.5


class Wallet(Enum):
    MIN_WITHDRAW = 100
    REFERRAL_PERCENTAGE = 10


class TransitionTitles(Enum):
    VISIT = 'Открыть сайт'
    PAID = 'Получить награду'


class SeeNewsTimeout(Enum):
    TIMEOUT = 60 * 60
