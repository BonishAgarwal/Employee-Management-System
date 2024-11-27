

import datetime
import jwt

from app.models.models import User
# Secret key and configurations
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




class Authenticate:
    def __init__(self, db):
        self.db = db

    def authenticate_user(self, email, password):
        user = self.db.query(User).filter(User.email==email, User.password==password).first()
        
        if user:
            return user
        else:
            return False
    
    def generate_jwt(self, user):
        payload = {
            "user_id": user.id,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Token expires in 1 hour
            "iat": datetime.datetime.utcnow()  # Issued at
        }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        
        return token
    
    def decode_jwt(self, token):
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        
        return payload