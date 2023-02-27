from fastapi import FastAPI
from . import schemas, models
from .database import engine

from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
async def create(data: schemas.Blog, db: Session):
    return db

"""
https://www.youtube.com/watch?v=7t2alSnE2-I&list=PLe30vg_FG4OSKH_8zpLlnf4WpNlzL526E&ab_channel=Bitfumes
"""