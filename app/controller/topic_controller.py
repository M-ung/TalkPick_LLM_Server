from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..service.topic_service import TopicService
from ..repository.topic_repository import TopicRepository
from ..dto.request.topic_req_dto import TopicReqDTO
from ..dto.response.topic_res_dto import TopicResDTO

router = APIRouter(prefix="/api/v1")

@router.post("/topics/recommend", response_model=TopicResDTO)
async def recommend_topics(
    request: TopicReqDTO,
    db: Session = Depends(get_db)
):
    repository = TopicRepository(db)
    service = TopicService(repository)
    return await service.recommend(request) 