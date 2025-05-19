from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from .topic_exception import TopicException, ErrorCode, ErrorResponse

def init_exception_handlers(app: FastAPI):
    @app.exception_handler(TopicException)
    async def topic_exception_handler(request: Request, exc: TopicException):
        return JSONResponse(
            status_code=exc.error_code.status,
            content=exc.to_response()
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        error_response = ErrorResponse(
            ErrorCode.INTERNAL_SERVER_ERROR,
            str(exc)
        )
        return JSONResponse(
            status_code=500,
            content=error_response.to_dict()
        ) 