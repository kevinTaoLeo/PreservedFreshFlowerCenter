from rest_framework import  serializers
from order import models

class OrderSerialzer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip = serializers.CharField(max_length=32,unique=True)
    hostname = serializers.CharField(max_length=64)
    num_cpu = serializers.CharField(max_length=32)
    cpu = serializers.CharField(max_length=32)
    num_memory = serializers.CharField(max_length=32)
    memory = serializers.CharField(max_length=64)
    sysversion = serializers.CharField(max_length=32)
    def create(self, validated_data):
        return models.OrderInfo.objects.create(**validated_data)