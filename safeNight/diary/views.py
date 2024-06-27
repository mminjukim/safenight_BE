from .models import Diary
from .serializers import DiarySerializer
from rest_framework.viewsets import ModelViewSet

class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer