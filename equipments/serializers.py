from rest_framework import serializers
from . models import equipment

class equipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment
        fields = '__all__'

