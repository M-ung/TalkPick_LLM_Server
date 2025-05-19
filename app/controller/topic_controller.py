from fastapi import APIRouter
from ..service.topic_service import TopicService
from ..dto.request.topic_req_dto import TopicReqDTO
from ..dto.response.topic_res_dto import TopicResDTO
from app.common.exception.topic_exception import TopicException

router = APIRouter(prefix="/api/v1")

@router.post("/topics/recommend", response_model=TopicResDTO)
async def recommend_topics(request: TopicReqDTO):
    try:
        service = TopicService()
        return await service.recommend(request)
    except TopicException as e:
        raise HTTPException(
            status_code=400,
            detail={
                "message": e.message,
                "error_code": e.error_code
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "내부 서버 오류가 발생했습니다.",
                "error_code": "INTERNAL_SERVER_ERROR"
            }
        )