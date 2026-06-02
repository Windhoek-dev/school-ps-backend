from app.core.db import SessionDep
from app.modules.inventory.application.update_item_inventory import UpdateItemInventory
from app.modules.sports.domain.service import SportsService
from app.modules.sports.schemas.request import UpdateItemDeportes

class UpdateItemDeportes(UpdateItemInventory):
    def __init__(self, session: SessionDep):
        super().__init__(session=session)
        self.service = SportsService(repository=self.repository)

    async def _execute(self, item_id: int, item_data: UpdateItemDeportes):
        return await self._service.update_item(item_id=item_id, item_data=item_data)  