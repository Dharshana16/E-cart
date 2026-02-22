from database import Base



from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    INTEGER,
    Text,
    Numeric
)
class Category(Base):
    __tablename__ = 'categories'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    def _repr_(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


