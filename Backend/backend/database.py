from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/mysqlDB"

engine = create_engine(DATABASE_URL)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session