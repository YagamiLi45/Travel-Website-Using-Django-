#Using Django Model fields from their official Website 

from django.db import models

# Create your models here.
class Destination(models.Model):
    # id : int Automatically Generate in db
    name = models.CharField(max_length=100) # type: ignore
    img = models.ImageField(upload_to='pics') # type: ignore
    desc = models.TextField() # type: ignore
    price = models.IntegerField()
    offer = models.BooleanField(default=False)