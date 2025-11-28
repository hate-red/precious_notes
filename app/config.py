from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    # Postgres settings
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # for passwords
    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file = ROOT_DIR / '.env',
    )
    

settings = Settings() # type: ignore


def get_db_url():
    return (
        f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@'
        f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
    )


def get_auth_data():
    return {
        'secret_key': settings.SECRET_KEY,
        'algorithm': settings.ALGORITHM,
    }
