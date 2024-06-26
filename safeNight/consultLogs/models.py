from django.db import models
from django.contrib.auth.models import User

class ConsultLogs(models.Model):
    memoryId = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(verbose_name="내용", default='상담 기록이 없습니다')
    
    def __str__(self):
        return self.content