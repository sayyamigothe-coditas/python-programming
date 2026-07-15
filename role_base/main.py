from fastapi import APIRouter, Depends, FastAPI

from crud import create_user
from dependencies import get_db, require_role
from schema import UserCreate, UserResponse
from sqlalchemy.orm import Session

app = FastAPI()


router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.delete("/delete/{id}")
def delete_user(id:int,current_user=Depends(require_role('ADMIN'))):
    return { "message":"user deleted"}

app.include_router(router)
