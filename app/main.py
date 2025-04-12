from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.engine import create_db_and_tables
from fastapi.responses import JSONResponse
from app.routers import categories, expenses, incomes

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:5173",
    "http://127.0..0.1:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.on_event("shutdown")
def on_shutdown():
    pass   

app.include_router(categories.router, tags=["categories"])
app.include_router(expenses.router, tags=["expenses"])
app.include_router(incomes.router, tags=["incomes"])

@app.get("/health", tags=["health"])
async def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)