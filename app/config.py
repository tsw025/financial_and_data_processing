import os

from pydantic import Field
from pydantic_settings import BaseSettings

dir_path = os.path.dirname(os.path.realpath(__file__))


class Settings(BaseSettings):
    database_url: str = Field(env="DATABASE_URL")

    class Config:
        env_file = f"{dir_path}/.env"
        extra = "ignore"


SETTINGS = Settings()
