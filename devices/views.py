import random

from background_task import background
# Create your views here.
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from devices.models import Device
from devices.serializers import DevicEditeSerializers, DeviceSerializers
import datetime

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'devices': reverse('device-list', request=request, format=format),
        'login': reverse('login', request=request, format=format),

    })

class Devices(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed, edited, delete and create.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializers
    permission_classes = (IsAuthenticated,)

class SendUpdate(APIView):
    """
        API to send data to specific device with specific sensor id inteegrated with that device.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        device_id = request.POST.get('dev_id')
        sens_id = request.POST.get('sensor_id')
        try:
            if Device.objects.get(dev_id=device_id).sensors_set.filter(sensor_id=sens_id).exists():
                return Response({
                        'Device': device_id,
                        'sensor': sens_id,
                        'data': random.randint(10, 100),
                    })
            else:
                return Response({
                        'Device': device_id,
                        'sensor': sens_id,
                        'data': 'Device with sensor id does not exists.',
                    })
        except Exception as e:
            return Response({
                'Device': device_id,
                'sensor': sens_id,
                'data': 'Device or sensor does not exists.',
            })


class GetData(APIView):
    """ 
        API to get data of specific device with specific sensor id inteegrated with that device on specific interval with is value.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        device_id = request.POST.get('dev_id')
        sens_id = request.POST.get('sensor_id')
        time = request.POST.get('time',60)

        endtime = datetime.datetime.now()+ datetime.timedelta(hours=1)

        try:
            if Device.objects.get(dev_id=device_id).sensors_set.filter(sensor_id=sens_id).exists():
                get_data(device_id,sens_id,time,repeat=time, repeat_until=endtime)
                return Response({
                        'Device': device_id,
                        'sensor': sens_id,
                        'data': f'Get requests placed for Device {device_id} of sensor {sens_id} with {time}.',
                    })
            else:
                return Response({
                        'Device': device_id,
                        'sensor': sens_id,
                        'data': 'Device with sensor id does not exists.',
                    })
        except Exception as e:
            return Response({
                'Device': device_id,
                'sensor': sens_id,
                'data': 'Device or sensor does not exists.',
            })
        

@background(schedule=60)
def get_data(device_id,sens_id,sec):

    print(f'recevied {random.randint(10, 100)} from Device {device_id} of sensor {sens_id} with {sec}.')
