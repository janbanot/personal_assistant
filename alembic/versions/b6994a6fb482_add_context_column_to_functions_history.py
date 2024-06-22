"""add context column to functions history

Revision ID: b6994a6fb482
Revises: 6409f4f8492b
Create Date: 2024-06-22 09:34:02.802263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6994a6fb482'
down_revision: Union[str, None] = '6409f4f8492b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('functions_history', sa.Column('context', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('functions_history', 'context')
