from database import Base
from schemas.customer import Customer
from sqlalchemy import (
    String,
    Column,
    Integer,
    ForeignKey,
    DateTime,
    )
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey(Customer.id))  # Foreign key to customers table
    order_date = Column(DateTime, default=datetime.utcnow())  # Default to current timestamp

    def _repr_(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, order_date='{self.order_date}')>"

