from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas import product as schemas
from app.crud import product as crud

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.post("/")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)
