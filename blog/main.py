from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    desc: str


@app.post("/blog")
async def create(data: Blog):
    return data
