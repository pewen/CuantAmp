from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql

from db import BaseModel
from users.models import TwitterUser


class Tweet(BaseModel):
    __tablename__ = "tweets"

    id: int = Column(Integer, primary_key=True, index=True, unique=True)
    text: str = Column(String, nullable=False)
    source: str = Column(String, nullable=False)
    truncated: bool = Column(Boolean, nullable=False)
    coordinates: dict = Column(postgresql.JSON)
    place: dict = Column(postgresql.JSON)
    entities: dict = Column(postgresql.JSON)
    extended_entities: dict = Column(postgresql.JSON)
    lang: str = Column(String)
    in_reply_to_status_id: int = Column(Integer) # FIXME: debería tener una FK
    in_reply_to_user_id: int = Column(Integer) # FIXME: debería tener una FK

    user_id: int = Column(
        Integer, ForeignKey("twitter_users.id"), nullable=False
    )
    user: TwitterUser = relationship("User")

    quoted_status_id: int = Column(Integer, ForeignKey("tweets.id"))
    quoted_status = relationship("Tweet")

    retweeted_status_id: int = Column(Integer, ForeignKey("tweets.id"))
    retweeted_status = relationship("Tweet")

    quote_count: int = Column(Integer)
    reply_count: int = Column(Integer)
    retweet_count: int = Column(Integer, nullable=False)
    favorite_count: int = Column(Integer)


class TweetMetrics(BaseModel):
    __tablename__ = "tweets_metrics"

    time: datetime = Column(DateTime, primary_key=True, index=True)
    tweet_id = Column(Integer, nullable=False, index=True)

    quote_count: int = Column(Integer)
    reply_count: int = Column(Integer)
    retweet_count: int = Column(Integer, nullable=False)
    favorite_count: int = Column(Integer)