from fastapi import FastAPI

from app.database.database import Base, engine

from app.routers import user
from app.routers import product
from app.routers import category
from app.routers import cart
from app.routers import order


app = FastAPI(title="E-commerce API")


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "E-commerce API is running"}


app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(cart.router)
app.include_router(order.router)
