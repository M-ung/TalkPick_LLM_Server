from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from ..domain.topic import Topic, TalkPickStatus

class TopicRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, topic_id: int) -> Optional[Topic]:
        return self.db.query(Topic).filter(Topic.id == topic_id).first()

    def find_recommended_topics(
        self, 
        member_id: int, 
        random_id: int, 
        used_topic_ids: List[int]
    ) -> List[Topic]:
        query = self.db.query(Topic).filter(
            Topic.status == TalkPickStatus.ACTIVE,
            Topic.id.notin_(used_topic_ids)
        )
        
        # 랜덤하게 4개 선택
        return query.order_by(func.random()).limit(4).all()

    def save(self, topic: Topic) -> Topic:
        self.db.add(topic)
        self.db.commit()
        self.db.refresh(topic)
        return topic 