from app.modules.inventory.domain.repositories import InventoryRepository
from app.modules.inventory.schemas.request import (
    CreateBorrowRequest,
    CreateItemRequest,
    CreateTypeInventoryRequest,
    UpdateItemRequest,
)


class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    async def get_inventory(self):
        return await self.repository.get_inventory()

    async def create_item(self, item_data: CreateItemRequest):
        return await self.repository.create_item(item_data)

    async def create_type_inventory(self, type_data: CreateTypeInventoryRequest):
        return await self.repository.create_type_inventory(name=type_data.nombre)

    async def update_item(self, item_id: int, item_data: UpdateItemRequest):
        item = await self.repository.get_item_by_id(item_id)
        if not item:
            return None

        return await self.repository.update_item(item=item, item_data=item_data)

    async def create_borrow(self, borrow_data: CreateBorrowRequest):
        item = await self.repository.get_item_by_id(borrow_data.inventario_id)
        if not item:
            return None

        if borrow_data.cantidad > item.cantidad:
            return None

        return await self.repository.create_borrow(borrow_data)
