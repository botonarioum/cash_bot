import os

from peewee import PostgresqlDatabase

# setting_path = os.path.join(Path(dirname(__file__)).parent, '.env.example')
# if os.path.isfile(setting_path):
#     dotenv_path = join(dirname(__file__), setting_path)
#     load_dotenv(dotenv_path)
#
# DATABASE_CREDENTIALS = {
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASSWORD'),
#     'host': os.getenv('DB_HOST'),
#     'port': int(os.getenv('DB_PORT'))
# }

database = None


def prepare_credentials():
    return {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT'))
    }


def init_database(credentials=None):
    global database
    credentials = credentials or prepare_credentials()
    if database is None:
        database = PostgresqlDatabase(os.getenv('DB_NAME'), **credentials)
        return init_database(credentials)
    return database
