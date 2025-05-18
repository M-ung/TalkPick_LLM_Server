from sqlalchemy import Column, BigInteger, Enum
from ....config.database import Base
from ...base_time import BaseTime
from ..type.keyword import Keyword

class TopicKeyword(Base, BaseTime):
    __tablename__ = "topic_keyword"

    id = Column(BigInteger, primary_key=True)
    topic_id = Column(BigInteger)
    keyword = Column(Enum(Keyword)) 