from datetime import datetime, timedelta
from jose import jwt

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    # copy the payload because we don't want to modify the original data
    to_encode = data.copy()

    # Suppose:
    # Current time  10:00
    # Expiry 10:30
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    #add the expiry time to the payload
    to_encode.update({"exp": expire})

    # encode the payload with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
