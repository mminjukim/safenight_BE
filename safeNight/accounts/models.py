from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = ((1, "환자"), (2, "간병인"), (3, "선택하지 않음"))
    role = models.PositiveSmallIntegerField(verbose_name='회원', choices=ROLE_CHOICES, null=True)

    NOTI_CHOICES = ((True, "동의"), (False, "미동의"))
    allow_noti = models.BooleanField(verbose_name='알림 받기', choices=NOTI_CHOICES, null=True)

    name = models.CharField(verbose_name='이름', max_length=30)
    birthdate = models.DateField(verbose_name='생년월일', blank=True, null=True)
    profile_picture = models.ImageField(null=True)

