from database import Base

from sqlalchemy import (
    String,
    Column,
    Integer
    )

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def _repr_(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"

