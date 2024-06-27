from rest_framework import serializers
from .models import ConsultLog

class ConsultLogSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y.%m.%d %a")
    
    class Meta:
        model = ConsultLog
        fields = [ 'memoryId', 'date', 'doctor', 'content' ] 