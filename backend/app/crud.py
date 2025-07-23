from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate


def get_user(db: Session, user_id: int):
  return db.query(User).filter(User.id == user_id).first()

def get_users(db:Session):
  return db.query(User).all()

def get_user_by_email(db:Session, email:str):
  return db.query(User).filter(User.email == email).first()


def delete_user(db: Session, user_id: int):
  db_user = db.query(User).filter(User.id == user_id).first()
  if db_user:
    db.delete(db_user)
    db.commit()
  return None


def create_user(db:Session, user: UserCreate):
  hashed_password = user.password
  db_user = User(email=user.email, hashed_password=hashed_password, name = user.name)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user