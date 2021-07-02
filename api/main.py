from fastapi import FastAPI, APIRouter

from tusers import router as tusers
from tweets import router as tweets

app = FastAPI()
router = APIRouter()

router.include_router(
  tusers.router, prefix="/tusers", tags=["tusers"]
)
router.include_router(
  tweets.router, prefix="/tweets", tags=["tweets"]
)

app.include_router(router, prefix="/api")
