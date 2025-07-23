from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import schemas, database, crud


router = APIRouter()

@router.post("/users",response_model=schemas.User)
def create_user(user:schemas.UserCreate, db: Session = Depends(database.get_db)):
  return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id, db:Session = Depends(database.get_db)):
  db_user = crud.get_user(db=db, user_id=user_id)
  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")
  return db_user   

@router.get("/users", response_model=list[schemas.User])  
def get_users(db:Session = Depends(database.get_db)):
      db_users = crud.get_users(db=db)
      return db_users

@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id, db:Session = Depends(database.get_db)):
   db_user = crud.delete_user(db=db, user_id=user_id)
   if not db_user:
    raise HTTPException(status_code=404, detail="User not found")
   return db_user