from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas import cart as schemas
from app.crud import cart as crud

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("/")
def get_cart(db: Session = Depends(get_db)):
    return crud.get_cart(db)


@router.post("/")
def add_to_cart(
    cart: schemas.CartCreate,
    db: Session = Depends(get_db)
):
    return crud.add_to_cart(db, cart)
