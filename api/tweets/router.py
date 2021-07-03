from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from tweets import schemas
from tweets.controller import crud


router = APIRouter()


@router.post("/", response_model=schemas.Tweet)
def create_tweet(
    tweet: schemas.TweetCreate,
    db: Session = Depends(get_db),
):
    return crud.create_tweet(db=db, tweet=tweet)

@router.put("/{tweet_id}", response_model=schemas.Tweet)
def update_tweet(
    tweet_id: int,
    tweet: schemas.TweetUpdate,
    db: Session = Depends(get_db),
):
    db_tweet = crud.get(db=db, id=tweet_id)
    if not db_tweet:
        raise HTTPException(status_code=404, detail="tuser not found")
    return crud.update(db=db, db_obj=db_tweet, obj_in=tweet)

@router.get("/{tweet_id}", response_model=schemas.Tweet)
def get_tweet(
    tweet_id: int,
    db: Session = Depends(get_db),
):
    return crud.get(db=db, id=tweet_id)

@router.get("/{tweet_id}/metrics", response_model=List[schemas.TweetMetrics])
def get_tweet_metrics(
    tweet_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_metrics(db=db, by={"tweet_id": tweet_id})

@router.get("/by_user/{user_id}", response_model=List[schemas.Tweet])
def get_tweets_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_tweets_by_user(
        db=db, user_id=user_id, skip=skip, limit=limit
    )
