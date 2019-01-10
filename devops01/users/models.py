from django.db import models

class UserInfo(models.Model):
    ###定义用户权限级别
    user_type_choices = (
        (1,'普通用户'),
        (2, 'VIP用户'),
        (3, 'SVIP用户'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=128,unique=True)
    group = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo')
    token = models.CharField(max_length=64)
