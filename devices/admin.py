from django.contrib import admin

# Register your models here.
from devices.models import Device, Sensors, Readings



class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'dev_id')

admin.site.register(Device, DeviceAdmin)


class SensorsAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_id')

admin.site.register(Sensors, SensorsAdmin)

class ReadingsAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'timestamp')

admin.site.register(Readings, ReadingsAdmin)