from pydantic import BaseModel, EmailStr
from datetime import datetime

class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]


class TokenData(BaseModel):
    access_token: str
    expires_at: datetime

class UserValid(BaseModel):
    username: str
    password: str