from django.db import models
import pendulum
# Create your models here.
from django.utils import dateparse


class Patient(models.Model):
	def __str__(self):
		return self.Name

	Name = models.CharField(max_length=100)
	dob = models.DateField('date of birth', default=dateparse.parse_date('01/01/01'), null=True)
	Address = models.CharField(max_length=200)
	mobile = models.CharField(max_length=10)
	issue = models.CharField(max_length=1000)
	profile_image = models.ImageField(null=True)
