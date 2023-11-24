from pydantic import BaseModel, constr
# from typing import List, Dict, Union, Optional


class UserBase(BaseModel):
  first_name: str
  last_name: str
  email: str
  username:str
  password: str
  
  
class LoginBase(BaseModel):
    username:str
    password:str  
