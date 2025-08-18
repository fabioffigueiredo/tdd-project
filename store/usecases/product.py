from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exception import NotFoundException, InsertionException
import pymongo
from datetime import datetime


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        try:
            product_model = ProductModel(**body.model_dump())
            await self.collection.insert_one(product_model.model_dump())
            return ProductOut(**product_model.model_dump())
        except Exception as e:
            raise InsertionException(message=f"Error inserting product: {str(e)}")

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})
        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(
        self, min_price: float = None, max_price: float = None
    ) -> list[ProductOut]:
        filter_query = {}

        if min_price is not None or max_price is not None:
            price_filter = {}
            if min_price is not None:
                price_filter["$gte"] = min_price
            if max_price is not None:
                price_filter["$lte"] = max_price
            filter_query["price"] = price_filter

        return [ProductOut(**item) async for item in self.collection.find(filter_query)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        # Verificar se o produto existe primeiro
        existing_product = await self.collection.find_one({"id": id})
        if not existing_product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        # Preparar dados para atualização, incluindo updated_at
        update_data = body.model_dump(exclude_unset=True)
        if "updated_at" not in update_data:
            update_data["updated_at"] = datetime.utcnow()

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})
        return True if result.deleted_count > 0 else False


product_usecase = ProductUseCase()
