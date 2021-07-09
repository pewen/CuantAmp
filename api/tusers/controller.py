from typing import List

from sqlalchemy.orm import Session

from db import BaseCRUD
from tusers import models, schemas


def get_seed_users(db: Session) -> List[schemas.TUserSeed]:
    return db.query(models.TwitterUserSeed).all()


crud = BaseCRUD[
    models.TwitterUser, models.TwitterUserMetrics, schemas.TUserCreate, schemas.TUserUpdate
](models.TwitterUser, models.TwitterUserMetrics)
