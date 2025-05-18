from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..service.topic_service import TopicService
from ..repository.topic_repository import TopicRepository
from ..dto.request.topic_request import TopicRequest
from ..dto.response.topic_response import TopicListResponse

router = APIRouter(prefix="/api/v1")
@router.post("/random/recommend", response_model=TopicListResponse)
async def recommend_topics(
    request: TopicRequest,
    db: Session = Depends(get_db)
):
    repository = TopicRepository(db)
    service = TopicService(repository)
    return await service.get_recommendations(request) 