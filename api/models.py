from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


#  extending the django user model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    api_key = models.CharField(max_length=32, blank=True)


# Create your models here.
class MachineDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_id = models.PositiveIntegerField(primary_key=True)
    machine_location = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.machine_id

    class Meta:
        ordering = ["machine_id"]


class SensorValue(models.Model):
    is_power_available = [
        (1, "ON"),
        (0, "OFF"),
    ]
    machine_id = models.ForeignKey(MachineDescription, on_delete=models.CASCADE)
    temperature = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    soil = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    mains = models.PositiveSmallIntegerField(choices=is_power_available, default=1)
    timestamp = models.DateTimeField(default=timezone.now)
