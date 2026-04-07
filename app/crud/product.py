from sqlalchemy.orm import Session

from app.models import product as models
from app.schemas import product as schemas


def get_products(db: Session):
    return db.query(models.Product).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
