from fastapi import FastAPI, APIRouter

from users import  router as users


app = FastAPI()
router = APIRouter()

router.include_router(users.router, prefix="/user", tags=["users"])

app.include_router(router, prefix="/api")
