from models import User


def create_user(db, name, email, password):

    user = User(name=name, email=email, password=password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db, email):

    return db.query(User).filter(User.email == email).first()
