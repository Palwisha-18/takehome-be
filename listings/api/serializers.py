from api.models import Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
