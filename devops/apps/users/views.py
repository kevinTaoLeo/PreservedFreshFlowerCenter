from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.

user = get_user_model()

"""
get:
    list
    get
create
update
delete
"""

class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet继承只读类
    retrieve:
        返回指定用户信息
    list：
        返回用户列表
    """
    queryset = user.objects.all()
    serializer_class = UserSerializer
