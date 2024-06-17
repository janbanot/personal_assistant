from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.database.models.personal_memory import PersonalMemory


class PersonalMemorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonalMemory
        fields = (
            "id",
            "name",
            "description",
            "source",
            "category",
            "tags",
            "created_at",
            "updated_at",
            "active",
        )
