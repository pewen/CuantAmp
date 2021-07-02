from typing import List, Optional
from datetime import datetime

from db import BaseSchema
from tusers.schemas import TUser


class TweetBase(BaseSchema):
    id: int
    text: str
    source: str
    truncated: bool
    coordinates: dict
    place: dict
    entities: dict
    extended_entities: dict
    lang: str
    in_reply_to_status_id: int
    in_reply_to_user_id: int
    user_id: int
    user: TUser
    quoted_status_id: int
    # quoted_status
    retweeted_status_id: int
    # retweeted_status
    quote_count: int
    reply_count: int
    retweet_count: int
    favorite_count: int


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
