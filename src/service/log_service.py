from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from connections.postgres import get_session
from models.log import Log
from models.message import Message

class LogService():

    def __init__(
        self,
        session: AsyncSession
    ):
        self.session: AsyncSession = session
        self.message_model = Message
        self.log_model = Log

    async def create_message(self, data) -> None:
        result = self.message_model(**data)

        self.session.add(result)
        await self.session.commit()
        await self.session.refresh(result)

    async def create_log(self, data) -> None:
        result = self.log_model(**data)

        self.session.add(result)
        await self.session.commit()
        await self.session.refresh(result)

    

@lru_cache()
def get_log_service(
    session: AsyncSession = Depends(get_session)
) -> LogService:
    return LogService(
        session
    )
