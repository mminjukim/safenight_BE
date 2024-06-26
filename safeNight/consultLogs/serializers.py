from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers
from .models import ConsultLogs
from django.contrib.auth.models import User

class ConsultLogsSerializer(ModelSerializer):
    doctor = serializers.ReadOnlyField(source = 'doctor.username')
    date = serializers.DateTimeField(format="%Y.%m.%d %a")

    class Meta:
        model = ConsultLogs
        fields = [ 'memoryId', 'date', 'doctor', 'content' ] 