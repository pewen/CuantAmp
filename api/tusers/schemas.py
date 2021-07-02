from typing import List, Optional
from datetime import datetime

from db import BaseSchema


class TUserBase(BaseSchema):
    id: int
    user_id: Optional[int]
    name: str
    screen_name: str
    location: str = ""
    url: str = ""
    description: str = ""
    protected: bool
    verified: bool
    created_at: datetime
    profile_banner_url: str
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool
    withheld_in_countries: List[str] = []
    withheld_scope: str = ""
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int


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
