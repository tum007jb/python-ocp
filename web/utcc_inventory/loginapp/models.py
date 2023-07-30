from django.db import models

# Create your models here.
class Inventory(models.Model):
    id_invent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    series_number = models.IntegerField
