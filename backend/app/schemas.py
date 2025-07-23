from pydantic import BaseModel

from typing import List, Optional


class UserBase(BaseModel):
  email: str
  name: str
  
  class Config:
    orm_mode = True
  
class UserCreate(UserBase):
  password: str


class Product(BaseModel):
  id:int
  name:str
  description:str
  price: str

class User(UserBase):
  id:int
  favorites:List[Product] = []
  model_config = {'from_attributes': True}

class LoginRequest(BaseModel):
  email: str
  password: str

class Token(BaseModel):
  access_token: str
  token_type:str
  user: Optional[dict] = None




