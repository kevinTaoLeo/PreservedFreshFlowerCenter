from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import exceptions
from users import models
from rest_framework.authentication import BasicAuthentication

# Create your views here.

ORDER_DICT = {
    1:{
        'ip':"1.1.1.1",
        'hostname':"hezefan01",
        'memory':'8G',
        'content':'hahahahha'
    },
    2:{
        'ip': "2.2.2.2",
        'hostname': "hezefan02",
        'memory': '128G',
        'content': 'hehehheeheeheh'
    }
}

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()


class AuthView(APIView):
    """用于用户登录认证
    code1000：认证成功
    code1001：用户名或密码错误
    code1002请求异常"""
    authentication_classes = []   ##登录不需要认证
    permission_classes =  []      ##无权限控制
    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':"认证成功"}
        try:
            #user = request._request.POST.get('username')
            user = request._request.POST.get('username')
            #print(user)
            pwd = request._request.POST.get('password')
            #print(pwd)
            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            print(obj)
            if obj == None:
                ret['code'] = 1001
                ret['msg'] = "用户名或者密码错误"
                return JsonResponse(ret)
            ###为登录用户创建token
            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = "请求异常"
        return JsonResponse(ret)

# class FirstAuthtication(object):
#     def authenticate(self,request):
#         pass
#     def authenticate_header(self,request):
#         pass
#
# class Authtication(object):
#     def authenticate(self,request):
#         token = request._request.GET.get('token')
#         token_obj = models.UserToken.objects.filter(token=token).first()
#         if not token_obj:
#             raise exceptions.AuthenticationFailed('用户未认证')
#         ## 在rest framework内部将这两个字段赋值给request，以供后续操作使用
#         return (token_obj.user,token_obj)
#     def authenticate_header(self,request):
#         pass

class OrderView(APIView):
    """用于资产清单"""
    #authentication_classes = [FirstAuthtication,Authtication]
    def get(self,request,*args,**kwargs):
        #self.dispatch()
        #request.user
        #request.auth
        ret = {'code':1000,'msg':"请求成功",'data':None}
        try:
            ret['data'] =ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)

