from marshmallow import Schema, fields


class PasswordSchema(Schema):
    user_id = fields.UUID(required=True)
    name = fields.String(required=True)
    password = fields.String(required=True)
    category = fields.UUID(required=True, allow_none=True)


