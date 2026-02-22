from database import Base
from schemas.order import Order
from sqlalchemy import (
    String,
    Column,
    Integer,
    ForeignKey,
    Numeric,
    DateTime,
    DATE,
    )
from datetime import datetime
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey(Order.id))  # Foreign key to orders table
    payment_mode = Column(String(50))
    amount = Column(Numeric(10, 2))
    payment_date = Column(DateTime, default=datetime.utcnow())  # Default to current timestamp

    def _repr_(self):
        return f"<Payment(id={self.id}, order_id={self.order_id}, amount={self.amount})>"