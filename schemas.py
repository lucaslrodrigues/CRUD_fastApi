from typing import List, Union
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    id: Optional[int]
    name: str
    login: str
    senha: str


class UserCreate(BaseModel):
    id: Optional[int]
    name: str
    login: str
    senha: str

class UserUpdate(UserBase):
    pass

class User(BaseModel):
    id: Optional[int]
    name: Optional[str]
    login: Optional[str]
    senha: Optional[str]
    
    class Config:
        orm_mode = True