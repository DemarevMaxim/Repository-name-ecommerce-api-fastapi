from sqlalchemy.orm import Session

from app.models import order as models
from app.schemas import order as schemas


def get_orders(db: Session):
    return db.query(models.Order).all()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order
