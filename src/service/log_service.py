from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.sql.expression import func

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

    async def get_form_result(self, address):

        query = select(
            self.message_model.created,
            self.message_model.str,
            self.message_model.int_id
        ).union_all(
            select(
                self.log_model.created,
                self.log_model.str,
                self.log_model.int_id
            ).where(self.log_model.address == address)
        ).order_by('int_id', 'created')

        query_alias = query.alias()

        count_query = select(func.count()).select_from(query_alias)
        count_result = await self.session.execute(count_query)
        query_size = count_result.scalar()

        if query_size > 100:
            query = query.limit(100)

        # Execute the main query
        result = await self.session.execute(query)
        return result.all(), query_size


@lru_cache()
def get_log_service(
    session: AsyncSession = Depends(get_session)
) -> LogService:
    return LogService(
        session
    )
