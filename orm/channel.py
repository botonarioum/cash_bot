import datetime

from peewee import Model, IntegerField, CharField, DateTimeField, ForeignKeyField

from dev import database
from orm.area import Area


class Channel(Model):
    area = ForeignKeyField(Area)

    channel_id = IntegerField()

    first_name = CharField(null=True)
    last_name = CharField(null=True)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def update_me(self):
        self.updated_at = datetime.datetime.now()
        self.save()

    class Meta:
        database = database


if __name__ == '__main__':
    print('run')
    channel = Channel()
    channel.area = Area.get_by_id(2)
    channel.channel_id = 1
    channel.first_name = 'John'
    channel.last_name = 'Doe'
    channel.save()
