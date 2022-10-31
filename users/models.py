from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserData(User):
    username = models.CharField(verbose_name='Имя пользователя', max_length=30)
    surname = models.CharField(verbose_name='Фамилия пользователя', max_length=45)
    lastname = models.CharField(verbose_name='Отчество пользователя', max_length=45)
    picture = models.ImageField(verbose_name='Изображение пользователя', upload_to='users/')
    status = models.BooleanField(verbose_name='Статус пользователя', default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

