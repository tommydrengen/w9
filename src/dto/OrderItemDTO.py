from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class OrderItemDTO(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, primary_key=True)
    item_id = Column(String)
    product_id = Column(String)
    quantity = Column(String)
    list_price = Column(String)
    discount = Column(String)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)