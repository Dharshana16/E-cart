from database import Base,engine

from schemas.product import Product
from schemas.cart_detail import CartDetail
from schemas.category import Category
from schemas.customer import Customer
from schemas.order import Order
from schemas.order_detail import OrderDetail
from schemas.payment import Payment

Base.metadata.create_all(engine)