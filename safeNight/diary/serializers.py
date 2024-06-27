from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Diary 
from django.conf import settings


class DiarySerializer(ModelSerializer):
    date = serializers.DateField(format="%Y.%m.%d %a")
    class Meta:
        model = Diary
        fields = ['diaryId', 'date', 'content']