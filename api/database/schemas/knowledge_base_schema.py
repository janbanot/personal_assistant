from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.database.models.knowledge_base import KnowledgeBase


class KnowledgeBaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = KnowledgeBase
        fields = (
            "id",
            "category",
            "tag",
            "content",
            "source",
            "created_at",
            "updated_at",
            "last_accessed_at",
            "active",
        )
