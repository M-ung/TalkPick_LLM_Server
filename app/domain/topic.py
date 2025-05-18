from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from ..config.database import Base
from .base_time import BaseTime
from enum import Enum as PyEnum

class TalkPickStatus(PyEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class CategoryGroup(PyEnum):
    STRANGER = "STRANGER"
    CLOSE = "CLOSE"

class Topic(Base, BaseTime):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    detail = Column(String)
    thumbnail = Column(String)
    icon = Column(String)
    category_id = Column(Integer)
    status = Column(Enum(TalkPickStatus))
    created_by_id = Column(Integer) 