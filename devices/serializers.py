from rest_framework import serializers
from devices.models import Device

class DeviceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name','dev_id']

class DevicEditeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('name','dev_id')