from datetime import datetime
from typing import List, Optional

from pydantic import validator
from dateutil.parser import parse

from db import BaseSchema


class TUserBase(BaseSchema):
    id: int
    user_id: Optional[int]
    name: str
    screen_name: str
    location: str = None
    url: str = None
    description: str = ""
    protected: bool
    verified: bool
    created_at: datetime
    profile_banner_url: str = None
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool
    withheld_in_countries: List[str] = []
    withheld_scope: str = None
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int

    @validator("user_id", always=True)
    def set_user_id(cls, value, values):
        return values["id"]

    @validator("created_at", pre=True)
    def parse_date(cls, v):
        if isinstance(v, str):
            return parse(v)
        return v


class TUserCreate(TUserBase):
    pass


class TUserUpdate(TUserBase):
    pass


class TUser(TUserBase):
    pass


class TUserMetrics(BaseSchema):
    time: datetime
    user_id: int
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int


class TUserSeed(BaseSchema):
    id: int
    name: str
    gender: str
    category: str
    country: str
    user_id: int
    user: TUser
