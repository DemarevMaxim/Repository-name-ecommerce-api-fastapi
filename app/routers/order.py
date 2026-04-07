from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas import order as schemas
from app.crud import order as crud

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@router.post("/")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order(db, order)
