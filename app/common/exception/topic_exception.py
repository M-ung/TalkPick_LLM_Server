from enum import Enum
from typing import Optional

class ErrorCode(Enum):
    # 4XX 에러
    INVALID_TOPIC_REQUEST = ("INVALID_TOPIC_REQUEST", "잘못된 주제 추천 요청입니다.", 400)
    INSUFFICIENT_TOPICS = ("INSUFFICIENT_TOPICS", "추천할 수 있는 주제가 부족합니다.", 400)
    LLM_RESPONSE_PARSING_ERROR = ("LLM_RESPONSE_PARSING_ERROR", "주제 추천 처리 중 오류가 발생했습니다.", 400)
    
    # 5XX 에러
    INTERNAL_SERVER_ERROR = ("INTERNAL_SERVER_ERROR", "내부 서버 오류가 발생했습니다.", 500)
    LLM_SERVER_ERROR = ("LLM_SERVER_ERROR", "LLM 서버 처리 중 오류가 발생했습니다.", 500)

    def __init__(self, code: str, message: str, status: int):
        self.code = code
        self.message = message
        self.status = status

class ErrorResponse:
    def __init__(
        self,
        error_code: ErrorCode,
        detail: Optional[str] = None
    ):
        self.success = False
        self.status = error_code.status
        self.code = error_code.code
        self.message = error_code.message
        self.detail = detail

    def to_dict(self):
        response = {
            "success": self.success,
            "status": self.status,
            "error": {
                "code": self.code,
                "message": self.message
            }
        }
        if self.detail:
            response["error"]["detail"] = self.detail
        return response

class TopicException(Exception):
    def __init__(self, error_code: ErrorCode, detail: Optional[str] = None):
        self.error_code = error_code
        self.detail = detail
        super().__init__(error_code.message)

    def to_response(self):
        return ErrorResponse(self.error_code, self.detail).to_dict() 