from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from config import ALGORITHM, SECRET_KEY
from database import SessionLocal
from schema import get_user_by_id


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: int = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid Token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_id(db, user_id)

    if user is None:

        raise HTTPException(status_code=401, detail="User not found")

    return user


def require_role(role: str):

    def role_checker(current_user=Depends(get_current_user)):
        # we are passing because sometimes we need "ADMIN" ,"USER"
        if current_user.role != role:
            raise HTTPException(status_code=403, detail="Access Denied")

        return current_user

    return role_checker
