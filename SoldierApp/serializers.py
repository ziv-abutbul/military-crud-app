from rest_framework import serializers
from SoldierApp.models import Soldier

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soldier
        fields = '__all__'