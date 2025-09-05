from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Ищет .env в текущей и родительских папках
DB_URL = os.getenv('DB_URL')
BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class Settings(BaseSettings):
    DB_NAME: str
    DB_NAME_p: str
    DB_NAME_q: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    auth_jwt: AuthJWT = AuthJWT()

    @property
    def DATABASE_URL_psycopg(self):
        return f"sqlite:///{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg_postgres(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_q}"

    model_config = SettingsConfigDict(env_file=DB_URL)


settings = Settings()
