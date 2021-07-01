from typing import List
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
)
from sqlalchemy.dialects import postgresql

from db import BaseModel


class TwitterUser(BaseModel):
    __tablename__ = "twitter_users"

    id: int = Column(Integer, primary_key=True, index=True, unique=True)
    name: str = Column(String, nullable=False)
    screen_name: str = Column(String, nullable=False)
    location: str = Column(String)
    url: str = Column(String)
    description: str = Column(String)
    protected: bool = Column(Boolean, nullable=False)
    verified: bool = Column(Boolean, nullable=False)
    created_at: datetime = Column(DateTime, nullable=False)
    profile_banner_url: str = Column(String, nullable=False)
    profile_image_url_https: str = Column(String, nullable=False)
    default_profile: bool = Column(Boolean, nullable=False)
    default_profile_image: bool = Column(Boolean, nullable=False)
    withheld_in_countries: List[str] = Column(postgresql.ARRAY(String, dimensions=1))
    withheld_scope: str = Column(String)

    followers_count: int = Column(Boolean, nullable=False)
    friends_count: int = Column(Boolean, nullable=False)
    listed_count: int = Column(Boolean, nullable=False)
    favourites_count: int = Column(Boolean, nullable=False)
    statuses_count: int = Column(Boolean, nullable=False)


class TwitterUserMetrics(BaseModel):
    __tablename__ = "twitter_users_metrics"

    time: datetime = Column(DateTime, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)

    followers_count: int = Column(Boolean, nullable=False)
    friends_count: int = Column(Boolean, nullable=False)
    listed_count: int = Column(Boolean, nullable=False)
    favourites_count: int = Column(Boolean, nullable=False)
    statuses_count: int = Column(Boolean, nullable=False)
