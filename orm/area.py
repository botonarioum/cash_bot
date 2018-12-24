from peewee import Model, CharField

from init_database import database


class Area(Model):
    title = CharField()
    token = CharField(unique=True)

    class Meta:
        database = database


if __name__ == '__main__':
    print('run')
    area = Area()
    area.title = 'example area'
    area.token = 'example token'
    area.save()
