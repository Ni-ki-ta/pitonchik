from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    DB_NAME: str
    DB_NAME_p: str
    DB_NAME_q: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        #populate_by_name=True,
        case_sensitive=False,
    )
    reset_password_token_secret: str
    verification_token_secret: str
    lifetime_seconds: int = 3600

    bearer_token_url: str = "auth/login"
    #ACCESS_TOKEN: AccessToken

    @property
    def DATABASE_URL_psycopg(self):
        return f"sqlite:///{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg_postgres(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_q}"


settings = Settings()
