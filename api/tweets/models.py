from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql

from db import BaseModel
from tusers.models import TwitterUser


class Tweet(BaseModel):
    __tablename__ = "tweets"

    id: int = Column(Integer, primary_key=True, index=True, unique=True)
    created_at: datetime = Column(DateTime, nullable=False)
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
    quoted_status: "Tweet" = relationship("Tweet")

    retweeted_status_id: int = Column(Integer, ForeignKey("tweets.id"))
    retweeted_status: "Tweet" = relationship("Tweet")

    quote_count: int = Column(Integer)
    reply_count: int = Column(Integer)
    retweet_count: int = Column(Integer, nullable=False)
    favorite_count: int = Column(Integer)


class TweetMetrics(BaseModel):
    __tablename__ = "tweets_metrics"

    id: int = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    time: datetime = Column(
        DateTime(timezone=True),
        default=func.now(),
        primary_key=True,
        index=True
    )
    tweet_id = Column(
        Integer,
        ForeignKey("tweets.id"),
        nullable=False,
        index=True
    )

    quote_count: int = Column(Integer)
    reply_count: int = Column(Integer)
    retweet_count: int = Column(Integer, nullable=False)
    favorite_count: int = Column(Integer)
