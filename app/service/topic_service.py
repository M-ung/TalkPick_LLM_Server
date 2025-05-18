from typing import List
from ..repository.topic_repository import TopicRepository
from ..dto.request.topic_request import TopicRequest
from ..dto.response.topic_response import TopicResponse, TopicListResponse

class TopicService:
    def __init__(self, repository: TopicRepository):
        self.repository = repository

    async def get_recommendations(self, request: TopicRequest) -> TopicListResponse:
        # TODO: 실제 구현에서는 사용된 주제 ID 목록을 DB에서 가져와야 함
        used_topic_ids = []  
        
        topics = self.repository.find_recommended_topics(
            request.member_id,
            request.random_id,
            used_topic_ids
        )
        
        topic_responses = [
            TopicResponse(
                id=topic.id,
                title=topic.title,
                detail=topic.detail,
                thumbnail=topic.thumbnail,
                icon=topic.icon,
                category_id=topic.category_id
            ) for topic in topics
        ]
        
        return TopicListResponse(topics=topic_responses) 