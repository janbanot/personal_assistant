"""create users table

Revision ID: 264699802ec3
Create Date: 2024-03-03 18:25:23.656599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '264699802ec3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('login', sa.String(64), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(128), nullable=False)
    )


def downgrade():
    op.drop_table('users')
