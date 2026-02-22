from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from fastapi import HTTPException
from crud.products import getProducts
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.get('/products')
def getProduct(): 
    return getProducts()

