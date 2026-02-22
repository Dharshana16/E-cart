from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from fastapi import HTTPException
from models.auth import Login,Register
from crud.auth import checkUser,insertUser,getUser
from schemas.customer import Customer
from fastapi.exceptions import HTTPException
router = APIRouter()
@router.post("/login")
def login(body:Login):
    user = getUser(body.name)
    if(user.password==body.password):
        return HTTPException(200,"Login Successful")
    return HTTPException(404,"Invalid Credentials")

@router.post('/register')
def register(body:Register):
    
    if(not checkUser(body.email)):
        insertUser(body)
        return body
    else:
        return HTTPException(status_code=409,detail="User already exists")
        