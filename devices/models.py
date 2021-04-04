from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Device(models.Model):
    """
        To store all devices.
    """
    name = models.CharField(max_length=60, blank=True, null=True)
    dev_id = models.CharField(max_length=10, blank=True ,null=True)

    def __str__(self):
        return self.name

class Sensors(models.Model):
    """
        To Store senosrs for each device.
    """
    sensor_name = models.CharField(max_length=60, blank=True, null=True)
    sensor_id = models.CharField(max_length=10, blank=True,null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.sensor_name

class Readings(models.Model):
    """
        To Store each senosrs value along with timestamp.
    """
    sensor_id = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    value = models.CharField(max_length=10,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sensor_id.sensor_name


@receiver(post_save, sender=Device)
def add_sensors(sender, created, instance, **kwargs):
    """
        To add defined sensors of each devices as the are added in device model.
    """
    if created:
        Sensors.objects.bulk_create([
            Sensors(sensor_name="pressure",sensor_id=f'pres{instance.id}',device=instance),
            Sensors(sensor_name="temp",sensor_id=f'temp{instance.id}',device=instance)
            ])