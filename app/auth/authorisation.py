
from functools import wraps
from app.db import get_db
from app.models.models import User
from fastapi import HTTPException
import jwt

db = get_db()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# RBAC - Role Based Authorisation
def authorise(allowed_roles):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            token = kwargs['token']
            
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            
            user_role = payload.get("role")
            
            if user_role not in allowed_roles:
                raise HTTPException(status_code=403, detail="Unauthorised user")
            
            return original_function(*args, **kwargs)
        
        return wrapper_function

    return decorator_function
        
            