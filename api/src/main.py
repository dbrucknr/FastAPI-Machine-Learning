from fastapi import FastAPI
from src.system import system_urls

app = FastAPI()
app.include_router(system_urls.router)
