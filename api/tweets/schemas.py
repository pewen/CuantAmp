from typing import Optional
from datetime import datetime

from pydantic import validator
from dateutil.parser import parse

from db import BaseSchema
from tusers.schemas import TUser


class TweetBase(BaseSchema):
    id: int
    created_at: datetime
    text: str
    source: str
    truncated: bool
    coordinates: Optional[dict]
    place: Optional[dict]
    entities: Optional[dict]
    extended_entities: Optional[dict]
    lang: Optional[str]
    in_reply_to_status_id: Optional[int]
    in_reply_to_user_id: Optional[int]
    user_id: int
    user: TUser
    quoted_status_id: Optional[int]
    quoted_status: Optional["TweetBase"] = None
    retweeted_status_id: Optional[int]
    retweeted_status: Optional["TweetBase"] = None
    quote_count: Optional[int]
    reply_count: Optional[int]
    retweet_count: int
    favorite_count: int

    @validator("created_at", pre=True)
    def parse_date(cls, v):
        if isinstance(v, str):
            return parse(v)
        return v

class TweetCreate(TweetBase):
    pass


class TweetUpdate(TweetBase):
    pass


class Tweet(TweetBase):
    pass


class TweetMetrics(BaseSchema):
    time: datetime
    tweet_id: int
    quote_count: int
    reply_count: int
    retweet_count: int
    favorite_count: int


TweetBase.update_forward_refs()
TweetCreate.update_forward_refs()
TweetUpdate.update_forward_refs()
Tweet.update_forward_refs()
