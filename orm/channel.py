import datetime

from peewee import Model, IntegerField, CharField, DateTimeField, ForeignKeyField

from init_database import database
from orm.area import Area


class Channel(Model):
    area = ForeignKeyField(Area)
    partner = ForeignKeyField('self', null=True)

    channel_id = IntegerField()

    first_name = CharField(null=True)
    last_name = CharField(null=True)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def set_partner(self, partner):
        self.partner = partner
        self.update_me()

    def update_me(self, now=None):
        self.updated_at = now or datetime.datetime.now()
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
