from fastapi import FastAPI
from src.system import system

app = FastAPI()
app.include_router(system.router)
