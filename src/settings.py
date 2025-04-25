from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Application(BaseSettings):

    name: str = Field(default="Orders services")
    version: str = Field(default="0.1")
    secret_key: str = Field(default="SECRET_KEY")
    host: str = Field(default="localhost")
    port: int = Field(default=8000)


class KafkaSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="KAFKA_")
    host: str = Field(default="localhost")
    port: int = Field(default=9092)

    @property
    def kafka_url(self) -> str:
        return f"{self.host}:{self.port}"


class Postgres(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    host: str = Field(default="localhost")
    port: int = Field(default=5432)
    user: str = Field(default="admin")
    password: str = Field(default="admin")
    database: str = Field(default="postgres")
    echo: bool = Field(default=False)

    @property
    def async_url(self) -> str:
        driver = "postgresql+psycopg"
        client_encoding = "client_encoding=utf8"
        return f"{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?{client_encoding}"

    @property
    def sync_url(self) -> str:
        driver = "postgresql"
        return f"{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):
    application: Application = Field(default=Application())
    postgres: Postgres = Field(default=Postgres())
    kafka: KafkaSettings = Field(default=KafkaSettings())


def get_settings() -> Settings:
    return Settings()
