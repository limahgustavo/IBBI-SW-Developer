

from fastapi import FastAPI
from backend.routes.User_router import router as User_router, router_teste
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens, ajuste conforme sua necessidade
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Headers permitidos
)

@app.get('/health-check')
def health_check():
    return True


app.include_router(User_router)
app.include_router(router_teste)


