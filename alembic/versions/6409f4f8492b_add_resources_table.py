"""add resources table

Revision ID: 6409f4f8492b
Revises: 265ab9e632ed
Create Date: 2024-06-15 13:17:26.673095

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6409f4f8492b"
down_revision: Union[str, None] = "265ab9e632ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "resources",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("content", sa.Text, nullable=True),
        sa.Column("url", sa.String(255), nullable=True),
        sa.Column("tags", sa.String(255), nullable=True),
        sa.Column("category", sa.String(255), nullable=False),
        sa.Column("active", sa.Boolean, nullable=False, server_default="true"),
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
    )


def downgrade() -> None:
    op.drop_table("resources")
