from fastapi import APIRouter, Depends
from app.schemas.models import UserLogin
from sqlalchemy.orm import Session
from app.db import get_db
from fastapi.security import OAuth2PasswordBearer
from app.auth.authenticate import Authenticate
from app.models.models import User


router = APIRouter()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth = Authenticate(db)
    
    result = auth.authenticate_user(user.email, user.password)

    if result:
        token = auth.generate_jwt(result)
        
        return token

@router.get("/test")
def test(token: str = Depends(oauth2_scheme)):
    print(token)
    auth = Authenticate()
    
    result = auth.decode_jwt(token)
    
    print(result)
    
    return result

@router.post("/register")
def register(user: UserLogin, db: Session = Depends(get_db)):
        user = User(
            username = user.username,
            email = user.email,
            password = user.password,
            role = user.role
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
    
    