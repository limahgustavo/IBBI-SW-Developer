Executar o backend localmente e isolado: fastapi dev main.py --host localhost --port 80

adicionar o alembic no poetry: poetry add alembic   

acessar o shell do poetry: poetry shell
iniciar o migration: alembic init migrations
cria um migration: alembic revision --autogenerate -m "create users table"
executar o migration: alembic upgrade head
