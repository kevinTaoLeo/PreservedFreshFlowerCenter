from django.db import models

class OrderInfo(models.Model):
    '''资产表'''
    ip = models.CharField(max_length=32,unique=True)
    hostname = models.CharField(max_length=64)
    num_cpu = models.CharField(max_length=32)
    cpu = models.CharField(max_length=32)
    num_memory = models.CharField(max_length=32)
    memory = models.CharField(max_length=64)
    sysversion = models.CharField(max_length=32)

    def __str__(self):
        return self.hip

    class Meta:
        verbose_name = "资产表"
        verbose_name_plural = verbose_name