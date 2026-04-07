from sqlalchemy.orm import Session

from app.models import cart as models
from app.schemas import cart as schemas


def get_cart(db: Session):
    return db.query(models.Cart).all()


def add_to_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(
        user_id=cart.user_id,
        product_id=cart.product_id,
        quantity=cart.quantity
    )

    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)

    return db_cart
