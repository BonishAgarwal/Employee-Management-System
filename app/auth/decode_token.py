from fastapi import APIRouter, Depends, HTTPException
from app.auth.authenticate import Authenticate
from fastapi.security import OAuth2PasswordBearer
from functools import wraps
import jwt

router = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def authenticate(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        try:
            token = kwargs.get("token")

            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            
            # Optionally, you can pass the payload to the route
            kwargs['user'] = payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        return original_function(*args, **kwargs)

    return wrapper_function