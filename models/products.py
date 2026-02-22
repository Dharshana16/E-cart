from pydantic import BaseModel
from typing import List, Optional

class Products(BaseModel):
    id:int
    name:str
    price:str
    description:str
    image:str
    category:Optional[str]
