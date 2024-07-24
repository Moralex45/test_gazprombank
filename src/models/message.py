from sqlalchemy import Boolean, Column, DateTime, String, Index

from models.base import BaseModel


class Message(BaseModel):
    __tablename__ = "message"

    id = Column(String, nullable=True)
    int_id = Column(String(16), nullable=False)
    str = Column(String, nullable=False)
    created = Column(DateTime, nullable=False, index=True)
    status = Column(Boolean, default=False)
