"""add knowledge_base table

Revision ID: e62d40842589
Revises: e3fab275bece
Create Date: 2024-06-15 13:09:52.554254

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e62d40842589"
down_revision: Union[str, None] = "e3fab275bece"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "knowledge_base",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("category", sa.String(255), nullable=False),
        sa.Column("tag", sa.String(255), nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("source", sa.String(255), nullable=True),
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
        sa.Column("last_accessed_at", sa.DateTime, nullable=True),
        sa.Column("active", sa.Boolean, nullable=False, server_default="true"),
    )


def downgrade() -> None:
    op.drop_table("knowledge_base")
