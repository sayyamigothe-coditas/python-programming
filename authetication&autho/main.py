from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, FastAPI
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from auth import create_access_token
from database import engine
from database import Base


from crud import create_user, get_user_by_email
from dependencies import get_db
from schemas import UserCreate, UserLogin  

Base.metadata.create_all(bind=engine)

ph = PasswordHasher()

app = FastAPI()

router = APIRouter()

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

    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

app.include_router(router)