import pandas as pd
from sqlalchemy.orm import Session

try:
    from database import SessionLocal
    from data_models import Products
except:
    from .database import SessionLocal
    from .data_models import Products


def get_products(db: Session):
    return db.query(Products).all()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
