"""add chat_history table

Revision ID: e3fab275bece
Revises: 7fbcdb262a79
Create Date: 2024-05-13 07:16:11.484875

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e3fab275bece"
down_revision: Union[str, None] = "7fbcdb262a79"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "chat_history",
        sa.Column("message_id", sa.Integer, primary_key=True),
        sa.Column("conversation_id", sa.Integer),
        sa.Column("user_message", sa.String),
        sa.Column("current_context", sa.String),
        sa.Column("answer", sa.String),
    )


def downgrade():
    op.drop_table("chat_history")
