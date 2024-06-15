"""add functions_history table

Revision ID: 0f632f48bc6d
Revises: e62d40842589
Create Date: 2024-06-15 13:14:00.332058

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0f632f48bc6d"
down_revision: Union[str, None] = "e62d40842589"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "functions_history",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("interaction_id", sa.Integer, nullable=False),
        sa.Column("function", sa.String(255), nullable=False),
        sa.Column("user_input", sa.Text, nullable=False),
        sa.Column("answer", sa.Text, nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
    )


def downgrade() -> None:
    op.drop_table("functions_history")
