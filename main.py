import models
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException

from utils import messages
from database import SessionLocal


class Item(BaseModel):
    """
    This is item serializer
    """
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
    """
    Get list of items API
    URL: /api/items/
    Method: GET
    :return:
    """
    items = db.query(models.Item).all()
    return items


@app.get('/api/item/{item_id}/', response_model=Item, status_code=status.HTTP_200_OK)
def item_details(item_id: int):
    """
    Get Item details API
    URL: /api/item/<id>/
    Method: GET
    :return:
    """
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


@app.post('/api/create-item', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """
    Item create API
    URL: /api/items/
    Method: POST
    :return:
    """
    old_item = db.query(models.Item).filter(models.Item.name == item.name).first()
    if old_item is not None:
        resp = {
            "status": False,
            "message": messages.ITEM_EXISTS
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
    resp = {
        "status": True,
        "message": messages.ITEM_CREATED
    }
    return resp


@app.put('/api/update-item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    """
    Item update API
    URL: /api/update-item/<pk>/
    Method: PUT
    :return:
    """
    get_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if get_item is not None:
        get_item.name = item.name
        get_item.price = item.price
        get_item.is_available = item.is_available
        get_item.description = item.description
        db.commit()
        return get_item
    else:
        resp = {
            "status": False,
            "message": messages.NO_ITEM
        }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resp)


@app.delete('/api/delete-item/{item_id}')
def delete_item(item_id: int):
    """
    Item create API
    URL: /api/delete-item/<i>/
    Method: DELETE
    :return:
    """
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        resp = {
            "status": False,
            "message": messages.ITEM_ALREADY_DELETE
        }
        return resp

    db.delete(item)
    db.commit()
    resp = {
        "status": True,
        "message": messages.ITEM_DELETE
    }
    return resp
