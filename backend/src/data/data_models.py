from sqlalchemy import Column, Integer, String

try:
    from database import Base
except:
    from .database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    name = Column(String, index=True)
    quantity = Column(String, index=True)
    price = Column(Integer, index=True)
    image = Column(String, index=True)
    category = Column(String, index=True)


