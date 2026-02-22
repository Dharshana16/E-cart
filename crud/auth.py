from database import SessionClass
from schemas.customer import Customer
from models.auth import Register
from sqlalchemy import insert
import jwt
sql1 = SessionClass()
sql = sql1.get_session()

def checkUser(email:str)->bool:
    return not(not(sql.query(Customer).filter(Customer.email==email).first()))

def insertUser(data:Register):
    obj = Customer(
        name=data.name,
        email= data.email,
        password=data.password
    )
    print(obj)
    sql.add(obj)
    sql.commit()

def getUser(name:str):
    return sql.query(Customer).filter(Customer.name==name).first()

def getUserById(id:int):
    return sql.query(Customer).filter(Customer.id==id).first()

