from database import Base

from schemas.category import Category
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    INTEGER,
    Text,
    Numeric
)
class Product(Base):
    __tablename__ = 'products'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    image = Column(String(255), nullable=False)
    stock = Column(INTEGER,default=300)
    category_id = Column(INTEGER, ForeignKey(Category.id))  # Foreign key to categories table

    def _repr_(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
