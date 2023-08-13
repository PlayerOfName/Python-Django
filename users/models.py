from django.db import models
from django.contrib.auth.models import User
from users.static.img import *
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defoult.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Comments(models.Model):

    nickname = models.CharField('Имя пользователя', max_length=50)
    text = models.TextField('Текст комментария')

    def __str__(self):
        return self.nickname
    