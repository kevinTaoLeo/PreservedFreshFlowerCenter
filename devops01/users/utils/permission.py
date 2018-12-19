class SVIPPermission(object):
    message = "必须是管理员才能访问"
    def has_permission(self,request,view):
        if request.user.user_type != 3:
            return False
        return True


