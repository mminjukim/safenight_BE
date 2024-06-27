from .models import ConsultLog
from .serializers import ConsultLogSerializer
from rest_framework.viewsets import ModelViewSet 

class ConsultLogViewSet(ModelViewSet):
    queryset = ConsultLog.objects.all()
    serializer_class = ConsultLogSerializer