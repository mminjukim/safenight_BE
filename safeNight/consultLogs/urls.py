from rest_framework.routers import SimpleRouter 
from django.urls import path, include
from .views import ConsultLogsViewSet


consultlogs_router = SimpleRouter(trailing_slash=False)
consultlogs_router.register('consultLogs', ConsultLogsViewSet, basename='consultLog') 


urlpatterns = [
    path('', include(consultlogs_router.urls)),
]