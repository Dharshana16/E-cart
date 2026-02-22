from database import Base

from schemas.product import Product
from schemas.order import Order

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    INTEGER,
    Numeric
)
class OrderDetail(Base):
    __tablename__ = 'order_details'

    order_id = Column(INTEGER, ForeignKey(Order.id), primary_key=True)  # Composite primary key
    product_id = Column(INTEGER, ForeignKey(Product.id), primary_key=True)  # Composite primary key
    quantity = Column(INTEGER,default=1)

    def _repr_(self):
        return f"<OrderDetail(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"

