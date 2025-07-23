from fastapi import APIRouter, Depends, HTTPException
import jwt
from sqlalchemy.orm import Session
from jose import JWTError
from passlib.context import CryptContext
from app import schemas, database, crud



router = APIRouter()

pwd_context = CryptContext(schemes="bcrypt", deprecated = "auto")



SECRET_KEY ="secret_key"
ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
  return jwt.encode(data, SECRET_KEY, algorithm= ALGORITHM)


@router.post("/login")
def login(credintials:schemas.LoginReqest, db:Session = Depends(database.get_db)):
  user = crud.get_user_by_email(db, credintials.email)
  if not user or not verify_password(credintials.password, user.hashed_password):
    raise HTTPException(status_code=401, detail="Неверный email или пароль")
  
  token =  create_access_token({"sub": str(user.id)})
  return {"access_token": token, "token_type": "bearer", "user": {"id": user.id, "email":user.email, "name": user.name}}


  



