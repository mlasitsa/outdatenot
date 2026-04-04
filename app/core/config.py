from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, RedisDsn


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

    model_config = SettingsConfigDict(env_file=".env", extra="forbid")


# Required fields are supplied at runtime by environment variables / .env (pydantic-settings)
# static analyzers cannot see that, so they flag a bare `Settings()` call, we can safely ignore the error.
settings = Settings()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]



