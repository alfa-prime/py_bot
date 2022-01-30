from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOKEN")

    log_level: str = Field(..., env="LOG_LEVEL")
    log_output: str = Field(..., env="LOG_OUTPUT")

    class Config:
        env_file = './.env'
        env_file_encoding = "utf-8"


settings = Settings()
