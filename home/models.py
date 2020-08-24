from django.db import models
import pendulum
# Create your models here.
from django.utils import dateparse


class Patient(models.Model):
	def __str__(self):
		return self.name

	id = models.AutoField(primary_key=True)  # System generated Unique ID
	name = models.CharField(max_length=256, null=True)
	age = models.IntegerField(null=True)
	sex = models.CharField(max_length=9, choices=[(1, 'Male'), (2, 'Female')], null=True)
	email = models.CharField(max_length=1024, null=True)
