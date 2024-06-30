from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.database import get_session
from backend.use_case.case_user import UserUseCases


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')



def token_verifier(
    db_session: Session = Depends(get_session),
    token = Depends(oauth_scheme)
):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(token=token)