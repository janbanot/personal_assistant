"""increase users.password_hash length

Revision ID: 7fbcdb262a79
Revises: 264699802ec3
Create Date: 2024-03-06 00:18:57.968757

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7fbcdb262a79"
down_revision: Union[str, None] = "264699802ec3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        "users", "password_hash", existing_type=sa.String(128), type_=sa.String(256)
    )


def downgrade():
    op.alter_column(
        "users", "password_hash", existing_type=sa.String(256), type_=sa.String(128)
    )
