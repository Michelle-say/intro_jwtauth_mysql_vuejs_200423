from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int
    MYSQL_PASSWORD: str
    MYSQL_USER: str
    MYSQL_DB: str
    MYSQL_HOST: str
    MYSQL_HOSTNAME: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = './.env'


settings = Settings()