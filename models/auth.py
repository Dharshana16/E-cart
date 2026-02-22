from pydantic import BaseModel
from typing import List
from typing import List

class Login(BaseModel):
    name:str
    password:str
    
class Register(BaseModel):
    name:str
    email:str
    password:str