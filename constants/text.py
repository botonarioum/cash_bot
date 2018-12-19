from enum import Enum


class DefaultButtonTitles(Enum):
    EARN = "🤑 Заработать"
    PARTNERS = "👥 Партнёры"
    BANK = "💰 Мой банк"
    HELP = "ℹ ️Помощь"


class EarnButtonTitles(Enum):
    INVITE_FRIEND = "📢 Пригласить друга (10 у.е)"
    VIEW_NEWS = "👀 Посмотреть новости (3 у.е)"
    SUBSCRIBE_CHANNEL = "➕ Подписаться на канал (10 у.е)"
    SHARE_CONTACTS = "🤝 Рассказать о себе (50 у.е)"


class BankButtonTitles(Enum):
    WITHDRAW = "💶 Вывод средств"


class PartnerTitles(Enum):
    PARTNER_1 = 'Google'
    PARTNER_2 = 'Yandex'


class EventNames(Enum):
    START_USAGE = 'start_usage'


class ShareContactsTitles(Enum):
    PHONE = "👍 Рассказать кто ты (25 у.е)"
    LOCATION = "✌️ Рассказать откуда ты (25 у.е)"


class OtherTitles(Enum):
    BACK = '↩️ Назад'


class Prices(Enum):
    ON_USER_CONNECT = 0
    ON_REFERRAL_CONNECT = 50
