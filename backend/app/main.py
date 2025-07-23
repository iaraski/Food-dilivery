from fastapi import FastAPI
from app.api import users,auth
from app.database import engine
from app.models import Base
from app import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/", summary="пока пусто",)
def read_root():
    return {"message": "Welcome to Food Order App"}

app.include_router(users.router, prefix="/api")
app.include_router(auth.router, prefix="/api" )

