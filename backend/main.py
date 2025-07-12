from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Base

app = FastAPI()

engine = create_engine("postgresql://food_order_user:food_order_pass@db:5432/food_order_db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@app.post("/restaurants/")
def create_restaurant(name: str, address: str):
    db = SessionLocal()
    restaurant = Restaurant(name=name, address=address)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant