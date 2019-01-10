class SVIPPermission(object):
    message = {'code':1004,'msg':"权限不足"}
    def has_permission(self,request,view):
        if request.user.user_type != 3:
            return False
        return True


