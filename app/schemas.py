from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


#  Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# User schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Users(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Vote schemas
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


# post schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: Users
    class Config:
        orm_mode = True

class PostOuts(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

