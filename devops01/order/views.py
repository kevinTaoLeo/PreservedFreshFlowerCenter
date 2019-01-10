from django.shortcuts import render
from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import exceptions
from users import models
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import render
from django.http import HttpResponse
from order import models
# Create your views here.
class OrderView(APIView):
    """用于资产清单"""
    #authentication_classes = [FirstAuthtication,Authtication]
    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':"请求成功",'data':None}
        try:
            ret['data'] =ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)