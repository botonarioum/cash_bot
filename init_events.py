from blinker import signal

from constants.text import EventNames
from subscribers.subscribers import update_user

start_usage_event = signal(EventNames.START_USAGE.value)
start_usage_event.connect(update_user)
