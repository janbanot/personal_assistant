"""add personal_memory table

Revision ID: 265ab9e632ed
Revises: 0f632f48bc6d
Create Date: 2024-06-15 13:15:35.943222

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "265ab9e632ed"
down_revision: Union[str, None] = "0f632f48bc6d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "personal_memory",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("source", sa.String(255), nullable=True),
        sa.Column("category", sa.String(255), nullable=False),
        sa.Column("tags", sa.String(255), nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.Column("active", sa.Boolean, nullable=False, server_default="true"),
    )


def downgrade() -> None:
    op.drop_table("personal_memory")
