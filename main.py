import models
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
from typing import Optional, List

from database import SessionLocal


class Item(BaseModel):  # Serializer
    id: int
    name: str
    description: str
    price: int
    is_available: bool

    class Config:
        orm_mode = True


db = SessionLocal()

app = FastAPI()


@app.get('/api/items', response_model=List[Item], status_code=status.HTTP_200_OK)
def get_items():
    items = db.query(models.Item).all()
    return items


@app.get('/api/item/{item_id}/', response_model=Item, status_code=status.HTTP_200_OK)
def item_details(item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


@app.post('/api/create-item', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    old_item = db.query(models.Item).filter(models.Item.name == item.name).first()
    if old_item is not None:
        resp = {
            "status": False,
            "message": "The item is already exists"
        }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resp)

    new_item = models.Item(
        name=item.name,
        price=item.price,
        is_available=item.is_available,
        description=item.description,
    )

    db.add(new_item)
    db.commit()
    return new_item


@app.put('/api/update-item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    get_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    get_item.name = item.name
    get_item.price = item.price
    get_item.is_available = item.is_available
    get_item.description = item.description
    db.commit()
    return get_item


@app.delete('/api/delete-item/{item_id}')
def delete_item(item_id: int):
    pass
