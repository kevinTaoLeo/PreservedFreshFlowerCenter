from django.db import models
from idcs.models import Idc
# Create your models here.

class Cabinet(models.Model):
    idc = models.ForeignKey(Idc,on_delete=models.CASCADE,verbose_name="项目所在平台")
    ##django1和2版本有on_delete参数的区别，在1版本默认如此，不用加
    name = models.CharField(max_length=255,verbose_name="项目名称")
    ips = models.CharField(max_length=255,verbose_name="项目所在IP段",null=True)
    leader = models.CharField(max_length=255,verbose_name="项目负责人",null=True)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'resources_cabinet'
        ordering = ["id"]
