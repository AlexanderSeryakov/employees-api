import logging
from envparse import Env
from pydantic_settings import BaseSettings

from .exceptions import InternalError

env = Env()


class CommonSettings(BaseSettings):
    APP_NAME: str = "Employees API"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    FACTORY: bool = True


class DatabaseSettings(BaseSettings):
    DB_URL: str = env.str("MONGODB_URL", default="mongodb://0.0.0.0@localhost:27017/employees_db")
    DB_NAME: str = ""


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

# class Settings:
#     """
#     Class with global config for application
#
#     """
#     version = "0.1.0"
#     title = "releads"
#
#     app_settings = {
#         'db_name': env.str('MONGODB_DBNAME'),
#         'mongodb_url': env.str('MONGODB'),
#         'db_username': env.str('MONGO_USER'),
#         'db_password': env.str('MONGO_PASSWORD'),
#         'max_db_conn_count': env.str('MAX_CONNECTIONS_COUNT'),
#         'min_db_conn_count': env.str('MIN_CONNECTIONS_COUNT'),
#     }
#
#     @classmethod
#     def app_settings_validate(cls):
#         for k, v in cls.app_settings.items():
#             if None is v:
#                 logging.error(f'Config variable error. {k} cannot be None')
#                 raise InternalError([{"message": "Server configure error"}])
#             else:
#                 logging.info(f'Config variable {k} is {v}')


settings = Settings()
