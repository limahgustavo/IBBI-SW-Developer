from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from http import HTTPStatus
from fastapi import status
from backend.schemas.User import Message, UserList, UserPublic, UserSchema, UserValid
from backend.models import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from backend.database import get_session



crypt_context = CryptContext(schemes=['sha256_crypt'])

SECRET_KEY = "9a4a5717996f3284fbd1d627a5eb2c6a7e4240b938a3559bbf99ff0a9027409c"
ALGORITHM = "HS256"

class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def user_login(db_session: Session, user: UserValid, expires_in: int = 30):
        user_on_db = db_session.query(User).filter_by(username=user.username).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=401,
                detail='Invalid username or password'
            )
        
        # Aqui você deve verificar a senha de forma segura
        if user.password != user_on_db.password:
            raise HTTPException(
                status_code=401,
                detail='Invalid username or password'
            )
        
        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub': user.username,
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }

    def verify_token(self, token: str):
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=HTTPStatus.HTTP_401_UNAUTHORIZED, detail='Invalid token')
        
        user_on_db = self._get_user(username=data['sub'])

        if user_on_db is None:
            raise HTTPException(status_code=HTTPStatus.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    def _get_user(self, username: str):
        user_on_db = self.db_session.query(User).filter_by(username=username).first()
        return user_on_db