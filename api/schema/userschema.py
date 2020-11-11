from .schema import ma
from api.models.usermodel import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
    id = ma.auto_field(dump_only=True)
    password = ma.auto_field(load_only=True)
