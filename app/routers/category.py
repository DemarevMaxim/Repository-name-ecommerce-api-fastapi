from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas import category as schemas
from app.crud import category as crud

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.post("/")
def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_category(db, category)
