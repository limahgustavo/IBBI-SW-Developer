fastapi dev main.py --host localhost --port 80

poetry add alembic     
poetry shell
alembic init migrations
cria um migration
alembic revision --autogenerate -m "create users table"
aplica o migration
alembic upgrade head
