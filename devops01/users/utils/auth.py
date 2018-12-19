
from rest_framework import exceptions
from users import models
from django.http import  JsonResponse



class FirstAuthtication(object):
    def authenticate(self,request):
        pass
    def authenticate_header(self,request):
        pass

class Authtication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        ret = {'code': 1000, 'msg': None}
        if not token_obj:
            ret['code'] = 1003
            ret['msg'] = "用户未认证"
            raise exceptions.AuthenticationFailed(ret)
        ## 在rest framework内部将这两个字段赋值给request，以供后续操作使用
        return (token_obj.user,token_obj)
    def authenticate_header(self,request):
        pass
