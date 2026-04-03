from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, RedisDsn


configDict: dict = {
    "env_file": ".env",
    "extra": "forbid"
}

class Settings(BaseSettings):
    app_name: str = "outdatenot"
    environment: str = "local"
    debug: bool = True
    version: str


    database_url: PostgresDsn
    redis_url: RedisDsn
    github_id: int
    github_private_key: str
    github_webhook_secret: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    model_config = SettingsConfigDict(**configDict)

settings = Settings()



