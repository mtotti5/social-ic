from django.db import models

# Create your models here.
class Location(models.Model):
	name = models.CharField(max_length=20)
	parent = models.ForeignKey('self', null=True, blank=True)
	coordX = models.CharField(max_length=20)
	coordY = models.CharField(max_length=20)
