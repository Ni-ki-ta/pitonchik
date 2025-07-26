from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Ищет .env в текущей и родительских папках
DB_URL = os.getenv('DB_URL')

class Settings(BaseSettings):
    DB_NAME: str

    @property
    def DATABASE_URL_psycopg(self):
        return f"sqlite:///{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=DB_URL)


settings = Settings()
