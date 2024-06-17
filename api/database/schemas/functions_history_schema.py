from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.database.models.functions_history import FunctionsHistory


class FunctionsHistorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FunctionsHistory
        fields = (
            "id",
            "interaction_id",
            "function",
            "user_input",
            "answer",
            "created_at",
        )
