from django.db import models

# Create your models here.
class Idc(models.Model):
    name = models.CharField("机房名称",max_length=32)
    address = models.CharField("机房地址",max_length=256)
    phone = models.CharField("联系人",max_length=15)
    email = models.EmailField("邮件地址",default="null")
    letter = models.CharField("IDC简称",max_length=5)

    def _str_(self):
        return self.name
    ##当print的时候在终端输出

    class Meta:
        db_table = 'resources_idc'