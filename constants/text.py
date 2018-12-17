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
    SHARE_CONTACTS = "🤝 Указать контакты  (25 у.е)"


class BankButtonTitles(Enum):
    WITHDRAW = "💶 Вывод средств"


class PartnerTitles(Enum):
    PARTNER_1 = 'Google'
    PARTNER_2 = 'Yandex'


class EventNames(Enum):
    START_USAGE = 'start_usage'
