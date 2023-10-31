from envparse import Env
from pydantic_settings import BaseSettings

env = Env()


class CommonSettings(BaseSettings):
    APP_NAME: str = "Employees API"
    DEBUG_MODE: bool = env.bool("DEBUG")
    MODE: str = env.str("MODE")  # DEV, TEST, PROD


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    FACTORY: bool = True


class DatabaseSettings(BaseSettings):
    DB_URL: str = env.str("MONGODB_URL", default="mongodb://0.0.0.0@localhost:27017")
    TEST_DB_URL: str = env.str("TEST_MONGODB_URL", default="mongodb://0.0.0.0@localhost:27017/test_dv")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
