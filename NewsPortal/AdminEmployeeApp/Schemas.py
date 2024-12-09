from ninja import ModelSchema
from .models import *




class ProductSchema(ModelSchema):
    class Config:
        model = AdminEmployeeCredentials  # Specify the model
        model_fields = '__all__'



