from blinker import signal

from constants.text import EventNames
from subscribers import subscribers

start_usage_event = signal(EventNames.START_USAGE.value)
start_usage_event.connect(subscribers.process_user_connect)

read_news_event = signal(EventNames.READ_NEWS.value)
read_news_event.connect(subscribers.user_viewed_news)
read_news_event.connect(subscribers.update_user)

visit_link_event = signal(EventNames.VISIT_LINK.value)
visit_link_event.connect(subscribers.user_visit_link)
visit_link_event.connect(subscribers.update_user)

user_make_action = signal(EventNames.ANY_ACTION.value)
user_make_action.connect(subscribers.update_user)
