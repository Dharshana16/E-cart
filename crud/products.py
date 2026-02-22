from database import SessionClass
from schemas.product import Product
from models.products import Products
from schemas.category import Category
from sqlalchemy import insert
sql1 = SessionClass()
sql = sql1.get_session()


def getProducts():
    data = sql.query(Product,Category).join(Category,Category.id==Product.category_id).all()
    obj = list()
    for i in data:
        obj.append(Products(name=i.Product.name,
                            price=i.Product.price,
                            description=i.Product.description,
                            image=i.Product.image,
                            category=i.Category.name))
    return obj
