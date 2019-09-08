from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class TrashImageModel(models.Model):
    location = JSONField()
    image = models.TextField()
    trash_density = models.DecimalField(max_digits=16, decimal_places=8)
    google_ml_json = JSONField(default = None, blank = True, null = True)
    time_taken = models.DateField(default=None, blank=True, null=True)
    before_after_cleaning = models.BooleanField(default= True)
    description = models.CharField(max_length=150)


# class AltTrashImageModel(models.Model):
#     image = models.TextField()
#     trash_density = models.DecimalField(max_digits=16, decimal_places=8)
#     google_ml_json = JSONField()
#     time_taken = models.DateField(default=None, blank=True, null=True)
#     before_after_cleaning = models.BooleanField()
#     description = models.CharField(max_length=150)


