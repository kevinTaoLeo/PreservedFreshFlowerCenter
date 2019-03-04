from rest_framework import serializers
from .models import Idc

class IdcSerializer(serializers.Serializer):
    """
    Idc 序列化类
    """

    id          = serializers.IntegerField(read_only=True)
    name        = serializers.CharField(required=True, max_length=32,label="云名称",help_text="云名称",error_messages={"blank":"傻缺这儿没写","required":"这个字段为必要字段"})
    address     = serializers.CharField(required=True, max_length=256,label="地址",help_text="地址",error_messages={"blank":"傻缺这儿没写","required":"这个字段为必要字段"})
    phone       = serializers.CharField(required=True, max_length=15,label="联系电话",help_text="联系电话",error_messages={"blank":"傻缺这儿没写","required":"这个字段为必要字段"})
    email       = serializers.EmailField(required=True,label="邮箱地址",help_text="邮箱地址",error_messages={"blank":"傻缺这儿没写","required":"这个字段为必要字段"})
    letter      = serializers.CharField(required=True, max_length=5,label="简称",help_text="简称",error_messages={"blank":"傻缺这儿没写","required":"这个字段为必要字段"})

 ##validated_data存储的是序列化以后干净的数据
    def create(self, validated_data):
        return Idc.objects.create(**validated_data)
##传入ID，为修改，不存入ID为更新，instance为当前对象（ID）
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance