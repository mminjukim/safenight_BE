from rest_framework.routers import SimpleRouter 
from django.urls import path, include
from .views import ConsultLogViewSet


consultlog_router = SimpleRouter(trailing_slash=False)
consultlog_router.register('consultLog', ConsultLogViewSet, basename='consultLog') 


urlpatterns = [
    path('', include(consultlog_router.urls)),
]