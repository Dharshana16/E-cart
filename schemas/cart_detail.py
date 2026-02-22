from database import Base
from schemas.customer import Customer
from schemas.product import Product
from sqlalchemy import (
    String,
    PrimaryKeyConstraint,
    Column,
    INTEGER,
    ARRAY,
    DATE,
    ForeignKey
    )
class CartDetail(Base):
    __tablename__ = 'cart_details'

    id = Column(INTEGER,autoincrement=True,primary_key=True)
    customer_id = Column(INTEGER, ForeignKey(Customer.id))  # Foreign key to customers table
    product_id = Column(INTEGER, ForeignKey(Product.id))  # Foreign key to products table
    def _repr_(self):
        return f"<CartDetail(id={self.id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity})>"
