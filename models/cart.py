from pydantic import BaseModel
from typing import List
class OrdersModel(BaseModel):
    orderId:str
    date:str
