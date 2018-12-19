from blinker import signal

from constants.text import EventNames
from subscribers import subscribers

start_usage_event = signal(EventNames.START_USAGE.value)
start_usage_event.connect(subscribers.update_user)
start_usage_event.connect(subscribers.on_start_usage)
