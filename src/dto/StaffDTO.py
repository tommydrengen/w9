from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class StaffDTO(Base):
    __tablename__ = 'staffs'

    staff_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)