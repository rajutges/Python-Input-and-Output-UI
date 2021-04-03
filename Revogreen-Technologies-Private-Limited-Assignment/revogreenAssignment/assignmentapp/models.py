from django.db import models

# Create your models here.
class Inputdata(models.Model):
    textdata = models.TextField()
    slider = models.TextField(default=0)
