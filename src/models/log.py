from sqlalchemy import Boolean, Column, DateTime, String, Index

from models.base import BaseModel

class Log(BaseModel):
    __tablename__ = 'log'

    created = Column(DateTime, nullable=False)
    int_id = Column(String(16), nullable=True)
    str = Column(String)
    address = Column(String)

    __table_args__ = (
        Index('log_address_idx', 'address', postgresql_using='HASH'),
    )
