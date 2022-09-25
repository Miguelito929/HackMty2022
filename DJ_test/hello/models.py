from django.db import models

# Create your models here.
class Event(models.Model):
    category = models.CharField(max_length=30)
    # TODO: Changee to geopoint column
    # location = models.PointField(srid=4326,dim=2)
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30)