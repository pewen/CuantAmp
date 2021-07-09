import tweepy
import pandas as pd
from sqlalchemy.orm import Session

from config import settings
from db.base import fill_model
from db.session import SessionLocal
from tusers import models
from tusers.controller import crud as tusers_crud


auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

db: Session = SessionLocal()
df: pd.DataFrame = pd.read_csv("data/politicxs.csv")

tseeds = []
for i, row in df[:20].iterrows():
    print(f"\rGetting data of user {i}/{len(df)}", end="")
    try:
        user = api.get_user(row.user_id)._json
        user["user_id"] = user["id"]
        tusers_crud.create(db=db, obj_in=user)
        tseeds.append(row.to_dict())
        db.commit()
    except tweepy.error.TweepError:
        continue

objs = [fill_model(tseed, models.TwitterUserSeed)
        for tseed in tseeds]
db.add_all(objs)
db.commit()

db.close()
