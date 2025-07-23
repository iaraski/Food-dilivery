from sqlalchemy import Column, Boolean,  Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

favorite_products = Table(
    "favorite_products", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key= True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True)
)
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True)
    name = Column(String)
    email = Column(String, unique= True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    Favorites = relationship("Product", secondary = favorite_products, back_populates = "favorites_by")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key= True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    favorites_by = relationship("User", secondary = favorite_products, back_populates = "Favorites")

    
