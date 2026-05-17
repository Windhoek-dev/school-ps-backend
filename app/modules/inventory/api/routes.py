from fastapi import APIRouter, status

from app.core.db import SessionDep
from app.modules.inventory.application.create_borrowing_inventory import (
    CreateItemBorrowing,
)
from app.modules.inventory.application.create_item_inventory import CreateItemInventory
from app.modules.inventory.application.create_type_inventory import CreateTypeInventory
from app.modules.inventory.application.get_items_inventory import GetItemsInventory
from app.modules.inventory.application.update_item_inventory import UpdateItemInventory
from app.modules.inventory.schemas.request import (
    CreateBorrowRequest,
    CreateItemRequest,
    CreateTypeInventoryRequest,
    UpdateItemRequest,
)
from app.shared.utils.response import Response

router = APIRouter()


@router.get("/items")
async def get_inventory(session: SessionDep):
    inventory_app = GetItemsInventory(session=session)
    data = await inventory_app.execute()

    return Response(
        data=data,
        message="Inventario obtenido exitosamente",
        status_code=status.HTTP_200_OK,
        details={"message": "Inventario obtenido exitosamente"},
    )


@router.post("/items")
async def create_item(session: SessionDep, create_item_request: CreateItemRequest):
    create_item_app = CreateItemInventory(session=session)
    data = await create_item_app.execute(create_item_request)

    return Response(
        data=data,
        message="Articulo creado exitosamente",
        status_code=status.HTTP_201_CREATED,
        details={"message": "Articulo creado exitosamente"},
    )


@router.post("/types")
async def create_type_inventory(
    session: SessionDep, create_type_request: CreateTypeInventoryRequest
):
    create_type_app = CreateTypeInventory(session=session)
    data = await create_type_app.execute(create_type_request)

    return Response(
        data=data,
        message="Tipo de inventario creado exitosamente",
        status_code=status.HTTP_201_CREATED,
        details={"message": "Tipo de inventario creado exitosamente"},
    )


@router.put("/items/{item_id}")
async def update_item(
    session: SessionDep, item_id: int, update_item_request: UpdateItemRequest
):
    update_item_app = UpdateItemInventory(session=session)
    data = await update_item_app.execute(item_id, update_item_request)

    return Response(
        data=data,
        message="Articulo actualizado exitosamente",
        status_code=status.HTTP_200_OK,
        details={"message": "Articulo actualizado exitosamente"},
    )


@router.post("/borrow")
async def create_borrowing(session: SessionDep, borrow_data: CreateBorrowRequest):
    create_borrow_app = CreateItemBorrowing(session=session)

    data = await create_borrow_app.execute(borrow_data)

    return Response(
        data=data,
        message="Prestamo creado exitosamente",
        status_code=status.HTTP_201_CREATED,
        details={"message": "Prestamo creado exitosamente"},
    )
