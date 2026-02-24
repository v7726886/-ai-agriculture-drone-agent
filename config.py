import os
from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    api_key: str
    database_url: AnyHttpUrl
    secret_key: str
    
    class Config:
        env_file = ".env"  # Load environment variables from a .env file
        env_file_encoding = 'utf-8'

settings = Settings()