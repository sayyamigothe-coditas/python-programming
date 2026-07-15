from argon2 import hash_password
from sqlalchemy.orm import Session
from models import User
from schema import UserCreate

def create_user(db: Session, user: UserCreate):

    # Convert plain password into hashed password
    hashed_password = hash_password(user.password)

    # Create SQLAlchemy User object
    new_user = User(
        name=user.name, email=user.email, password=hashed_password, role="USER"
    )

    # Save to database
    db.add(new_user)

    # Commit transaction
    db.commit()

    # Refresh object to get generated fields like id
    db.refresh(new_user)

    return new_user


