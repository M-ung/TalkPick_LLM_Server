from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional, List
from pydantic import BaseModel, conint 

class Settings(BaseSettings):
    # LLM 모델 설정
    MODEL_PATH: str  # 필수: 모델 파일 경로
    MODEL_TEMPERATURE: float = 0.7  # 선택: 기본값 0.7
    MODEL_MAX_TOKENS: int = 512  # 선택: 기본값 512
    MODEL_CONTEXT_LENGTH: int = 2048  # 선택: 기본값 2048
    MODEL_THREADS: int = 4  # 선택: 기본값 4

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True  

    def validate_model_path(self) -> None:
        """모델 파일 경로가 유효한지 검증"""
        if not self.MODEL_PATH:
            raise ValueError("MODEL_PATH 환경 변수가 설정되지 않았습니다.")
        
        import os
        if not os.path.exists(self.MODEL_PATH):
            raise ValueError(f"MODEL_PATH에 지정된 파일이 존재하지 않습니다: {self.MODEL_PATH}")

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    settings.validate_model_path() 
    return settings 