from rest_framework import viewsets
from .models import Idc
from .serializers import IdcSerializer

class IdcViewset(viewsets.ModelViewSet):
    """
     retrieve:
        返回指定idc信息
    list：
        返回idc列表
    update:
        更新idc信息
    destroy:
        删除idc记录
    create:
        创建idc记录
    partial_update:
        更新部分字段
    """

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
