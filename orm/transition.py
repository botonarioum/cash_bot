import os
from enum import Enum

from peewee import Model, ForeignKeyField, CharField

from init_database import database
from orm.channel import Channel


class STATUSES(Enum):
    NEW = 'new'
    VISIT = 'visit'
    PAID = 'paid'


class Transition(Model):
    channel = ForeignKeyField(Channel)
    status = CharField()

    def mark_as(self, new_status):
        self.status = new_status
        self.save()

    def get_redirect_url(self):
        redirect_url_pattern = os.getenv('REDIRECT_URL')

        return redirect_url_pattern.format(self.get_id())

    class Meta:
        database = database


if __name__ == '__main__':
    print('run')
    status = STATUSES.NEW
    print(status)
