"""empty message

Revision ID: e97c27c2ede2
Revises: 
Create Date: 2024-07-24 21:54:43.399698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e97c27c2ede2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('int_id', sa.String(length=16), nullable=False),
    sa.Column('str', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('pk', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('pk')
    )
    op.create_index('log_address_idx', 'log', ['address'], unique=False, postgresql_using='HASH')
    op.create_table('message',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('int_id', sa.String(length=16), nullable=False),
    sa.Column('str', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('pk', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('pk')
    )
    op.create_index(op.f('ix_message_created'), 'message', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_created'), table_name='message')
    op.drop_table('message')
    op.drop_index('log_address_idx', table_name='log', postgresql_using='HASH')
    op.drop_table('log')
    # ### end Alembic commands ###
