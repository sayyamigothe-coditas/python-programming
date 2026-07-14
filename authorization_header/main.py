from fastapi import APIRouter, Depends, FastAPI

from dependencies import get_current_user

app = FastAPI()
router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return current_user


app.include_router(router)
