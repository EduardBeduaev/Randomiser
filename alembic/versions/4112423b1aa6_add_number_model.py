"""add_number_model

Revision ID: 4112423b1aa6
Revises: 9bf6aae0a573
Create Date: 2025-03-08 16:18:13.440384

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4112423b1aa6'
down_revision: Union[str, None] = '9bf6aae0a573'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_table', sa.Column('number', sa.Integer(), nullable=False))
    op.drop_column('test_table', 'word')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_table', sa.Column('word', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.drop_column('test_table', 'number')
    # ### end Alembic commands ###
