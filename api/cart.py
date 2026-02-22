from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from crud.auth import getUserById
from sqlalchemy.exc import DatabaseError
from crud.cart import addProductToCart,removeProductFromCart,viewCart,checkout,orders,getOrderById

router = APIRouter()

auth_scheme = HTTPBearer()

@router.post("/cart/{productId}",status_code=200)  # Correct the route by replacing ':' with '{ }'
def addToCart(productId: int, userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        try:
            return "Added successfully" if  addProductToCart(productId,userId) else "Unexpected Error"
        except DatabaseError:
            raise HTTPException(409,detail=DatabaseError)
        


@router.delete("/cart/{productId}")  # Correct the route by replacing ':' with '{ }'
def deleteToCart(productId: int, userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        return "Removed successfully" if  removeProductFromCart(productId,userId) else "Unexpected Error"

@router.get("/view/")
def viewToCart(userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        return viewCart(userId)


@router.post('/checkout')
def order(userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        checkout(userId)


@router.get("/orders")
def getOrders(userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        return orders(userId)


@router.get("/orders/{orderId}")
def getOrder(orderId:str,userId:int):  # Use str directly for token
    if(not (not getUserById(userId))):
        return getOrderById(userId,orderId)
