from functools import lru_cache
from pathlib import Path
from pydantic import Field, PostgresDsn
from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    """
        Projects settings

        Attributes:
            POSTGRES_DB_HOST (str): IP-address Postgres host
            POSTGRES_DB_PORT (str): Postgres port
            POSTGRES_DB_NAME (str): Postgres' DB name
            POSTGRES_DB_USER (str): Postgres' username
            POSTGRES_DB_PASSWORD (str): Postgres' user password   
    """

    POSTGRES_DB_HOST: str = Field(env='POSTGRES_DB_HOST', default='127.0.0.1')
    POSTGRES_DB_PORT: int = Field(env='POSTGRES_DB_PORT', default=5432)
    POSTGRES_DB_NAME: str = Field(
        env='POSTGRES_DB_NAME',
        default='gazprombank')
    POSTGRES_DB_USER: str = Field(alias='POSTGRES_DB_USER', default='postgres')
    POSTGRES_DB_PASSWORD: str = Field(
        env='POSTGRES_DB_PASSWORD', default='postgres'
    )

    @property
    def get_database_url(self) -> PostgresDsn:
        """
        Postgres' connection string
        """
        return f'postgresql+asyncpg://{self.POSTGRES_DB_USER}:{self.POSTGRES_DB_PASSWORD}' \
               f'@{self.POSTGRES_DB_HOST}:{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'


    class Config:
        __BASE_DIR_PATH = Path(__file__).parent.parent.parent
        __ENV_FILE_PATH = __BASE_DIR_PATH / '.env' / '.env'

        env_file = __ENV_FILE_PATH
        env_file_encoding = 'utf-8'


__settings = Settings()

@lru_cache
def get_settings_instance():
    return __settings
