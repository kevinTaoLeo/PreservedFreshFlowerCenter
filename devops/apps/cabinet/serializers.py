from rest_framework import serializers
from .models import Cabinet
from idcs.serializers import IdcSerializer
from idcs.models import Idc


class CabinetSerializer(serializers.Serializer):
    ##此处idc为多对一,关联\
    id = serializers.IntegerField(read_only=True)
    idc = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all(),allow_empty=False)
    name = serializers.CharField(required=True,max_length=255,label="项目名称",help_text="项目名称")
    ips = serializers.CharField(required=True,max_length=255,label="项目IP范围",help_text="项目IP范围")
    leader = serializers.CharField(required=True,max_length=255,label="项目负责人",help_text="项目负责人")

    def to_representation(self, instance):
        idc_obj = instance.idc
        ret = super(CabinetSerializer,self).to_representation(instance)
        ret["idc"] = {
            "idcid": idc_obj.id,
            "name": idc_obj.name
        }
        return ret

    def to_internal_value(self,data):
        return super(CabinetSerializer,self).to_internal_value(data)

    def create(self, validated_data):
        return Cabinet.objects.create(**validated_data)


    # def create(self,validated_data):
    #     return Idc.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.address = validated_data.get("address", instance.address)
    #     instance.phone = validated_data.get("phone", instance.phone)
    #     instance.email = validated_data.get("email", instance.email)
    #     instance.save()
    #     return instance