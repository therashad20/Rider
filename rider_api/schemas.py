from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form

class User(BaseModel):
    full_name: str 
    email: str 
    phone_no: str
    user_type: int 
    password: Optional[str] =  None
    vehicle: str 
    is_active: Optional[bool] =  None
    is_block: Optional[bool] = None
    class Config():
        from_attributes=True   

    
class ShowUser(User):
    id: int
    uuid: str
    avater:Optional[str] =  None
    class Config():
        from_attributes=True



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str]  = None
