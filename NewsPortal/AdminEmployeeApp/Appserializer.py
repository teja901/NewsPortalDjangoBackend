from rest_framework import serializers
from .models import *


class AdminEmployeSerializer(serializers.ModelSerializer):

    class Meta:
        model=AdminEmployeeCredentials
        fields='__all__'


