from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    # name: str
    # quantity: int
    # price: float
    # status: bool
    # created_at: datetime
    # updated_at: datetime
    ...
