from sqlalchemy import Column, Integer, String, Text, DateTime
from api.extensions import db
import sqlalchemy as sa


class FunctionsHistory(db.Model):  # type: ignore
    __tablename__ = "functions_history"
    id = Column(Integer, primary_key=True)
    interaction_id = Column(Integer, nullable=False)
    function = Column(String(255), nullable=False)
    user_input = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=sa.func.now())
    context = Column(Text, nullable=True)
