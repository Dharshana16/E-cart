from database import SessionClass
from schemas.cart_detail import CartDetail
from schemas.product import Product
from schemas.order import Order
from schemas.order_detail import OrderDetail
from models.products import Products
from models.cart import OrdersModel
from sqlalchemy import insert, and_
from sqlalchemy.exc import IntegrityError, DatabaseError
from fastapi import HTTPException
import uuid
sql1 = SessionClass()
sql = sql1.get_session()


def addProductToCart(prod, usr):
    # Create a CartDetail object
    obj = CartDetail(
        customer_id=usr,
        product_id=prod,
    )
    exist = sql.query(CartDetail).filter(
        and_(CartDetail.customer_id == usr, CartDetail.product_id == prod)
    ).first()
    print(exist)
    if exist is None:
        try:
            sql.add(obj)
            sql.commit()
            return True
        except IntegrityError:
            sql.rollback()
            raise HTTPException(
                status_code=409, detail="Already exists in cart")
        except DatabaseError as e:

            sql.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        except Exception as e:
            sql.rollback()
            raise HTTPException(
                status_code=500, detail="An unexpected error occurred: " + str(e))
    else:
        raise HTTPException(status_code=409, detail="Already exists in cart")


def removeProductFromCart(prod, usr):
    item = sql.query(
        CartDetail).filter(CartDetail.customer_id == usr
                           ).filter(
        CartDetail.product_id == prod).first()
    try:
        sql.delete(item)
        sql.commit()
        return True
    except IntegrityError:
        sql.rollback()
        raise HTTPException(
            status_code=409, detail="Already exists in cart")
    except DatabaseError as e:

        sql.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        sql.rollback()
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e))


def viewCart(usr):
    data = sql.query(CartDetail, Product).join(Product, Product.id == CartDetail.product_id
                                               ).filter(CartDetail.customer_id == usr).all()
    obj = list()
    for i in data:
        obj.append(Products(
            id=i.Product.id,
            name=i.Product.name,
            price=i.Product.price,
            description=i.Product.description,
            image=i.Product.image))
    return obj



def checkout(usr):
    cart = viewCart(usr)
    order = Order(
        id=uuid.uuid4().int & (1 << 12)-1,
        customer_id=usr,
    )
    sql.add(order)
    sql.commit()
    for i in cart:
        removeProductFromCart(i.id,usr)
        temp = OrderDetail(order_id=order.id,product_id=i.id)
        sql.add(temp)
        sql.commit()
    return True


def orders(usr):
    data = sql.query(Order).filter(Order.customer_id==usr).all()
    obj = list()
    for i in data:
        obj.append(OrdersModel(orderId=i.id,date=str(i.order_date)))
    return obj

def getOrderById(usr,odr):
    data = sql.query(OrderDetail,Product).join(Product,Product.id==OrderDetail.product_id).filter(OrderDetail.order_id==odr).all()
    obj = list()
    for i in data:
        obj.append(Products(id=i.Product.id,
                            name=i.Product.name,
                            price=i.Product.price,
                            description=i.Product.description,
                            image=i.Product.image))
    return obj
