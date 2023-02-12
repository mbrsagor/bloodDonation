from fastapi import FastAPI
from .routes import users

app = FastAPI()

app.include_router(users.router)

"""
uMQ8tYSpgDi30A7e
"""