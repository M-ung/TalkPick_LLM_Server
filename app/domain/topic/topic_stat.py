from sqlalchemy import Column, Integer, BigInteger, Version
from ....config.database import Base
from ...base_time import BaseTime

class TopicStat(Base, BaseTime):
    __tablename__ = "topic_stat"

    id = Column(BigInteger, primary_key=True)
    topic_id = Column(BigInteger)
    e_count = Column(Integer, default=0)
    i_count = Column(Integer, default=0)
    s_count = Column(Integer, default=0)
    n_count = Column(Integer, default=0)
    f_count = Column(Integer, default=0)
    t_count = Column(Integer, default=0)
    j_count = Column(Integer, default=0)
    p_count = Column(Integer, default=0)
    average_talk_time = Column(BigInteger, default=0)
    select_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    teen_count = Column(Integer, default=0)
    twenties_count = Column(Integer, default=0)
    thirties_count = Column(Integer, default=0)
    forties_count = Column(Integer, default=0)
    fifties_count = Column(Integer, default=0)
    male_count = Column(Integer, default=0)
    female_count = Column(Integer, default=0)
    version = Column(Version) 