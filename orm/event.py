from peewee import Model, IntegerField, CharField, ForeignKeyField, TimestampField, DateTimeField

from init_database import database
from orm.channel import Channel


class Event(Model):
    title = CharField(null=True)
    price = IntegerField()
    channel = ForeignKeyField(Channel)
    created_at = DateTimeField()

    class Meta:
        database = database


if __name__ == '__main__':
    print('run')
    event = Event()
    event.title = 'register'
    event.price = 100
    event.channel = Channel.get_by_id(3)
    event.save()
