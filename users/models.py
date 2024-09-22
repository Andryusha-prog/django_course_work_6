from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email_user')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия пользователя')

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email