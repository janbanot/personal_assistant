from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from api.extensions import db
import sqlalchemy as sa


class KnowledgeBase(db.Model):  # type: ignore
    __tablename__ = "knowledge_base"
    id = Column(Integer, primary_key=True)
    category = Column(String(255), nullable=False)
    tag = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=sa.func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()
    )
    last_accessed_at = Column(DateTime, nullable=True)
    active = Column(Boolean, nullable=False, server_default="true")
