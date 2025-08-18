from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(f"{products_url}/", json=product_data())

    assert response.status_code == status.HTTP_201_CREATED

    content = response.json()
    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}/{product_inserted.id}")
    content = response.json()
    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    from uuid import uuid4

    non_existent_id = uuid4()
    response = await client.get(f"{products_url}/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
