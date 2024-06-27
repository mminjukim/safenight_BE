from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import DiaryViewSet


diary_router = SimpleRouter(trailing_slash=False)
diary_router.register('diary', DiaryViewSet, basename='diary')


urlpatterns = [
    path('', include(diary_router.urls)),
]