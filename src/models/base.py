import uuid

from connections.postgres import Base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID


class BaseModel(Base):
    __abstract__ = True

    pk = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
