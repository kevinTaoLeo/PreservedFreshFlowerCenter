from django.shortcuts import render
from rest_framework import viewsets
from .models import Cabinet
from .serializers import CabinetSerializer

class CabinetViewset(viewsets.ModelViewSet):
    """
     retrieve:
        返回指定项目信息
    list：
        返回项目列表
    update:
        更新项目信息
    destroy:
        删除项目记录
    create:
        创建项目记录
    partial_update:
        更新部分字段
    """

    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer

# Create your views here.
