from fastapi import APIRouter
from ..service.topic_service import TopicService
from ..dto.request.topic_req_dto import TopicReqDTO
from ..dto.response.topic_res_dto import TopicResDTO

router = APIRouter(prefix="/api/v1")

@router.post("/topics/recommend", response_model=TopicResDTO)
async def recommend_topics(request: TopicReqDTO):
    service = TopicService()
    return await service.recommend(request) 