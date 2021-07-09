from typing import List
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql

from db import BaseModel


class TwitterUser(BaseModel):
    __tablename__ = "twitter_users"

    id: int = Column(BigInteger, primary_key=True, index=True, unique=True)
    created_at: datetime = Column(DateTime(timezone=True), nullable=False)
    name: str = Column(String, nullable=False)
    screen_name: str = Column(String, nullable=False)
    location: str = Column(String)
    url: str = Column(String)
    description: str = Column(String)
    protected: bool = Column(Boolean, nullable=False)
    verified: bool = Column(Boolean, nullable=False)
    lang: str = Column(String)
    profile_banner_url: str = Column(String)
    profile_background_color: str = Column(String)
    profile_background_image_url_https: str = Column(String)
    profile_image_url_https: str = Column(String)
    default_profile: bool = Column(Boolean, nullable=False)
    default_profile_image: bool = Column(Boolean, nullable=False)
    withheld_in_countries: List[str] = Column(
        postgresql.ARRAY(String, dimensions=1)
    )

    followers_count: int = Column(Integer, nullable=False)
    friends_count: int = Column(Integer, nullable=False)
    listed_count: int = Column(Integer, nullable=False)
    favourites_count: int = Column(Integer, nullable=False)
    statuses_count: int = Column(Integer, nullable=False)


class TwitterUserMetrics(BaseModel):
    __tablename__ = "twitter_users_metrics"

    id: int = Column(
        BigInteger,
        ForeignKey("twitter_users.id"),
        primary_key=True,
        index=True,
    )
    time: datetime = Column(
        DateTime(timezone=True),
        default=func.now(),
        primary_key=True,
        index=True
    )

    followers_count: int = Column(Integer, nullable=False)
    friends_count: int = Column(Integer, nullable=False)
    listed_count: int = Column(Integer, nullable=False)
    favourites_count: int = Column(Integer, nullable=False)
    statuses_count: int = Column(Integer, nullable=False)


class TwitterUserSeed(BaseModel):
    __tablename__ = "twitter_users_seed"

    id: int = Column(
        Integer, primary_key=True, index=True, unique=True
    )
    name: str = Column(String, nullable=False)
    gender: str = Column(String, nullable=False)
    category: str = Column(String, nullable=False)
    country: str = Column(String, nullable=False)
    user_id: int = Column(
        BigInteger,
        ForeignKey("twitter_users.id"),
        index=True,
        unique=True,
    )
    user: TwitterUser = relationship("TwitterUser")
