from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.database.models.resources import Resource


class ResourceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        fields = (
            "id",
            "name",
            "content",
            "url",
            "tags",
            "category",
            "active",
            "created_at",
            "updated_at",
        )
