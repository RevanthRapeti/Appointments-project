from rest_framework import serializers
from .models import Appointment


class doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
