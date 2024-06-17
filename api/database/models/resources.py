from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from api.extensions import db
import sqlalchemy as sa


class Resource(db.Model):  # type: ignore
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    url = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    category = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False, server_default="true")
    created_at = Column(DateTime, nullable=False, server_default=sa.func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()
    )
