from store.schemas.product import ProductIn
from uuid import UUID


def test_schemas_return_success():
    data = {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 8.500,
        "status": True,
    }

    product = ProductIn.model_validate(data)
    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.500}
    ProductIn.model_validate(data)
