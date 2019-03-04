from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    """
    用户序列化类
    """
    id       = serializers.IntegerField()
    username = serializers.CharField(label="用户名",help_text="用户名")
    email    = serializers.EmailField(label="邮箱",help_text="邮箱")
    date_joined = serializers.DateTimeField(label="创建时间",help_text="创建时间")
