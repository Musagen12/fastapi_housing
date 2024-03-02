from fastapi import FastAPI
from .routers import customers, status
from .config import settings
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customers.router)
app.include_router(status.router)