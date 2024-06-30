from backend.schemas.User import Message, UserList, UserPublic, UserSchema, UserValid
from backend.database import get_session
from backend.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from http import HTTPStatus
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from decouple import config
from fastapi.security import OAuth2PasswordRequestForm
from backend.use_case.case_user import UserUseCases
from backend.depends import token_verifier

router = APIRouter(prefix='/users')
router_teste = APIRouter(prefix='/teste', dependencies=[Depends(token_verifier)])

crypt_context = CryptContext(schemes=['sha256_crypt'])


SECRET_KEY = "9a4a5717996f3284fbd1d627a5eb2c6a7e4240b938a3559bbf99ff0a9027409c"
ALGORITHM = "HS256"

@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db_user.username = user.username
    db_user.password = user.password
    db_user.email = user.email
    session.commit()
    session.refresh(db_user)

    return db_user


@router.delete('/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):

    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}




@router.post('/login')
def login(login_request_form: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_session)):
    user = UserValid(
        username=login_request_form.username,
        password=login_request_form.password
    )

    uc = UserUseCases

    token_data = uc.user_login(db_session, user=user, expires_in=60)

    return token_data


@router_teste.get('/')
def test_user_verify():
    return 'It works'

