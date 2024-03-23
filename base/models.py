from django.db import models

# Create your models here.
class EventManage(models.Model):
    event_name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return self.event_name