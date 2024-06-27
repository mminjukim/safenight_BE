from django.db import models
from datetime import date

class ConsultLog(models.Model):
    memoryId = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name="작성일", default=date.today)
    doctor = models.CharField(verbose_name="상담사", max_length=30)
    content = models.TextField(verbose_name="내용", default='상담 기록이 없습니다')
    
    def __str__(self):
        return self.content