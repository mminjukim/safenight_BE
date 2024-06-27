from django.db import models
from django.conf import settings

class Diary(models.Model):
    diaryId = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name="내용", default='')
    date = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):
        return self.content