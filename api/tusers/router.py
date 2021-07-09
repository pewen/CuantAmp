from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from tusers import schemas
from tusers.controller import crud, get_seed_users
from tweets import schemas as tweets_schemas
from tweets.controller import crud as tweets_crud


router = APIRouter()


@router.post("/", response_model=schemas.TUser)
def create_tuser(
    user: schemas.TUserCreate,
    db: Session = Depends(get_db),
):
    # user.user_id = user.id # FIXME: The schema must do this
    return crud.create(db=db, obj_in=user)

@router.put("/{user_id}", response_model=schemas.TUser)
def update_tuser(
    user_id: int,
    user: schemas.TUserUpdate,
    db: Session = Depends(get_db),
):
    # user.user_id = user.id # FIXME: The schema must do this
    db_user = crud.get(db=db, id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="tuser not found")
    return crud.update(db=db, db_obj=db_user, obj_in=user)

@router.get("/{user_id}", response_model=schemas.TUser)
def get_tuser(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.get(db=db, id=user_id)

@router.get("/{user_id}/metrics", response_model=List[schemas.TUserMetrics])
def get_tuser_metrics(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_metrics(db=db, id=user_id)

@router.get("/{user_id}/tweets", response_model=List[tweets_schemas.Tweet])
def get_tusers_tweets(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return tweets_crud.get_tweets_by_user(
        db=db, user_id=user_id, skip=skip, limit=limit
    )

@router.get("/seed/", response_model=List[schemas.TUserSeed])
def root(db: Session = Depends(get_db)):
    return get_seed_users(db=db)
