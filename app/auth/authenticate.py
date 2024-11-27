

import datetime
import jwt
# Secret key and configurations
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




class Authenticate:
    
    def authenticate_user(self, username, password):
        if username == "admin" and password == "admin":
            user_id = 1
            return user_id
        else:
            return False
    
    def generate_jwt(self, user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Token expires in 1 hour
            "iat": datetime.datetime.utcnow()  # Issued at
        }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        
        return token
    
    def decode_jwt(self, token):
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        
        return payload