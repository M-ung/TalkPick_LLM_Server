from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # LLM Model settings
    MODEL_PATH: str
    MODEL_TEMPERATURE: float = 0.7
    MODEL_MAX_TOKENS: int = 2000
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings() 