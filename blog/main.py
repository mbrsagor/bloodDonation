from fastapi import FastAPI
from . import schemas, models
from .database import engine

from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
async def create(data: schemas.Blog, db: Session):
    return db
