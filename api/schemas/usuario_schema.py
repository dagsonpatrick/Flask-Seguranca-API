from api import ma
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ("id", "nome", "email", "senha", "is_admin", "api_key")

    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    is_admin = fields.Boolean(required=True)
    api_key = fields.String(required=False)