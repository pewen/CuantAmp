from sqlalchemy.orm import Session

from db import BaseCRUD
from tweets import models, schemas
from tusers.controller import crud as tusers_crud


class TweetCRUD(BaseCRUD[
    models.Tweet, models.TweetMetrics, schemas.TweetCreate, schemas.TweetUpdate
]):
    def create_tweet(
        self, db: Session, *, tweet: schemas.TweetCreate
    ) -> models.Tweet:
        db_user = tusers_crud.get(db=db, id=tweet.user_id)
        if not db_user:
            tusers_crud.create(db=db, obj_in=tweet.user)
        else:
            tusers_crud.update(db=db, db_obj=db_user, obj_in=tweet.user)

        return self.create(db=db, obj_in=tweet)

    def get_tweets_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ):
        return (
            db.query(self.model)
            .filter(self.model.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .order_by("created_at desc")
            .all()
        )


crud = TweetCRUD(models.Tweet, models.TweetMetrics)
