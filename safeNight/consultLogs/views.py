from .models import ConsultLogs
from .serializers import ConsultLogsSerializer
from rest_framework.viewsets import ModelViewSet 

class ConsultLogsViewSet(ModelViewSet):
    queryset = ConsultLogs.objects.all()
    serializer_class = ConsultLogsSerializer

    def perform_create(self, serializer):
        serializer.save(doctor = self.request.user)