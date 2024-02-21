from rest_framework import serializers
from postapp.models import Model
class Demoserializer(serializers.ModelSerializer):
    class Meta:
        models= Model
        fields='__all__'
