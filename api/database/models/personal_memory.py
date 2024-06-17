from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from api.extensions import db
import sqlalchemy as sa


class PersonalMemory(db.Model):  # type: ignore
    __tablename__ = "personal_memory"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    source = Column(String(255), nullable=True)
    category = Column(String(255), nullable=False)
    tags = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=sa.func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()
    )
    active = Column(Boolean, nullable=False, server_default="true")
