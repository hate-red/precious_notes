from celery import Celery

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    BASE_URL: str
    BASE_DIR: Path = Path(__file__).parent

    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env')


settings = Settings() # type: ignore

redis_url = f'redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:' \
            f'{settings.REDIS_PORT}/0'

celery_app = Celery(
    'celery_worker',
    broker=redis_url,
    backend=redis_url,
)