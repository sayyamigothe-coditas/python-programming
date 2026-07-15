from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, Depends, FastAPI, HTTPException

from auth import create_access_token
from crud import create_user, get_user_by_email
from dependencies import get_current_user, get_db
from schemas import UserCreate, UserLogin
from sqlalchemy.orm import Session

app = FastAPI()
router = APIRouter()
ph = PasswordHasher()


@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = ph.hash(user.password)

    new_user = create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=hashed_password,
    )

    return {"message": "Registered"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    try:
        ph.verify(db_user.password, user.password)
    except VerifyMismatchError:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user.id), "email": db_user.email})

    return {"access_token": token, "token_type": "bearer"}


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return current_user


app.include_router(router)
