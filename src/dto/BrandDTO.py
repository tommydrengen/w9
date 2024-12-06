from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BrandDTO(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(String)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
